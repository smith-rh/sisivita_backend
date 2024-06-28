from datetime import datetime, date  # Asegúrate de importar date

from flask import Blueprint, request
from models.respuesta import Respuestas  # Ajusta la importación según el nombre correcto

respuesta_routes = Blueprint('respuesta_routes', __name__)

@respuesta_routes.route('/respuesta', methods=['POST'])
def create_respuesta():
    usuario_id = request.json.get('usuario_id')
    respuesta_id = request.json.get('respuesta_id')
    fecha_fin = date.today()  # Utiliza date.today() para obtener solo la fecha

    new_respuesta = Respuestas(usuario_id=usuario_id, respuesta_id=respuesta_id, fecha_fin=fecha_fin)
    # Aquí deberías guardar `new_respuesta` en la base de datos o realizar la lógica necesaria
    
    return 'Respuesta creada correctamente', 201  # Ejemplo de respuesta HTTP 201

