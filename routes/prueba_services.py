import sqlalchemy
from flask import Blueprint, make_response, jsonify, request
from sqlalchemy import func
from sqlalchemy.sql.operators import and_

from models.ansiedad import Ansiedad
from models.diagnostico import Diagnostico
from models.opciones import Opciones
from models.opciones_predeterminadas import Opciones_predeterminadas
from models.preguntas import Preguntas
from models.respuesta import Respuestas
from models.respuesta_usuario import Respuesta_Usuario
from models.template import Templates
from models.pruebas import Pruebas
from models.usuarios import Usuarios
from schemas.respuesta_schema import respuesta_schema
from schemas.respuesta_usuario_schema import respuesta_usuario_schema, respuestas_usuario_schema
from schemas.template_schema import template_schema, templates_schema, TemplatesSchema
from schemas.pruebas_schema import pruebas_schema, prueba_schema
from schemas.usuarios_schema import usuarios_schema
from utils.db import db

prueba_services = Blueprint('prueba_services', __name__)


@prueba_services.route('/pruebas', methods=['GET'])
def get_Pruebas():
    all_usuario = Pruebas.query.all()
    result = pruebas_schema.dump(all_usuario)
    print(result)
    data = {
        'message': 'Todo los test',
        'status': 200,
        'data': result
    }
    return make_response(jsonify(data), 200)


@prueba_services.route('/pruebas/<int:id>', methods=['GET'])
def get_test(id):
    test = Pruebas.query.get(id)
    if test is None:
        data = {
            'message': 'No existe el test',
            'status': 404
        }
        return make_response(jsonify(data), 200)
    result = prueba_schema.dump(test)

    data = {
        'message': 'Test encontrado',
        'status': 200,
        'data': result
    }
    return make_response(jsonify(data), 200)


@prueba_services.route('/pruebas/all', methods=['GET'])
def get_all_tests():
    response = []

    data = (
        db.session.query(
            Pruebas.prueba_id.label('prueba_id'),
            Pruebas.titulo.label('titulo'),
            Pruebas.descripcion.label('test_description'),
            Pruebas.fecha_creacion.label('fecha_creacion'),
            Preguntas.pregunta_id.label('pregunta_id'),
            Preguntas.textopregunta.label('textopregunta'),
            Opciones.opcion_id.label('opcion_id'),
            Opciones.op_pre_id.label('op_pre_id'),
            Opciones_predeterminadas.nombre.label('nombre')
        )
        .join(Preguntas, Preguntas.prueba_id == Pruebas.prueba_id)
        .outerjoin(Opciones, Opciones.pregunta_id == Preguntas.pregunta_id)
        .join(Opciones_predeterminadas, Opciones_predeterminadas.op_pre_id == Opciones.op_pre_id)
        .all()
    )

    temp_response = {}

    for row in data:
        prueba_id = row.prueba_id
        pregunta_id = row.pregunta_id

        if prueba_id not in temp_response:
            temp_response[prueba_id] = {
                "prueba_id": prueba_id,
                "titulo": row.titulo,
                "test_description": row.test_description,
                "fecha_creacion": str(row.fecha_creacion),
                "preguntas": {}
            }
            print(row.fecha_creacion)

        if pregunta_id not in temp_response[prueba_id]["preguntas"]:
            temp_response[prueba_id]["preguntas"][pregunta_id] = {
                "pregunta_id": pregunta_id,
                "textopregunta": row.textopregunta,
                "opciones": []
            }

        if row.opcion_id:
            temp_response[prueba_id]["preguntas"][pregunta_id]["opciones"].append({
                "opcion_id": row.opcion_id,
                "op_pre_id": row.op_pre_id,
                "nombre": row.nombre
            })

    for test in temp_response.values():
        test['preguntas'] = list(test['preguntas'].values())
        response.append(test)

    if response:
        return make_response(jsonify({
            'message': 'Todos los test completos',
            'status': 200,
            'data': response}), 200)
    else:
        return make_response(jsonify({'message': 'No se encontraron datos', 'status': 404}), 200)


