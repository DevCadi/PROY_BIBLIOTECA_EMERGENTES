from database import db

class Proyecto(db.Model):
    __tablename__ = "proyecto_academico"

    id_pro = db.Column(db.Integer, primary_key=True)
    id_material = db.Column(db.Integer, db.ForeignKey('materiales.id_material'), nullable=False)
    gestion = db.Column(db.Integer, nullable=False)
    modalidad = db.Column(db.String(50), nullable=False)

    material = db.relationship('Material', back_populates = 'proyecto_academico')

    def __init__(self, id_material ,gestion, modalidad):
        self.id_material = id_material
        self.gestion = gestion
        self.modalidad = modalidad

    def save(self):
        db.session.add(self)
        db.session.commit()

    #Ver 
    @staticmethod
    def get_all():
        return Proyecto.query.all()
    
    #ver solo uno
    @staticmethod
    def get_by_id(id_pro):
        return Proyecto.query.get(id_pro)
    
    #actualizar
    def update(self, id_material=None ,gestion=None, modalidad=None):
        if gestion and id_material and modalidad:
            self.id_material = id_material
            self.gestion = gestion
            self.modalidad = modalidad
        db.session.commit()

    #eliminar
    def delete(self):
        db.session.delete(self)
        db.session.commit()

