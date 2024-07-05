from utils.ma import ma
from models.pruebas_template import PruebasTemplates

class PruebasTemplatesSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = PruebasTemplates
        fields = ('pruebas_template_id','minimo',
                  'maximo','prueba_id')
pruebas_template_schema = PruebasTemplatesSchema()
pruebas_templates_schema = PruebasTemplatesSchema(many=True)