@prueba_services.route('/pruebas/all/<int:id>', methods=['GET'])
def get_all_test(id):
    response = []

    data = (
        db.session.query(
            Pruebas.prueba_id.label('prueba_id'),
            Pruebas.titulo.label('titulo'),
            Pruebas.descripcion.label('test_description'),
            Pruebas.fecha_creacion.label('fecha_creacion'),
            Preguntas.pregunta_id.label('pregunta_id'),
            Preguntas.textopregunta.label('textopregunta'),
            Opciones.opcion_id.label('opcion_id'),
            Opciones.op_pre_id.label('op_pre_id'),
            Opciones_predeterminadas.nombre.label('nombre')
        )
        .where(Pruebas.prueba_id == id)
        .join(Preguntas, Preguntas.prueba_id == Pruebas.prueba_id)
        .outerjoin(Opciones, Opciones.pregunta_id == Preguntas.pregunta_id)
        .join(Opciones_predeterminadas, Opciones_predeterminadas.op_pre_id == Opciones.op_pre_id)
        .all()
    )

    temp_response = {}

    for row in data:
        prueba_id = row.prueba_id
        pregunta_id = row.pregunta_id

        if prueba_id not in temp_response:
            temp_response[prueba_id] = {
                "prueba_id": prueba_id,
                "titulo": row.titulo,
                "test_description": row.test_description,
                "fecha_creacion": row.fecha_creacion,
                "preguntas": {}
            }

        if pregunta_id not in temp_response[prueba_id]["preguntas"]:
            temp_response[prueba_id]["preguntas"][pregunta_id] = {
                "pregunta_id": pregunta_id,
                "textopregunta": row.textopregunta,
                "opciones": []
            }

        if row.opcion_id:
            temp_response[prueba_id]["preguntas"][pregunta_id]["opciones"].append({
                "opcion_id": row.opcion_id,
                "op_pre_id": row.op_pre_id,
                "nombre": row.nombre
            })

    for test in temp_response.values():
        test['preguntas'] = list(test['preguntas'].values())
        response.append(test)

    if response:
        return make_response(jsonify({
            'message': 'Todos los test completos',
            'status': 200,
            'data': response}), 200)
    else:
        return make_response(jsonify({'message': 'No se encontraron datos', 'status': 404}), 200)


@prueba_services.route('/pruebas/responder', methods=['POST'])
def responder():
    try:
        fecha_fin = request.json.get('fecha_fin')
        preguntas = request.json.get('preguntas')
        usuario_id = request.json.get('usuario_id')
        if not all([fecha_fin, preguntas, usuario_id]):
            return make_response(jsonify({'message': 'Datos incompletos', 'status': 400}), 200)
        if any('pregunta_id' not in pregunta or 'opcion_id' not in pregunta for pregunta in preguntas):
            return make_response(jsonify({'message': 'Faltan datos en las preguntas', 'status': 400}), 200)

        new_respuesta_usuario = Respuesta_Usuario(usuario_id=usuario_id, fecha_fin=fecha_fin, puntuacion=0)
        db.session.add(new_respuesta_usuario)
        # db.session.commit()
        puntaje = 0

        for pregunta in preguntas:
            opcion_id = pregunta['opcion_id']
            opcion = Opciones.query.filter_by(opcion_id=opcion_id).first()
            puntaje += opcion.valor

            new_respuesta = Respuestas(opcion_id=opcion_id, res_user_id=new_respuesta_usuario.res_user_id)
            db.session.add(new_respuesta)
            # db.session.commit()

        new_respuesta_usuario.puntuacion = puntaje
        db.session.add(new_respuesta_usuario)

        templates = (db.session.query(
            Templates.template_id.label('template_id'),
            Templates.estado.label('estado'),
            Templates.max.label('max'),
            Templates.min.label('min'),
        )
                     .where(Preguntas.pregunta_id == pregunta['pregunta_id'])
                     .where(Preguntas.prueba_id == Pruebas.prueba_id)
                     .where(Pruebas.prueba_id == Templates.prueba_id)
                     .all()
                     )
        for row in templates:
            min = row.min
            max = row.max
            if (puntaje <= max and puntaje >= min):
                semaforo = row.estado
                break
        data = {
            'message': 'Respuesta Guardada',
            'puntuacion': puntaje,
            'semaforo': semaforo,
            'status': 200,
        }
        db.session.commit()

        return make_response(jsonify(data), 200)
    except Exception as e:
        db.session.rollback()
        print(e)
        return make_response(jsonify({'message': 'Error al guardar respuesta', 'status': 500}), 200)


