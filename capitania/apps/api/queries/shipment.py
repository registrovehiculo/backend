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
    shipment_user_missing_in_onat = graphene.List(ShipmentType)
    shipment_user_missing_in_system = graphene.List(ClienteType)
    shipment_user_different_shipment = graphene.List(ClienteType)
    shipment_user_different_base = graphene.List(ClienteType)
    shipment_user_different_captaincy = graphene.List(ClienteType)

    def resolve_shipment(self, info):
        return Shipment.objects.all().exclude(Q(owner_name__isnull=True) | Q(owner_name='')).order_by('id_number')

    def resolve_owner_with_more_than_one_shipment(self, info):
        # dupes = Shipment.objects.values('id_number', 'shipment_name').annotate(Count('id_number')).order_by(
        #     'id_number').filter(id_number__count__gt=1)
        # return Shipment.objects.filter(id_number__in=[item['id_number'] for item in dupes]).order_by('id_number')
        return Shipment.objects.raw('SELECT distinct * FROM (SELECT s.*, COUNT(*) OVER (PARTITION BY ID_NUMBER) c FROM CORE_SHIPMENT s) WHERE c > 1')

    # Estan en el sistema embarcacion pero no en el infogesti
    def resolve_shipment_user_missing_in_onat(self, info):
        return Shipment.objects.raw('SELECT s.* from  CORE_SHIPMENT s left outer join CLIENTE@INFOGESTI info on s.ID_NUMBER = info.NIT where info.NIT IS NULL order by s.ID_NUMBER')

    # Estan en el infogesti que no estan en el sistema embarcacion
    def resolve_shipment_user_missing_in_system(self, info):
        return Cliente.objects.raw('SELECT  DISTINCT c.DPA, c.NIT, c.NOMBRE_COMPLETO, C.ID from CLIENTE_EMBARCACION@INFOGESTI emb  INNER JOIN CLIENTE@INFOGESTI c  on emb.ID_CLIENTE = c.ID LEFT outer JOIN  CORE_SHIPMENT s on s.ID_NUMBER = c.NIT where s.ID_NUMBER IS NULL ORDER BY NIT')

    # Usuarios con diferentes embarcaciones
    def resolve_shipment_user_different_shipment(self, info):
        return Cliente.objects.raw('SELECT  DISTINCT c.DPA, c.NIT, c.NOMBRE_COMPLETO, emb.NOMBRE_EMBARCACION as embarcacion, C.ID from CLIENTE_EMBARCACION@INFOGESTI emb  INNER JOIN CLIENTE@INFOGESTI c  on emb.ID_CLIENTE = c.ID INNER JOIN  CORE_SHIPMENT s on s.ID_NUMBER = c.NIT AND UPPER(s.SHIPMENT_NAME) <> UPPER(emb.NOMBRE_EMBARCACION)  order by nit')

    # Usuarios con diferentes basificaciones
    def resolve_shipment_user_different_base(self, info):
        return Cliente.objects.raw('SELECT  DISTINCT c.DPA, c.NIT, c.NOMBRE_COMPLETO, emb.NOMBRE_EMBARCACION as embarcacion,  cap.NOMBRE as capitania, bas.NOMBRE as basificacion, c.ID from C_EMBARCACION_CAPITANIA@infogesti cap inner join C_EMBARCACION_BASIFICACION@infogesti bas on cap.ID = bas.ID_CAPITANIA inner join CLIENTE_EMBARCACION@INFOGESTI emb on bas.ID = emb.ID_BASIFICACION INNER JOIN CLIENTE@INFOGESTI c  on emb.ID_CLIENTE = c.ID INNER JOIN  CORE_SHIPMENT s on s.ID_NUMBER = c.NIT AND UPPER(s.BASE_NAME) <> UPPER(bas.NOMBRE) order by NIT')

    # Usuarios con diferentes capitanias
    def resolve_shipment_user_different_captaincy(self, info):
        return Cliente.objects.raw('SELECT  DISTINCT c.DPA, c.NIT, c.NOMBRE_COMPLETO, emb.NOMBRE_EMBARCACION as embarcacion,  cap.NOMBRE as capitania, bas.NOMBRE as basificacion, c.ID from C_EMBARCACION_CAPITANIA@infogesti cap inner join C_EMBARCACION_BASIFICACION@infogesti bas on cap.ID = bas.ID_CAPITANIA inner join CLIENTE_EMBARCACION@INFOGESTI emb on bas.ID = emb.ID_BASIFICACION INNER JOIN CLIENTE@INFOGESTI c  on emb.ID_CLIENTE = c.ID INNER JOIN  CORE_SHIPMENT s on s.ID_NUMBER = c.NIT AND UPPER(s.CAPTAINCY_PROVINCE) <> UPPER(cap.NOMBRE) order by NIT')

    # Usuarios con una sola embarcacion
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
        return Shipment.objects.raw('SELECT distinct * FROM (SELECT s.*, COUNT(*) OVER (PARTITION BY ID_NUMBER) c FROM CORE_SHIPMENT s inner join  CLIENTE@infogesti ci on ci.NOMBRE_COMPLETO = s.OWNER_NAME inner join CLIENTE_EMBARCACION@infogesti ce on ci.id = ce.id_cliente)  WHERE c = 1')