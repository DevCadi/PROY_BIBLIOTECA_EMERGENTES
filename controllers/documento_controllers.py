from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
import os

from models.documento_model import Documento
from models.material_model import Material
from database import db

documentos_bp = Blueprint('documentos', __name__, url_prefix="/documentos")
UPLOAD_FOLDER = os.path.join(os.getcwd(), 'static', 'pdf')  # Ruta absoluta

@documentos_bp.route('/')
def index():
    documentos = Documento.query.all()
    return render_template('documentos/index.html', documentos=documentos)

@documentos_bp.route('/create', methods=['GET', 'POST'])
def subir_pdf():
    materiales = Material.query.all()
    if request.method == 'POST':
        archivo = request.files['archivo']
        id_material = request.form['id_material']

        if archivo and archivo.filename.endswith('.pdf'):
            filename = secure_filename(archivo.filename)
            ruta = os.path.join(UPLOAD_FOLDER, filename)
            archivo.save(ruta)

            nuevo = Documento(nombre=filename, id_material=id_material)
            db.session.add(nuevo)
            db.session.commit()

            flash('Archivo subido correctamente.', 'success')
            return redirect(url_for('documentos.index'))

    return render_template('documentos/create.html', materiales=materiales)

@documentos_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def editar(id):
    documento = Documento.query.get_or_404(id)
    materiales = Material.query.all()
    if request.method == 'POST':
        documento.id_material = request.form['id_material']

        archivo = request.files['archivo']
        if archivo and archivo.filename.endswith('.pdf'):
            filename = secure_filename(archivo.filename)
            archivo.save(os.path.join(UPLOAD_FOLDER, filename))
            documento.nombre = filename

        db.session.commit()
        flash('Documento actualizado.', 'info')
        return redirect(url_for('documentos.index'))

    return render_template('documentos/edit.html', documento=documento, materiales=materiales)

@documentos_bp.route('/delete/<int:id>', methods=['POST'])
def eliminar(id):
    documento = Documento.query.get_or_404(id)
    try:
        archivo_path = os.path.join(UPLOAD_FOLDER, documento.nombre)  # ← CORREGIDO

        if os.path.exists(archivo_path):
            os.remove(archivo_path)
            print("Archivo eliminado correctamente:", archivo_path)
        else:
            print("Archivo no encontrado:", archivo_path)

        db.session.delete(documento)
        db.session.commit()
        flash('Documento eliminado correctamente.', 'warning')

    except Exception as e:
        flash(f'Error al eliminar: {e}', 'danger')
        print("Error al eliminar:", e)

    return redirect(url_for('documentos.index'))
