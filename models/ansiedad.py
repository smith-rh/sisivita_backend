from utils.db import db


from utils.db import db

class Ansiedad(db.Model):
    __tablename__ = 'ansiedad'

    ansiedad_id = db.Column(db.Integer, primary_key=True)
    nivel = db.Column(db.String(255))
    semaforo = db.Column(db.String(255))

    def __init__(self, nivel, semaforo):
        self.nivel = nivel
        self.semaforo = semaforo
        