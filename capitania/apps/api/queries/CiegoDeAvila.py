import graphene
from capitania.apps.api.types.provincias import CiegoDeAvilaType
from capitania.apps.api.types.infogestiShipement import ClienteType
from capitania.apps.core.models import CiegoDeAvila, Cliente


class ContributorsFromCiegoDeAvilaQuery(graphene.ObjectType):
    contributors_missing_in_onat_ciego = graphene.List(CiegoDeAvilaType)
    contributors_with_different_information_ciego_plate = graphene.List(CiegoDeAvilaType)
    contributors_with_different_information_ciego_name = graphene.List(CiegoDeAvilaType)
    contributors_with_equals_information_ciego = graphene.List(CiegoDeAvilaType)
    ciego = graphene.List(CiegoDeAvilaType)

    # 1 Contribuyentes que estan en capitania vehiculo que no estan en la onat
    def resolve_contributors_missing_in_onat_ciego(self, info):
        return CiegoDeAvila.objects.raw('SELECT DISTINCT RECA.* from CORE_CIEGODEAVILA reca left OUTER JOIN cliente@infogesti C ON C.NIT = RECA.NUMEROIDENTIDAD WHERE C.NIT IS NULL order by reca.NUMEROIDENTIDAD')

    # 2 Contribuyentes que estan en ambos capitania con informaciones diferentes
    def resolve_contributors_with_different_information_ciego_plate(self, info):
        return CiegoDeAvila.objects.raw('SELECT DISTINCT  FROM DIRECCION@INFOGESTI DIR INNER JOIN CLIENTE_DIRECCION@INFOGESTI C_DIR ON DIR.ID = C_DIR.ID_DIRECCION INNER JOIN CLIENTE@INFOGESTI C ON C.ID = C_DIR.ID_CLIENTE INNER JOIN CLIENTE_TT@INFOGESTI TT ON TT.ID_CLIENTE = C.ID INNER JOIN CORE_CIEGODEAVILA RECA ON C.NIT = RECA.NUMEROIDENTIDAD WHERE C.UNIDAD BETWEEN 2901 AND 2910 AND TT.MATRICULA <> RECA.CHAPANUEVA')


    def resolve_contributors_with_different_information_ciego_name(self, info):
        return CiegoDeAvila.objects.raw('SELECT DISTINCT * FROM DIRECCION@INFOGESTI DIR INNER JOIN CLIENTE_DIRECCION@INFOGESTI C_DIR ON DIR.ID = C_DIR.ID_DIRECCION INNER JOIN CLIENTE@INFOGESTI C ON C.ID = C_DIR.ID_CLIENTE INNER JOIN CLIENTE_TT@INFOGESTI TT ON TT.ID_CLIENTE = C.ID INNER JOIN CORE_CIEGODEAVILA RECA ON C.NIT = RECA.NUMEROIDENTIDAD WHERE C.UNIDAD BETWEEN 2901 AND 2910 AND UPPER(C.NOMBRE_COMPLETO) <> UPPER(RECA.DATOSPERSONA) AND  upper(substr(C.NOMBRE_COMPLETO, 0, 1)) <> upper(substr(RECA.DATOSPERSONA, 0, 1)) AND  upper(substr(C.NOMBRE_COMPLETO, 2, 1)) <> upper(substr(RECA.DATOSPERSONA, 2, 1)) AND  upper(substr(C.NOMBRE_COMPLETO, 0, 1)) <> upper(substr(RECA.DATOSPERSONA, 2, 1)) AND  upper(substr(C.NOMBRE_COMPLETO, 2, 1)) <> upper(substr(RECA.DATOSPERSONA, 0, 1))')

    # 4 Contribuyentes totalmente coincidentes
    def resolve_contributors_with_equals_information_ciego(self, info):
        return CiegoDeAvila.objects.raw('SELECT DISTINCT * FROM DIRECCION@INFOGESTI DIR INNER JOIN CLIENTE_DIRECCION@INFOGESTI C_DIR ON DIR.ID = C_DIR.ID_DIRECCION INNER JOIN CLIENTE@INFOGESTI C ON C.ID = C_DIR.ID_CLIENTE INNER JOIN CLIENTE_TT@INFOGESTI TT ON TT.ID_CLIENTE = C.ID INNER JOIN CORE_CIEGODEAVILA RECA ON C.NIT = RECA.NUMEROIDENTIDAD WHERE C.UNIDAD BETWEEN 2901 AND 2910 AND UPPER(C.NOMBRE_COMPLETO) = UPPER(RECA.DATOSPERSONA) AND TT.MATRICULA = RECA.CHAPANUEVA')

    def resolve_ciego(self, info):
        return CiegoDeAvila.objects.all()


schema = graphene.Schema(query=ContributorsFromCiegoDeAvilaQuery, auto_camelcase=False)
