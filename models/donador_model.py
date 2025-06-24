from database import db

class Donador(db.Model):
    __tablename__ = "donadores"

    id_donador = db.Column(db.Integer,primary_key=True)
    nombre = db.Column(db.String(80),nullable=False)
    apellido = db.Column(db.String(80),nullable=False)
    telefono = db.Column(db.String(20),nullable=False)

    material = db.relationship('Material', back_populates='donador')

    def __init__(self, nombre, apellido, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
    
    #tener un obj de tipo usuario y guardarlo en la bd
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    #método para devolver los donadores de la tabla donadores
    @staticmethod #no depende de la clase
    def get_all():
        return Donador.query.all()
    
    #metodo para recuperar un solo registro
    @staticmethod
    def get_by_id(id):
        return Donador.query.get(id)
    
    #metodo para actualizar
    def update(self, nombre=None, apellido=None, telefono=None):
        if nombre:
            self.nombre = nombre
        if apellido:
            self.apellido = apellido
        if telefono:
            self.telefono = telefono
        db.session.commit()
    
    #metodo delete
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        

    def to_dict(self):
        return {
            "id_donador": self.id_donador,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "telefono": self.telefono,
        }