import graphene
from django.db.models import Q
from django.db.models.functions import Length

from capitania.apps.api.types.provincias import CienfuegosType
from capitania.apps.api.types.infogestiShipement import ClienteType
from capitania.apps.core.models import Cienfuegos, Cliente


class ContributorsFromCienfuegosQuery(graphene.ObjectType):
    contributors_missing_in_onat_cienfuegos = graphene.List(CienfuegosType)
    contributors_with_different_information_cienfuegos_plate = graphene.List(CienfuegosType)
    contributors_with_different_information_cienfuegos_name = graphene.List(CienfuegosType)
    contributors_with_equals_information_cienfuegos = graphene.List(CienfuegosType)
    cienfuegos_name_infogesti = graphene.List(ClienteType)
    wrong_id_cienfuegos = graphene.List(CienfuegosType)
    cienfuegos = graphene.List(CienfuegosType)

    # 1 Contribuyentes que estan en capitania vehiculo que no estan en la onat
    def resolve_contributors_missing_in_onat_cienfuegos(self, info):
        return Cienfuegos.objects.raw('select distinct reca.* from CORE_CIENFUEGOS reca left outer join cliente@infogesti c on reca.NUMEROIDENTIDAD = c.nit left outer join cliente_tt@infogesti tt on tt.id_cliente =c.id where tt.id_cliente is null')

    # 2 Contribuyentes que estan en ambos capitania con informaciones diferentes
    def resolve_contributors_with_different_information_cienfuegos_plate(self, info):
        return Cienfuegos.objects.raw('SELECT DISTINCT RECA.* FROM DIRECCION@INFOGESTI DIR INNER JOIN CLIENTE_DIRECCION@INFOGESTI C_DIR ON DIR.ID = C_DIR.ID_DIRECCION INNER JOIN CLIENTE@INFOGESTI C ON C.ID = C_DIR.ID_CLIENTE INNER JOIN CLIENTE_TT@INFOGESTI TT ON TT.ID_CLIENTE = C.ID INNER JOIN CORE_CIENFUEGOS RECA ON C.NIT = RECA.NUMEROIDENTIDAD WHERE C.UNIDAD BETWEEN 2701 AND 2708 AND TT.MATRICULA <> RECA.CHAPANUEVA')


    def resolve_contributors_with_different_information_cienfuegos_name(self, info):
        return Cienfuegos.objects.raw('SELECT RECA.* FROM DIRECCION@INFOGESTI DIR INNER JOIN CLIENTE_DIRECCION@INFOGESTI C_DIR ON DIR.ID = C_DIR.ID_DIRECCION INNER JOIN CLIENTE@INFOGESTI C ON C.ID = C_DIR.ID_CLIENTE INNER JOIN CLIENTE_TT@INFOGESTI TT ON TT.ID_CLIENTE = C.ID INNER JOIN CORE_CIENFUEGOS RECA ON C.NIT = RECA.NUMEROIDENTIDAD WHERE C.UNIDAD BETWEEN 2701 AND 2708 AND UPPER(C.NOMBRE_COMPLETO) <> UPPER(RECA.DATOSPERSONA) AND  upper(substr(C.NOMBRE_COMPLETO, 0, 1)) <> upper(substr(RECA.DATOSPERSONA, 0, 1)) AND  upper(substr(C.NOMBRE_COMPLETO, 2, 1)) <> upper(substr(RECA.DATOSPERSONA, 2, 1)) AND  upper(substr(C.NOMBRE_COMPLETO, 0, 1)) <> upper(substr(RECA.DATOSPERSONA, 2, 1)) AND  upper(substr(C.NOMBRE_COMPLETO, 2, 1)) <> upper(substr(RECA.DATOSPERSONA, 0, 1)) order by RECA.NUMEROIDENTIDAD')

    def resolve_cienfuegos_name_infogesti(self, info):
        return Cliente.objects.raw(
            'SELECT C.NOMBRE_COMPLETO, C.id, c.nit FROM DIRECCION@INFOGESTI DIR INNER JOIN CLIENTE_DIRECCION@INFOGESTI C_DIR ON DIR.ID = C_DIR.ID_DIRECCION INNER JOIN CLIENTE@INFOGESTI C ON C.ID = C_DIR.ID_CLIENTE INNER JOIN CLIENTE_TT@INFOGESTI TT ON TT.ID_CLIENTE = C.ID INNER JOIN CORE_CIENFUEGOS RECA ON C.NIT = RECA.NUMEROIDENTIDAD WHERE C.UNIDAD BETWEEN 2701 AND 2708 AND UPPER(C.NOMBRE_COMPLETO) <> UPPER(RECA.DATOSPERSONA) AND  upper(substr(C.NOMBRE_COMPLETO, 0, 1)) <> upper(substr(RECA.DATOSPERSONA, 0, 1)) AND  upper(substr(C.NOMBRE_COMPLETO, 2, 1)) <> upper(substr(RECA.DATOSPERSONA, 2, 1)) AND  upper(substr(C.NOMBRE_COMPLETO, 0, 1)) <> upper(substr(RECA.DATOSPERSONA, 2, 1)) AND  upper(substr(C.NOMBRE_COMPLETO, 2, 1)) <> upper(substr(RECA.DATOSPERSONA, 0, 1)) order by C.nit')

    # 4 Contribuyentes totalmente coincidentes
    def resolve_contributors_with_equals_information_cienfuegos(self, info):
        return Cienfuegos.objects.raw('SELECT DISTINCT RECA.* FROM DIRECCION@INFOGESTI DIR INNER JOIN CLIENTE_DIRECCION@INFOGESTI C_DIR ON DIR.ID = C_DIR.ID_DIRECCION INNER JOIN CLIENTE@INFOGESTI C ON C.ID = C_DIR.ID_CLIENTE INNER JOIN CLIENTE_TT@INFOGESTI TT ON TT.ID_CLIENTE = C.ID INNER JOIN CORE_CIENFUEGOS RECA ON C.NIT = RECA.NUMEROIDENTIDAD WHERE C.UNIDAD BETWEEN 2701 AND 2708 AND UPPER(C.NOMBRE_COMPLETO) = UPPER(RECA.DATOSPERSONA) AND TT.MATRICULA = RECA.CHAPANUEVA')

    def resolve_wrong_id_cienfuegos(self, info):
        return Cienfuegos.objects.annotate(numeroidentidad_len=Length('numeroidentidad')).filter(Q(
            numeroidentidad_len__lt=5) | Q(numeroidentidad__isnull=True) | Q(datospersona__isnull=True))

    def resolve_cienfuegos(self, info):
        return Cienfuegos.objects.all()


schema = graphene.Schema(query=ContributorsFromCienfuegosQuery, auto_camelcase=False)
