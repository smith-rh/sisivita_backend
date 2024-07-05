from flask import jsonify, make_response, request
from flask import Blueprint, request, make_response, jsonify # type: ignore
from utils.db import db
from models.usuarios import Usuarios
from models.respuesta_usuario import Respuesta_Usuario
from models.ubigeo import Ubigeo

vigilancia_services = Blueprint('vigilancia_services', __name__)

@vigilancia_services.route('/usuarios_con_resultados', methods=['GET'])
def get_usuarios_con_resultados():
    sort_by = request.args.get('sort_by', 'puntuacion')  # Default sort by 'puntuacion'
    sort_order = request.args.get('sort_order', 'asc')  # Default sort order 'asc'

    if sort_order == 'desc':
        results = db.session.query(Usuarios, Respuesta_Usuario, Ubigeo).join(Respuesta_Usuario).join(Ubigeo).order_by(Respuesta_Usuario.puntuacion.desc()).all()
    else:
        results = db.session.query(Usuarios, Respuesta_Usuario, Ubigeo).join(Respuesta_Usuario).join(Ubigeo).order_by(Respuesta_Usuario.puntuacion.asc()).all()
    
    result_data = []
    for usuario, respuesta_usuario, ubigeo in results:
        result_data.append({
            'usuario_id': usuario.usuario_id,
            'nombre': usuario.nombre,
            'apellidos': usuario.apellidos,
            'correo_electronico': usuario.correo_electronico,
            'ubigeo': usuario.ubigeo,
            'distrito': ubigeo.distrito,
            'provincia': ubigeo.provincia,
            'departamento': ubigeo.departamento,
            'puntuacion': respuesta_usuario.puntuacion,
            'fecha_fin': respuesta_usuario.fecha_fin,
            'diagnostico_id': respuesta_usuario.diagnostico_id
        })

    data = {
        'message': 'Usuarios con resultados fetched successfully',
        'status': 200,
        'data': result_data
    }
    return make_response(jsonify(data), 200)
