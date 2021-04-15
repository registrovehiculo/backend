from graphene_django.types import DjangoObjectType
from capitania.apps.core.models import InfogestiShipment, Cliente


class InfogestiShipmentType(DjangoObjectType):
    class Meta:
        model = InfogestiShipment


class ClienteType(DjangoObjectType):
    class Meta:
        model = Cliente
