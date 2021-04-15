from graphene_django.types import DjangoObjectType
from capitania.apps.core import models


class VehiculoType(DjangoObjectType):
    class Meta:
        model = models.Vehiculo
