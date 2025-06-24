from database import db

class Materia(db.Model):
    __tablename__ = "materias"

    id_materia = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)

    material = db.relationship('Material', back_populates='materia')

    def __init__(self, nombre):
        self.nombre = nombre

    def save(self):
        db.session.add(self)
        db.session.commit()

    #Ver Materias
    @staticmethod
    def get_all():
        return Materia.query.all()
    
    #ver solo una Materia
    @staticmethod
    def get_by_id(id_materia):
        return Materia.query.get(id_materia)
    
    #actualizar
    def update(self, nombre=None):
        if nombre:
            self.nombre = nombre
        db.session.commit()

    #eliminar
    def delete(self):
        db.session.delete(self)
        db.session.commit()

