from database import db

class Editorial(db.Model):
    __tablename__ = "editoriales"

    id_editorial = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    direccion = db.Column(db.String(50), nullable=False)
    telefono = db.Column(db.String(20), nullable=False)

    libros = db.relationship('Libro', back_populates='editorial')

    def __init__(self, nombre, direccion, telefono):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono

    def save(self):
        db.session.add(self)
        db.session.commit()

    #Ver 
    @staticmethod
    def get_all():
        return Editorial.query.all()
    
    #ver solo uno
    @staticmethod
    def get_by_id(id_editorial):
        return Editorial.query.get(id_editorial)
    
    #actualizar
    def update(self, nombre=None, direccion=None, telefono=None):
        if nombre is not None:
            self.nombre = nombre
        if direccion is not None:
            self.direccion = direccion
        if telefono is not None:
            self.telefono = telefono
        db.session.commit()


    #eliminar
    def delete(self):
        db.session.delete(self)
        db.session.commit()

