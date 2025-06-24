from flask import request, redirect, url_for, Blueprint

from models.materia_model import Materia
from views import materia_view

materia_bp = Blueprint('materia',__name__,url_prefix="/materias")

@materia_bp.route("/")
def index():
    materias = Materia.get_all()
    return materia_view.list(materias)

@materia_bp.route("/create", methods = ['GET','POST'])
def create():
    if request.method == 'POST':
        nombre = request.form['nombre']
    
        materia = Materia(nombre)
        materia.save()
        return redirect(url_for('materia.index'))
    return materia_view.create()

@materia_bp.route("/edit/<int:id_materia>", methods=['GET','POST'])
def edit(id_materia):
    materia = Materia.get_by_id(id_materia)
    if request.method == 'POST':
        nombre = request.form['nombre']
        materia.update(nombre=nombre)
        return redirect(url_for('materia.index'))
    return materia_view.edit(materia)

@materia_bp.route("/delete/<int:id_materia>")
def delete(id_materia):
    materia = Materia.get_by_id(id_materia)
    materia.delete()
    return redirect(url_for('materia.index'))
