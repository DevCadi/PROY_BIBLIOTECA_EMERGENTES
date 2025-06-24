from database import db

class Documento(db.Model):
    __tablename__ = "documentos"

    id_documento = db.Column(db.Integer, primary_key=True)
    id_material = db.Column(db.Integer, db.ForeignKey('materiales.id_material'), nullable=False)
    nombre = db.Column(db.String(150), nullable=False)

    material = db.relationship('Material', back_populates = 'documento')
    
    @property
    def id(self):
        return self.id_documento
    
    def __init__(self ,id_material, nombre):
        self.id_material = id_material
        self.nombre = nombre

    def save(self):
        db.session.add(self)
        db.session.commit()

    #Ver categorias
    @staticmethod
    def get_all():
        return Documento.query.all()
    
    #ver solo una categoria
    @staticmethod
    def get_by_id(id_documento):
        return Documento.query.get(id_documento)
    
    #actualizar
    def update(self, id_material=None, nombre=None):
        if id_material and nombre:
            self.id_material = id_material
            self.nombre = nombre
        db.session.commit()

    #eliminar
    def delete(self):
        db.session.delete(self)
        db.session.commit()

