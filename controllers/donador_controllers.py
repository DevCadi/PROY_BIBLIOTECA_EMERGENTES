from flask import request, redirect, url_for, Blueprint, session, abort, render_template
from utils.decorators import login_required, role_required
from models.donador_model import Donador  # Importa tu modelo
from views import donador_view  # Tu vista para donadores

# Crea el blueprint
donador_bp = Blueprint('donador', __name__, url_prefix="/donadores")

# ----------- LISTAR DONADORES -----------
@donador_bp.route("/", methods=["GET"])
@login_required
@role_required('Admin', 'Bibliotecario')
def index():
    donadores = Donador.get_all()
    return donador_view.list(donadores)

# ----------- CREAR DONADOR -----------
@donador_bp.route("/create", methods=['GET', 'POST'])
@login_required
@role_required('Admin', 'Bibliotecario')
def create():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        telefono = request.form['telefono']

        nuevo_donador = Donador(nombre, apellido, telefono)
        nuevo_donador.save()
        return redirect(url_for('donador.index'))
    return donador_view.create()

# ----------- EDITAR DONADOR -----------
@donador_bp.route("/edit/<int:id>", methods=['GET', 'POST'])
@login_required
@role_required('Admin', 'Bibliotecario')
def edit(id):
    donador_obj = Donador.get_by_id(id)  # Usar la clase/modelo Donador

    if not donador_obj:
        return "Donador no encontrado", 404

    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        telefono = request.form['telefono']

        donador_obj.update(nombre=nombre, apellido=apellido, telefono=telefono)
        return redirect(url_for('donador.index'))

    return donador_view.edit(donador_obj)


# ----------- ELIMINAR DONADOR -----------
@donador_bp.route("/delete/<int:id>", methods=['POST', 'GET'])
@login_required
@role_required('Admin')
def delete(id):
    donador = Donador.get_by_id(id)
    if not donador:
        return "Donador no encontrado", 404
    donador.delete()
    return redirect(url_for('donador.index'))
