from flask import render_template

def list(materiales):
    return render_template('materiales/index.html', materiales=materiales)

def create(categorias, autores, materias, donadores):
    return render_template('materiales/create.html', categorias=categorias, autores=autores, materias=materias, donadores=donadores)

def edit(material, categorias, autores, materias, donadores):
    return render_template('materiales/edit.html', material=material, categorias=categorias, autores=autores, materias=materias, donadores=donadores)
