import graphene
from capitania.apps.api.types.provincias import ArtemisaType
from capitania.apps.api.types.infogestiShipement import ClienteType
from capitania.apps.core.models import Artemisa, Cliente


class ContributorsFromArtemisaQuery(graphene.ObjectType):
    contributors_missing_in_onat_artemisa = graphene.List(ArtemisaType)
    contributors_with_different_information_artemisa_plate = graphene.List(ArtemisaType)
    contributors_with_different_information_artemisa_name = graphene.List(ArtemisaType)
    contributors_with_equals_information_artemisa = graphene.List(ArtemisaType)
    artemisa = graphene.List(ArtemisaType)

    # 1 Contribuyentes que estan en capitania vehiculo que no estan en la onat
    def resolve_contributors_missing_in_onat_artemisa(self, info):
        return Artemisa.objects.raw('SELECT DISTINCT reca.* from CORE_ARTEMISA reca left OUTER JOIN cliente@infogesti C ON C.NIT = RECA.NUMEROIDENTIDAD WHERE C.NIT IS NULL order by reca.NUMEROIDENTIDAD')

    # 2 Contribuyentes que estan en ambos capitania con informaciones diferentes
    def resolve_contributors_with_different_information_artemisa_plate(self, info):
        return Artemisa.objects.raw('SELECT DISTINCT reca.* FROM DIRECCION@INFOGESTI DIR INNER JOIN CLIENTE_DIRECCION@INFOGESTI C_DIR ON DIR.ID = C_DIR.ID_DIRECCION INNER JOIN CLIENTE@INFOGESTI C ON C.ID = C_DIR.ID_CLIENTE INNER JOIN CLIENTE_TT@INFOGESTI TT ON TT.ID_CLIENTE = C.ID INNER JOIN CORE_ARTEMISA RECA ON C.NIT = RECA.NUMEROIDENTIDAD WHERE C.UNIDAD BETWEEN 2101 AND 2111 AND TT.MATRICULA <> RECA.CHAPANUEVA')


    def resolve_contributors_with_different_information_artemisa_name(self, info):
        return Artemisa.objects.raw('SELECT DISTINCT reca.* FROM DIRECCION@INFOGESTI DIR INNER JOIN CLIENTE_DIRECCION@INFOGESTI C_DIR ON DIR.ID = C_DIR.ID_DIRECCION INNER JOIN CLIENTE@INFOGESTI C ON C.ID = C_DIR.ID_CLIENTE INNER JOIN CLIENTE_TT@INFOGESTI TT ON TT.ID_CLIENTE = C.ID INNER JOIN CORE_ARTEMISA RECA ON C.NIT = RECA.NUMEROIDENTIDAD WHERE C.UNIDAD BETWEEN 2101 AND 2111 AND UPPER(C.NOMBRE_COMPLETO) <> UPPER(RECA.DATOSPERSONA) AND  upper(substr(C.NOMBRE_COMPLETO, 0, 1)) <> upper(substr(RECA.DATOSPERSONA, 0, 1)) AND  upper(substr(C.NOMBRE_COMPLETO, 2, 1)) <> upper(substr(RECA.DATOSPERSONA, 2, 1)) AND  upper(substr(C.NOMBRE_COMPLETO, 0, 1)) <> upper(substr(RECA.DATOSPERSONA, 2, 1)) AND  upper(substr(C.NOMBRE_COMPLETO, 2, 1)) <> upper(substr(RECA.DATOSPERSONA, 0, 1))')

    # 4 Contribuyentes totalmente coincidentes
    def resolve_contributors_with_equals_information_artemisa(self, info):
        return Artemisa.objects.raw('SELECT DISTINCT reca.* FROM DIRECCION@INFOGESTI DIR INNER JOIN CLIENTE_DIRECCION@INFOGESTI C_DIR ON DIR.ID = C_DIR.ID_DIRECCION INNER JOIN CLIENTE@INFOGESTI C ON C.ID = C_DIR.ID_CLIENTE INNER JOIN CLIENTE_TT@INFOGESTI TT ON TT.ID_CLIENTE = C.ID INNER JOIN CORE_ARTEMISA RECA ON C.NIT = RECA.NUMEROIDENTIDAD WHERE C.UNIDAD BETWEEN 2101 AND 2111 AND UPPER(C.NOMBRE_COMPLETO) = UPPER(RECA.DATOSPERSONA) AND TT.MATRICULA = RECA.CHAPANUEVA')

    def resolve_artemisa(self, info):
        return Artemisa.objects.all()


schema = graphene.Schema(query=ContributorsFromArtemisaQuery, auto_camelcase=False)