@prueba_services.route('/pruebas/mapadecalor', methods=['GET'])
def getTestResuelto():
    user_responses = (
        db.session.query(
            Usuarios.usuario_id.label('usuario_id'),
            Usuarios.ubigeo.label('ubigeo'),
            Respuesta_Usuario.puntuacion.label('puntuacion'),
            Templates.estado.label('estado'),
            Templates.max.label('max'),
            Templates.min.label('min'),
            Templates.template_id.label('template_id'),
            Templates.prueba_id.label('prueba_id')
        )
        .join(Respuesta_Usuario, Usuarios.usuario_id == Respuesta_Usuario.usuario_id)
        .join(Respuestas, Respuestas.res_user_id == Respuesta_Usuario.res_user_id)
        .join(Opciones, Opciones.opcion_id == Respuestas.opcion_id)
        .join(Preguntas, Preguntas.pregunta_id == Opciones.pregunta_id)
        .join(Pruebas, Pruebas.prueba_id == Preguntas.prueba_id)
        .join(Templates, Templates.prueba_id == Pruebas.prueba_id)
        .where(and_(
            Templates.min <= Respuesta_Usuario.puntuacion,
            Templates.max >= Respuesta_Usuario.puntuacion
        ))
        .group_by(
            Usuarios.usuario_id,
            Usuarios.ubigeo,
            Respuesta_Usuario.puntuacion,
            Templates.estado,
            Templates.max,
            Templates.min,
            Templates.template_id,
            Templates.prueba_id
        )
        .all()
    )

    response =[]
    for row in user_responses:
        max_value = db.session.query(func.max(Templates.max)).filter_by(prueba_id=row.prueba_id).scalar()
        response.append ( {
            'puntuacion': row.puntuacion,
            'estado': row.estado,
            'ubigeo': row.ubigeo,
            'maximo': max_value
        })
    data = {
        'message': 'Respuesta Guardada',
        'data': response,
        'status': 200,
    }
    db.session.commit()

    return make_response(jsonify(data), 200)

@prueba_services.route('/pruebas/vigilancia',methods=['GET'])

def getVigilancia():
    query = (
        db.session.query(
            Usuarios.nombre,
            Usuarios.apellidos,
            Respuesta_Usuario.res_user_id,
            Respuesta_Usuario.fecha_fin,
            Respuesta_Usuario.puntuacion,
            Pruebas.prueba_id,
            Pruebas.titulo,
            Templates.estado,
            Respuesta_Usuario.diagnostico_id,
            Diagnostico.ansiedad_id,
            Ansiedad.nivel
        )
        .join(Respuesta_Usuario, Respuesta_Usuario.usuario_id == Usuarios.usuario_id)
        .join(Respuestas, Respuestas.res_user_id == Respuesta_Usuario.res_user_id)
        .join(Opciones, Opciones.opcion_id == Respuestas.opcion_id)
        .join(Preguntas, Preguntas.pregunta_id == Opciones.pregunta_id)
        .join(Pruebas, Pruebas.prueba_id == Preguntas.prueba_id)
        .outerjoin(Diagnostico, Diagnostico.diagnostico_id == Respuesta_Usuario.diagnostico_id)
        .outerjoin(Ansiedad, Ansiedad.ansiedad_id == Diagnostico.ansiedad_id)
        .join(Templates, Templates.prueba_id == Pruebas.prueba_id)
        .filter(Respuesta_Usuario.puntuacion.between(Templates.min, Templates.max))
        .all()
    )
    results = []
    for row in query:
        result = {
            'nombre': row.nombre,
            'apellidos': row.apellidos,
            'res_user_id': row.res_user_id,
            'fecha_fin': str(row.fecha_fin),
            'puntuacion': row.puntuacion,
            'prueba_id': row.prueba_id,
            'titulo': row.titulo,
            'estado': row.estado,
            'diagnostico_id': row.diagnostico_id,
            'ansiedad_id': row.ansiedad_id,
            'nivel': row.nivel
        }
        results.append(result)

    return make_response(jsonify({'message': 'Datos encontrados', 'status': 200, 'data': results}), 200)