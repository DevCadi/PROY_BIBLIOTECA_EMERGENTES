from flask import render_template

def list(donadores):
    return render_template('donadores/index.html', donadores=donadores)

def create():
    return render_template('donadores/create.html')

def edit(donador):
    return render_template('donadores/edit.html', donador=donador)