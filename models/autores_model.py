from database import db

class Autores(db.Model):
    __tablename__ = "autores"

    id_autor = db.Column(db.Integer,primary_key=True)
    nombre = db.Column(db.String(150),nullable=False)
    apellidos = db.Column(db.String(150),nullable=False)
    nacionalidad = db.Column(db.String(150))

    materiales = db.relationship('Material', back_populates='autor')

    def __init__(self, nombre, apellidos ,nacionalidad):
        self.nombre = nombre
        self.apellidos = apellidos
        self.nacionalidad = nacionalidad
    
    #tener un obj de tipo usuario y guardarlo en la bd
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    #método para devolver los usuarios de la tabla usuarios
    @staticmethod #no depende de la clase
    def get_all():
        return Autores.query.all()
    
    #metodo para recuperar un solo registro
    @staticmethod
    def get_by_id(id):
        return Autores.query.get(id)
    
    #metodo para actualizar
    def update(self, nombre=None, apellidos=None,nacionalidad=None):
        if nombre and apellidos and nacionalidad:
            self.nombre = nombre
            self.apellidos = apellidos
            self.nacionalidad = nacionalidad
        db.session.commit()
    
    #metodo delete
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        
    def to_dict(self):
        return {
            'id_autor': self.id_autor,
            'nombre': self.nombre,
            'apellidos': self.apellidos,
            'nacionalidad': self.nacionalidad
        }