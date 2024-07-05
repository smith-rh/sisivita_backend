from sqlalchemy import func
from utils.db import db


class Personas(db.Model):
    __tablename__ = 'personas'

    persona_id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)
    apellidos = db.Column(db.String(255), nullable=False)
    ubigeo = db.Column(db.String(6), nullable=False)
    correo_electronico = db.Column(db.String(255), nullable=True)
    contrasena = db.Column(db.String(255), nullable=True)

    def __init__(self, nombre, apellidos, ubigeo, correo_electronico=None, contrasena=None):
        self.nombre = nombre
        self.apellidos = apellidos
        self.ubigeo = ubigeo
        self.correo_electronico = correo_electronico
        self.contrasena = contrasena


  
