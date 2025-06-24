# controllers/dashboard_controllers.py
from flask import Blueprint, render_template, jsonify
from models.usuario_model import Usuario
from models.prestamo_model import Prestamo
from models.material_model import Material
from sqlalchemy import extract, func
from database import db

# Blueprint para dashboard
dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/')
def index():
    total_lectores = Usuario.query.filter_by(tipo='Lector').count() or 0
    total_prestamos = Prestamo.query.count() or 0

    ranking_materiales = (
        db.session.query(Material.titulo, func.count(Prestamo.id_material))
        .join(Prestamo, Material.id_material == Prestamo.id_material)
        .group_by(Material.titulo)
        .order_by(func.count(Prestamo.id_material).desc())
        .limit(5)
        .all()
    )

    return render_template(
        'dashboard.html',
        total_lectores=total_lectores,
        total_prestamos=total_prestamos,
        ranking_materiales=ranking_materiales
    )

@dashboard_bp.route('/grafico-prestamos')
def grafico_prestamos():
    datos = (
        db.session.query(
            extract('month', Prestamo.fecha_prestamo).label('mes'),
            func.count(Prestamo.id_prestamo).label('cantidad')
        )
        .group_by(extract('month', Prestamo.fecha_prestamo))
        .order_by(extract('month', Prestamo.fecha_prestamo))
        .all()
    )
    
    # Preparar respuesta JSON
    meses = [int(row.mes) for row in datos]
    cantidades = [int(row.cantidad) for row in datos]
    return jsonify({'meses': meses, 'cantidades': cantidades})
