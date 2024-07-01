from flask import Flask
from flask_cors import CORS

from routes.opciones_routes import opciones_routes
from routes.preguntas_services import preguntas_services
from routes.prueba_services import prueba_services
from routes.especialistas_services import especialistas_services
from routes.titulo_routes import titulo_routes
from routes.usuarios_routes import usuarios_routes
from config import DATABASE_CONNECTION_URI
from utils.db import db

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_CONNECTION_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_POOL_SIZE"] = 20
app.config["SQLALCHEMY_POOL_TIMEOUT"] = 30
app.config["SQLALCHEMY_POOL_RECYCLE"] = 1800

# no cache
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

db.init_app(app)

app.register_blueprint(usuarios_routes)
#app.register_blueprint(especialistas_services)
#app.register_blueprint(prueba_services)
#app.register_blueprint(preguntas_services)
#app.register_blueprint(opciones_routes)
#app.register_blueprint(titulo_routes)

with app.app_context():
    db.create_all()

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True,port=5000)
