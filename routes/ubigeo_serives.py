'''
from flask import Flask, jsonify, request
from utils.db import db
from models import Usuarios, Ubicaciones

app = Flask(__name__)

@app.route('/usuario/<int:usuario_id>', methods=['GET'])
def get_usuario(usuario_id):
    # Buscar el usuario por su ID
    usuario = Usuarios.query.get(usuario_id)
    if not usuario:
        return jsonify({'error': 'Usuario no encontrado'}), 404

    # Buscar la ubicación basada en el ubigeo del usuario
    ubicacion = Ubicaciones.query.get(usuario.ubigeo)
    if not ubicacion:
        return jsonify({'error': 'Ubicación no encontrada'}), 404

    # Combinar los datos del usuario y la ubicación en la respuesta
    usuario_data = {
        'usuario_id': usuario.usuario_id,
        'nombre': usuario.nombre,
        'apellidos': usuario.apellidos,
        'correo_electronico': usuario.correo_electronico,
        'ubigeo': usuario.ubigeo,
        'ubicacion': {
            'distrito': ubicacion.distrito,
            'provincia': ubicacion.provincia,
            'departamento': ubicacion.departamento,
            'poblacion': ubicacion.poblacion,
            'superficie': ubicacion.superficie,
            'y': ubicacion.y,
            'x': ubicacion.x
        }
    }
    return jsonify(usuario_data)

if __name__ == '__main__':
    app.run(debug=True)
'''