from sqlalchemy import func

from utils.db import db


class Especialistas(db.Model):
    __tablename__ = 'especialistas'
    especialista_id = db.Column(db.Integer(), primary_key=True)
    nombre = db.Column(db.String(255))
    apellidos = db.Column(db.String(255))
    titulo_id = db.Column(db.Integer())
    correo_electronico = db.Column(db.String(255))
    contrasena = db.Column(db.String(255))
    ubigeo = db.Column(db.Integer())

    def __init__(self, nombre, apellidos, titulo_id, correo_electronico,
                 contrasena, ubigeo):
        self.nombre = nombre
        self.apellidos = apellidos
        self.titulo_id = titulo_id
        self.correo_electronico = correo_electronico
        self.contrasena = contrasena

        
        self.ubigeo = ubigeo

