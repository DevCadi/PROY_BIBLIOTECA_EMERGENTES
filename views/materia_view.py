from flask import render_template

def list(materias):
    return render_template('materias/index.html', materias=materias)

def create():
    return render_template('materias/create.html')

def edit(materia):
    return render_template('materias/edit.html', materia=materia)