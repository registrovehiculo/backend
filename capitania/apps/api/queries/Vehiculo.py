import graphene

from capitania.apps.api.types.vehiculo import VehiculoType
from capitania.apps.core.models import Vehiculo


class VehiculoQuery(graphene.ObjectType):
    vehiculo = graphene.List(VehiculoType, datospersona=graphene.String())

    def resolve_vehiculo(self, info, **kwargs):
        vehiculo = None
        datos_persona = kwargs.get('datospersona')
        if datos_persona is not None:
            try:
                vehiculo = Vehiculo.objects.filter(datospersona=datos_persona)
            except Vehiculo.DoesNotExist:
                return None

        return vehiculo


schema = graphene.Schema(query=VehiculoQuery, auto_camelcase=False)