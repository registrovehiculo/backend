import graphene
from django.db.models import Q
from django.db.models.functions import Length

from capitania.apps.api.types.provincias import SanticEspiritudType
from capitania.apps.api.types.infogestiShipement import ClienteType
from capitania.apps.core.models import SanticEspiritud, Cliente


class ContributorsFromSanticEspiritudQuery(graphene.ObjectType):
    contributors_missing_in_onat_santic_espiritud = graphene.List(SanticEspiritudType)
    contributors_with_different_information_santic_espiritud_plate = graphene.List(SanticEspiritudType)
    contributors_with_different_information_santic_espiritud_name = graphene.List(SanticEspiritudType)
    contributors_with_equals_information_santic_espiritud = graphene.List(SanticEspiritudType)
    espiritud_name_infogesti = graphene.List(ClienteType)
    wrong_id_santic_espiritud = graphene.List(SanticEspiritudType)
    santic_espiritud = graphene.List(SanticEspiritudType)

    # 1 Contribuyentes que estan en capitania vehiculo que no estan en la onat
    def resolve_contributors_missing_in_onat_santic_espiritud(self, info):
        return SanticEspiritud.objects.raw('select distinct reca.* from CORE_SANTICESPIRITUD reca left outer join cliente@infogesti c on reca.NUMEROIDENTIDAD = c.nit left outer join cliente_tt@infogesti tt on tt.id_cliente =c.id where tt.id_cliente is null')

    # 2 Contribuyentes que estan en ambos capitania con informaciones diferentes
    def resolve_contributors_with_different_information_santic_espiritud_plate(self, info):
        return SanticEspiritud.objects.raw('SELECT DISTINCT RECA.* FROM DIRECCION@INFOGESTI DIR INNER JOIN CLIENTE_DIRECCION@INFOGESTI C_DIR ON DIR.ID = C_DIR.ID_DIRECCION INNER JOIN CLIENTE@INFOGESTI C ON C.ID = C_DIR.ID_CLIENTE INNER JOIN CLIENTE_TT@INFOGESTI TT ON TT.ID_CLIENTE = C.ID INNER JOIN CORE_SANTICESPIRITUD RECA ON C.NIT = RECA.NUMEROIDENTIDAD WHERE C.UNIDAD BETWEEN 2801 AND 2808 AND TT.MATRICULA <> RECA.CHAPANUEVA')


    def resolve_contributors_with_different_information_santic_espiritud_name(self, info):
        return SanticEspiritud.objects.raw('SELECT RECA.* FROM DIRECCION@INFOGESTI DIR INNER JOIN CLIENTE_DIRECCION@INFOGESTI C_DIR ON DIR.ID = C_DIR.ID_DIRECCION INNER JOIN CLIENTE@INFOGESTI C ON C.ID = C_DIR.ID_CLIENTE INNER JOIN CLIENTE_TT@INFOGESTI TT ON TT.ID_CLIENTE = C.ID INNER JOIN CORE_SANTICESPIRITUD RECA ON C.NIT = RECA.NUMEROIDENTIDAD WHERE C.UNIDAD BETWEEN 2801 AND 2808 AND UPPER(C.NOMBRE_COMPLETO) <> UPPER(RECA.DATOSPERSONA) AND  upper(substr(C.NOMBRE_COMPLETO, 0, 1)) <> upper(substr(RECA.DATOSPERSONA, 0, 1)) AND  upper(substr(C.NOMBRE_COMPLETO, 2, 1)) <> upper(substr(RECA.DATOSPERSONA, 2, 1)) AND  upper(substr(C.NOMBRE_COMPLETO, 0, 1)) <> upper(substr(RECA.DATOSPERSONA, 2, 1)) AND  upper(substr(C.NOMBRE_COMPLETO, 2, 1)) <> upper(substr(RECA.DATOSPERSONA, 0, 1)) order by RECA.NUMEROIDENTIDAD')

    def resolve_espiritud_name_infogesti(self, info):
        return Cliente.objects.raw('SELECT C.NOMBRE_COMPLETO, C.id, c.nit FROM DIRECCION@INFOGESTI DIR INNER JOIN CLIENTE_DIRECCION@INFOGESTI C_DIR ON DIR.ID = C_DIR.ID_DIRECCION INNER JOIN CLIENTE@INFOGESTI C ON C.ID = C_DIR.ID_CLIENTE INNER JOIN CLIENTE_TT@INFOGESTI TT ON TT.ID_CLIENTE = C.ID INNER JOIN CORE_SANTICESPIRITUD RECA ON C.NIT = RECA.NUMEROIDENTIDAD WHERE C.UNIDAD BETWEEN 2801 AND 2808 AND UPPER(C.NOMBRE_COMPLETO) <> UPPER(RECA.DATOSPERSONA) AND  upper(substr(C.NOMBRE_COMPLETO, 0, 1)) <> upper(substr(RECA.DATOSPERSONA, 0, 1)) AND  upper(substr(C.NOMBRE_COMPLETO, 2, 1)) <> upper(substr(RECA.DATOSPERSONA, 2, 1)) AND  upper(substr(C.NOMBRE_COMPLETO, 0, 1)) <> upper(substr(RECA.DATOSPERSONA, 2, 1)) AND  upper(substr(C.NOMBRE_COMPLETO, 2, 1)) <> upper(substr(RECA.DATOSPERSONA, 0, 1)) order by C.nit')

    # 4 Contribuyentes totalmente coincidentes
    def resolve_contributors_with_equals_information_santic_espiritud(self, info):
        return SanticEspiritud.objects.raw('SELECT DISTINCT RECA.* FROM DIRECCION@INFOGESTI DIR INNER JOIN CLIENTE_DIRECCION@INFOGESTI C_DIR ON DIR.ID = C_DIR.ID_DIRECCION INNER JOIN CLIENTE@INFOGESTI C ON C.ID = C_DIR.ID_CLIENTE INNER JOIN CLIENTE_TT@INFOGESTI TT ON TT.ID_CLIENTE = C.ID INNER JOIN CORE_SANTICESPIRITUD RECA ON C.NIT = RECA.NUMEROIDENTIDAD WHERE C.UNIDAD BETWEEN 2801 AND 2808 AND UPPER(C.NOMBRE_COMPLETO) = UPPER(RECA.DATOSPERSONA) AND TT.MATRICULA = RECA.CHAPANUEVA')

    def resolve_wrong_id_santic_espiritud(self, info):
        return SanticEspiritud.objects.annotate(numeroidentidad_len=Length('numeroidentidad')).filter(Q(
            numeroidentidad_len__lt=5) | Q(numeroidentidad__isnull=True) | Q(datospersona__isnull=True))

    def resolve_santic_espiritud(self, info):
        return SanticEspiritud.objects.all()


schema = graphene.Schema(query=ContributorsFromSanticEspiritudQuery, auto_camelcase=False)
