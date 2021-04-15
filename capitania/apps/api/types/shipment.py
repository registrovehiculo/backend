from graphene_django.types import DjangoObjectType
from capitania.apps.core.models import Shipment


class ShipmentType(DjangoObjectType):
    class Meta:
        model = Shipment

