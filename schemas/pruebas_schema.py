from models.pruebas import Pruebas
from utils.ma import ma


class TestSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Pruebas
        fields = ('test_id','titulo','descripcion','fecha_creacion', 'template_id')
prueba_schema = TestSchema()
pruebas_schema = TestSchema(many=True)