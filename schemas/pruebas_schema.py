from models.pruebas import Pruebas
from utils.ma import ma


class PruebaSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Pruebas
        fields = ('prueba_id','titulo','descripcion','fecha_creacion', 'pruebas_template_id')
prueba_schema = PruebaSchema()
pruebas_schema = PruebaSchema(many=True)