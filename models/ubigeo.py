from sqlalchemy import func
from utils.db import db

class Ubigeo(db.Model):
    __tablename__ = 'ubigeo'
    
    ubigeo = db.Column(db.String(6), primary_key=True)
    distrito = db.Column(db.String(255), nullable=False)
    provincia = db.Column(db.String(255), nullable=False)
    departamento = db.Column(db.String(255), nullable=False)
    poblacion = db.Column(db.Integer, nullable=False)
    superficie = db.Column(db.Float, nullable=False)
    coordenada_y = db.Column(db.Float, nullable=False)
    coordenada_x = db.Column(db.Float, nullable=False)
    
    def __init__(self, ubigeo, distrito, provincia, departamento, poblacion, superficie, coordenada_y, coordenada_x):
        self.ubigeo = ubigeo
        self.distrito = distrito
        self.provincia = provincia
        self.departamento = departamento
        self.poblacion = poblacion
        self.superficie = superficie
        self.coordenada_y = coordenada_y
        self.coordenada_x = coordenada_x
