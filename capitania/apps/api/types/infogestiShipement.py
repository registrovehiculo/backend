from graphene_django.types import DjangoObjectType
from capitania.apps.core import models

class InfogestiShipmentType(DjangoObjectType):
    class Meta:
        model = models.InfogestiShipment


class ClienteType(DjangoObjectType):
    class Meta:
        model = models.Cliente
