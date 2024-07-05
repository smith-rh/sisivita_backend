from utils.db import db


class PruebasTemplates(db.Model):
    __tablename__ = 'pruebas_template'

    pruebas_template_id = db.Column(db.Integer, primary_key=True)
    minimo = db.Column(db.Integer)
    maximo = db.Column(db.Integer)
    estado = db.Column(db.String(255))
    prueba_id = db.Column(db.Integer, db.ForeignKey('pruebas.prueba_id'))
    
    def __init__(self, pruebas_template_id, minimo, maximo):
        self.pruebas_template_id_id = pruebas_template_id
        self.minimo = minimo
        self.maximo = maximo
