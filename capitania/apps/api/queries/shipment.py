import graphene
from django.db.models.aggregates import Count
from django.db.models.query_utils import Q

from capitania.apps.api.types.infogestiShipement import ClienteType
from capitania.apps.api.types.shipment import ShipmentType
from capitania.apps.core.models import Shipment, Cliente


class ShipmentQuery:
    shipment = graphene.List(ShipmentType)
    owner_with_more_than_one_shipment = graphene.List(ShipmentType)
    owner_with_different_name_equal_id = graphene.List(ShipmentType)
    owner_with_one_shipment = graphene.List(ShipmentType)
    registered_owners_more_than_one = graphene.List(ShipmentType)
    registered_owners_one = graphene.List(ShipmentType)

    def resolve_shipment(self, info):
        return Shipment.objects.all().exclude(Q(owner_name__isnull=True) | Q(owner_name='')).order_by('id_number')

    def resolve_owner_with_more_than_one_shipment(self, info):
        # dupes = Shipment.objects.values('id_number', 'shipment_name').annotate(Count('id_number')).order_by(
        #     'id_number').filter(id_number__count__gt=1)
        # return Shipment.objects.filter(id_number__in=[item['id_number'] for item in dupes]).order_by('id_number')
        return Shipment.objects.raw('SELECT distinct * FROM (SELECT s.*, COUNT(*) OVER (PARTITION BY ID_NUMBER) c FROM CORE_SHIPMENT s) WHERE c > 1')


    def resolve_owner_with_one_shipment(self, info):
        return Shipment.objects.raw('SELECT distinct * FROM (SELECT s.*, COUNT(*) OVER (PARTITION BY ID_NUMBER) c FROM CORE_SHIPMENT s) WHERE c = 1')
        # return Shipment.objects.raw('SELECT * FROM CORE_SHIPMENT WHERE (ID_NUMBER, OWNER_NAME) IN (SELECT ID_NUMBER, OWNER_NAME FROM CORE_SHIPMENT GROUP BY ID_NUMBER, OWNER_NAME HAVING COUNT(*) > 1) ORDER BY ID_NUMBER, OWNER_NAME')

    def resolve_owner_with_different_name_equal_id(self, info):
        return Shipment.objects.raw(
            'SELECT distinct  * FROM (SELECT s.*, COUNT(*) OVER (PARTITION BY ID_NUMBER) c FROM CORE_SHIPMENT s) WHERE c > 1 order by ID_NUMBER')

    def resolve_registered_owners(self, info):
        return Cliente.objects.raw(
            'Select * from CLIENTE_EMBARCACION@infogesti ce inner join CLIENTE@infogesti ci on ci.id = ce.id_cliente inner join CORE_SHIPMENT t on t.OWNER_NAME = ci.NOMBRE_COMPLETO')


    def resolve_registered_owners_more_than_one(self, info):
        return Shipment.objects.raw('SELECT distinct * FROM (SELECT s.*, COUNT(*) OVER (PARTITION BY ID_NUMBER) c FROM CORE_SHIPMENT s inner join  CLIENTE@infogesti ci on ci.NOMBRE_COMPLETO = s.OWNER_NAME inner join CLIENTE_EMBARCACION@infogesti ce on ci.id = ce.id_cliente)  WHERE c > 1')

    def resolve_registered_owners_one(self, info):
        return Shipment.objects.raw('    SELECT distinct * FROM (SELECT s.*, COUNT(*) OVER (PARTITION BY ID_NUMBER) c FROM CORE_SHIPMENT s inner join  CLIENTE@infogesti ci on ci.NOMBRE_COMPLETO = s.OWNER_NAME inner join CLIENTE_EMBARCACION@infogesti ce on ci.id = ce.id_cliente)  WHERE c = 1')