import graphene
from capitania.apps.api.types.provincias import GranmaType
from capitania.apps.api.types.infogestiShipement import ClienteType
from capitania.apps.core.models import Granma, Cliente


class ContributorsFromGranmaQuery(graphene.ObjectType):
    contributors_missing_in_onat_granma = graphene.List(GranmaType)
    contributors_with_different_information_granma_plate = graphene.List(ClienteType)
    contributors_with_different_information_granma_name = graphene.List(ClienteType)
    contributors_with_equals_information_granma = graphene.List(ClienteType)
    granma = graphene.List(GranmaType)

    # 1 Contribuyentes que estan en capitania vehiculo que no estan en la onat
    def resolve_contributors_missing_in_onat_granma(self, info):
        return Granma.objects.raw('SELECT DISTINCT RECA.* FROM DIRECCION@INFOGESTI DIR INNER JOIN CLIENTE_DIRECCION@INFOGESTI C_DIR ON DIR.ID = C_DIR.ID_DIRECCION INNER JOIN CLIENTE@INFOGESTI C ON C.ID = C_DIR.ID_CLIENTE INNER JOIN CLIENTE_TT@INFOGESTI TT ON TT.ID_CLIENTE = C.ID RIGHT OUTER JOIN CORE_GRANMA RECA ON C.NIT = RECA.NUMEROIDENTIDAD WHERE C.NIT IS NULL')

    # 2 Contribuyentes que estan en ambos capitania con informaciones diferentes
    def resolve_contributors_with_different_information_granma_plate(self, info):
        return Cliente.objects.raw('SELECT DISTINCT C.ID,  C.NIT, C.NOMBRE_COMPLETO, TT.MATRICULA, DIR.DIRECCION FROM DIRECCION@INFOGESTI DIR INNER JOIN CLIENTE_DIRECCION@INFOGESTI C_DIR ON DIR.ID = C_DIR.ID_DIRECCION INNER JOIN CLIENTE@INFOGESTI C ON C.ID = C_DIR.ID_CLIENTE INNER JOIN CLIENTE_TT@INFOGESTI TT ON TT.ID_CLIENTE = C.ID INNER JOIN CORE_GRANMA RECA ON C.NIT = RECA.NUMEROIDENTIDAD WHERE C.UNIDAD BETWEEN 3301 AND 3313 AND TT.MATRICULA <> RECA.CHAPANUEVA')


    def resolve_contributors_with_different_information_granma_name(self, info):
        return Cliente.objects.raw('SELECT DISTINCT C.ID,  C.NIT, C.NOMBRE_COMPLETO, TT.MATRICULA, DIR.DIRECCION FROM DIRECCION@INFOGESTI DIR INNER JOIN CLIENTE_DIRECCION@INFOGESTI C_DIR ON DIR.ID = C_DIR.ID_DIRECCION INNER JOIN CLIENTE@INFOGESTI C ON C.ID = C_DIR.ID_CLIENTE INNER JOIN CLIENTE_TT@INFOGESTI TT ON TT.ID_CLIENTE = C.ID INNER JOIN CORE_GRANMA RECA ON C.NIT = RECA.NUMEROIDENTIDAD WHERE C.UNIDAD BETWEEN 3301 AND 3313 AND UPPER(C.NOMBRE_COMPLETO) <> UPPER(RECA.DATOSPERSONA)')

    # 4 Contribuyentes totalmente coincidentes
    def resolve_contributors_with_equals_information_granma(self, info):
        return Cliente.objects.raw('SELECT DISTINCT C.ID,  C.NIT, C.NOMBRE_COMPLETO, TT.MATRICULA, DIR.DIRECCION FROM DIRECCION@INFOGESTI DIR INNER JOIN CLIENTE_DIRECCION@INFOGESTI C_DIR ON DIR.ID = C_DIR.ID_DIRECCION INNER JOIN CLIENTE@INFOGESTI C ON C.ID = C_DIR.ID_CLIENTE INNER JOIN CLIENTE_TT@INFOGESTI TT ON TT.ID_CLIENTE = C.ID INNER JOIN CORE_GRANMA RECA ON C.NIT = RECA.NUMEROIDENTIDAD WHERE C.UNIDAD BETWEEN 3301 AND 3313 AND UPPER(C.NOMBRE_COMPLETO) = UPPER(RECA.DATOSPERSONA) AND TT.MATRICULA = RECA.CHAPANUEVA')

    def resolve_granma(self, info):
        return Granma.objects.all()


schema = graphene.Schema(query=ContributorsFromGranmaQuery, auto_camelcase=False)
