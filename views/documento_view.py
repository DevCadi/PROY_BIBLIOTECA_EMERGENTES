from flask import render_template

def list(documentos):
    return render_template('documentos/index.html', documentos=documentos)

def create(materiales):
    return render_template('documentos/create.html', materiales=materiales)

def edit(documento, materiales):
    return render_template('documentos/edit.html', documento=documento, materiales=materiales)
