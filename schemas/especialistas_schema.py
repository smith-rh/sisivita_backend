from models.especialistas import Especialistas
from utils.ma import ma


class EspecialistasSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Especialistas
        fields = ('especialista_id','nombre','apellidos', 'correo_electronico',
                  'contrasena','fecha_registro','ubigeo', 'colegiatura')
especialista_schema = EspecialistasSchema()
especialistas_schema = EspecialistasSchema(many=True)