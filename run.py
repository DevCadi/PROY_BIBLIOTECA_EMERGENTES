from flask import Flask, request, render_template, session, redirect, url_for
from sqlalchemy import or_
from models.material_model import Material
from models.usuario_model import Usuario
from database import db
# Añade este import arriba junto con los demás:
from models.documento_model import Documento

from controllers import (
    categoria_controllers, autores_controllers, usuario_controllers,donador_controllers, audio_controllers,
    bibliotecario_controllers, editorial_controllers, video_controllers, libro_controllers,
    material_controllers, prestamo_controllers, proyectos_academicos_controllers,
    auth_controllers, reporte_controllers,dashboard_controllers, materia_controllers, documento_controllers
)

app = Flask(__name__)
app.secret_key = 'mi_clave_secreta_segura'

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///biblioteca.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

# Registrar blueprints
app.register_blueprint(audio_controllers.audio_bp, url_prefix='/audios')
app.register_blueprint(usuario_controllers.usuario_bp, url_prefix='/usuarios')
app.register_blueprint(donador_controllers.donador_bp, url_prefix='/donadores')
app.register_blueprint(bibliotecario_controllers.bibliotecario_bp, url_prefix='/bibliotecarios')
app.register_blueprint(categoria_controllers.categoria_bp, url_prefix='/categorias')
app.register_blueprint(autores_controllers.autor_bp, url_prefix='/autores')
app.register_blueprint(editorial_controllers.editorial_bp, url_prefix='/editoriales')
app.register_blueprint(video_controllers.video_bp, url_prefix='/videos')
app.register_blueprint(libro_controllers.libro_bp, url_prefix='/libros')
app.register_blueprint(material_controllers.material_bp, url_prefix='/materiales')
app.register_blueprint(prestamo_controllers.prestamo_bp, url_prefix='/prestamos')
app.register_blueprint(proyectos_academicos_controllers.proyecto_bp, url_prefix='/proyectos_academicos')
app.register_blueprint(auth_controllers.auth_bp, url_prefix='/auth')
app.register_blueprint(reporte_controllers.reporte_bp, url_prefix='/reportes')
app.register_blueprint(dashboard_controllers.dashboard_bp, url_prefix='/dashboard')
app.register_blueprint(materia_controllers.materia_bp, url_prefix='/materias')
app.register_blueprint(documento_controllers.documentos_bp, url_prefix='/documentos')


@app.route("/")
def home():
    tipo = request.args.get("tipo")
    buscar = request.args.get("buscar")

    query = Material.query

    if tipo:
        if tipo.lower() == 'proyecto':
            query = query.filter(
                or_(
                    Material.tipo.ilike('%proyecto%'),
                    Material.tipo.ilike('%tesis%')
                )
            )
        else:
            query = query.filter(Material.tipo.ilike(f"%{tipo}%"))

    if buscar:
        query = query.filter(Material.titulo.ilike(f"%{buscar}%"))

    materiales = query.all()
    documentos = Documento.get_all()  # 👈 Traer todos los documentos

    # Redirección según tipo de usuario
    if 'usuario_tipo' in session:
        if session['usuario_tipo'].lower() != 'lector':
            return redirect(url_for('dashboard.index'))
        else:
            return render_template(
                'home_lector.html',
                materiales=materiales,
                documentos=documentos
            )

    return render_template(
        'home_lector.html',
        materiales=materiales,
        documentos=documentos
    )


# Crear admin inicial si no existe
def crear_admin_inicial():
    admin_existente = Usuario.query.filter_by(tipo="Admin").first()
    if not admin_existente:
        admin = Usuario(
            nombre="Genesis",
            apellido="Campos",
            email="genesis@gmail.com",
            telefono="77587271",
            username="admin",
            password="123",
            tipo="Admin"
        )
        admin.save()
        print("Usuario Admin creado automáticamente.")
    else:
        print("Usuario Admin ya existe.")

@app.route('/carrera')
def carrera():
    return render_template('carrera.html')

@app.route('/juego')
def juego():
    return render_template('juego.html')

@app.route('/ubicacion')
def ubicacion():
    return render_template('ubicacion.html')

@app.route('/terminos')
def terminos():
    return render_template('terminos.html')

@app.route('/privacidad')
def privacidad():
    return render_template('privacidad.html')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        crear_admin_inicial()
    app.run(debug=True)
