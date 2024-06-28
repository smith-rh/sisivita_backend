from sqlalchemy import func
from utils.db import db


class Usuarios(db.Model):
    __tablename__ = 'usuarios'

    usuario_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(255))
    correo_electronico = db.Column(db.String(255), unique=True)
    contrasena = db.Column(db.String(255))
    apellidos = db.Column(db.String(255))
    ubigeo = db.Column(db.Integer)

    def __init__(self, nombre, apellidos,
                 correo_electronico, contrasena, ubigeo):
        self.nombre = nombre
        self.apellidos = apellidos
        self.correo_electronico = correo_electronico
        self.contrasena = contrasena
        self.ubigeo = ubigeo