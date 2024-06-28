from utils.ma import ma
from models.usuarios import Usuarios

class UsuariosSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Usuarios
        fields = ('usuario_id','nombre','apellidos','correo_electronico',
                  'contrasena', 'ubigeo')
usuario_schema = UsuariosSchema()
usuarios_schema = UsuariosSchema(many=True)