from flask import request, redirect, url_for, Blueprint
from models.material_model import Material
from models.categoria_model import Categoria
from models.autores_model import Autores
from models.materia_model import Materia
from models.donador_model import Donador
from views import categoria_view
from views import material_view

material_bp = Blueprint('material', __name__, url_prefix='/materiales')

@material_bp.route("/")
def index():
    materiales = Material.get_all()
    return material_view.list(materiales)

@material_bp.route("/create", methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        tipo = request.form['tipo']
        titulo = request.form['titulo']
        fecha_ingreso = request.form['fecha_ingreso']
        estado = request.form['estado']
        id_categoria = request.form['id_categoria']
        id_autor = request.form['id_autor']
        id_materia = request.form['id_materia']
        id_donador = request.form['id_donador']

        material = Material(tipo, titulo, fecha_ingreso, estado, id_categoria, id_autor, id_materia, id_donador)
        material.save()
        return redirect(url_for('material.index'))
    categorias = Categoria.query.all()
    autores = Autores.query.all()
    materias = Materia.query.all()
    donadores = Donador.query.all()

    return material_view.create(categorias=categorias, autores=autores, materias=materias, donadores=donadores)

@material_bp.route("/edit/<int:id_material>", methods=['GET', 'POST'])
def edit(id_material):
    material = Material.get_by_id(id_material)
    if request.method == 'POST':
        tipo = request.form['tipo']
        titulo = request.form['titulo']
        fecha_ingreso = request.form['fecha_ingreso']
        estado = request.form['estado']
        id_categoria = request.form['id_categoria']
        id_autor = request.form['id_autor']
        id_materia = request.form['id_materia']
        id_donador = request.form['id_donador']

        material.update(tipo=tipo, titulo=titulo, fecha_ingreso=fecha_ingreso, estado=estado, id_categoria=id_categoria, id_autor=id_autor, id_materia=id_materia, id_donador=id_donador)
        return redirect(url_for('material.index'))

    categorias = Categoria.query.all()
    autores = Autores.query.all()
    materias = Materia.query.all()
    donadores = Donador.query.all()

    return material_view.edit(material=material, categorias=categorias, autores=autores, materias=materias, donadores=donadores)

@material_bp.route("/delete/<int:id_material>")
def delete(id_material):
    material = Material.get_by_id(id_material)
    material.delete()
    return redirect(url_for('material.index'))
