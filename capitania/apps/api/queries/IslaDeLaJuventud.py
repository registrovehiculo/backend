import graphene
from capitania.apps.api.types.provincias import IslaDeLaJuventudType
from capitania.apps.api.types.infogestiShipement import ClienteType
from capitania.apps.core.models import IslaDeLaJuventud, Cliente


class ContributorsFromIslaDeLaJuventudQuery(graphene.ObjectType):
    contributors_missing_in_onat_isla = graphene.List(IslaDeLaJuventudType)
    contributors_with_different_information_isla_plate = graphene.List(IslaDeLaJuventudType)
    contributors_with_different_information_isla_name = graphene.List(IslaDeLaJuventudType)
    contributors_with_equals_information_isla = graphene.List(IslaDeLaJuventudType)
    isla = graphene.List(IslaDeLaJuventudType)

    # 1 Contribuyentes que estan en capitania vehiculo que no estan en la onat
    def resolve_contributors_missing_in_onat_isla(self, info):
        return IslaDeLaJuventud.objects.raw('SELECT DISTINCT RECA.* from CORE_ISLADELAJUVENTUD reca left OUTER JOIN cliente@infogesti C ON C.NIT = RECA.NUMEROIDENTIDAD WHERE C.NIT IS NULL order by reca.NUMEROIDENTIDAD')

    # 2 Contribuyentes que estan en ambos capitania con informaciones diferentes
    def resolve_contributors_with_different_information_isla_plate(self, info):
        return IslaDeLaJuventud.objects.raw('SELECT DISTINCT * FROM DIRECCION@INFOGESTI DIR INNER JOIN CLIENTE_DIRECCION@INFOGESTI C_DIR ON DIR.ID = C_DIR.ID_DIRECCION INNER JOIN CLIENTE@INFOGESTI C ON C.ID = C_DIR.ID_CLIENTE INNER JOIN CLIENTE_TT@INFOGESTI TT ON TT.ID_CLIENTE = C.ID INNER JOIN CORE_ISLADELAJUVENTUD RECA ON C.NIT = RECA.NUMEROIDENTIDAD WHERE C.UNIDAD = 4001 AND TT.MATRICULA <> RECA.CHAPANUEVA')


    def resolve_contributors_with_different_information_isla_name(self, info):
        return IslaDeLaJuventud.objects.raw('SELECT DISTINCT * FROM DIRECCION@INFOGESTI DIR INNER JOIN CLIENTE_DIRECCION@INFOGESTI C_DIR ON DIR.ID = C_DIR.ID_DIRECCION INNER JOIN CLIENTE@INFOGESTI C ON C.ID = C_DIR.ID_CLIENTE INNER JOIN CLIENTE_TT@INFOGESTI TT ON TT.ID_CLIENTE = C.ID INNER JOIN CORE_ISLADELAJUVENTUD RECA ON C.NIT = RECA.NUMEROIDENTIDAD WHERE C.UNIDAD = 4001 AND UPPER(C.NOMBRE_COMPLETO) <> UPPER(RECA.DATOSPERSONA) AND  upper(substr(C.NOMBRE_COMPLETO, 0, 1)) <> upper(substr(RECA.DATOSPERSONA, 0, 1)) AND  upper(substr(C.NOMBRE_COMPLETO, 2, 1)) <> upper(substr(RECA.DATOSPERSONA, 2, 1)) AND  upper(substr(C.NOMBRE_COMPLETO, 0, 1)) <> upper(substr(RECA.DATOSPERSONA, 2, 1)) AND  upper(substr(C.NOMBRE_COMPLETO, 2, 1)) <> upper(substr(RECA.DATOSPERSONA, 0, 1))')

    # 4 Contribuyentes totalmente coincidentes
    def resolve_contributors_with_equals_information_isla(self, info):
        return IslaDeLaJuventud.objects.raw('SELECT DISTINCT * FROM DIRECCION@INFOGESTI DIR INNER JOIN CLIENTE_DIRECCION@INFOGESTI C_DIR ON DIR.ID = C_DIR.ID_DIRECCION INNER JOIN CLIENTE@INFOGESTI C ON C.ID = C_DIR.ID_CLIENTE INNER JOIN CLIENTE_TT@INFOGESTI TT ON TT.ID_CLIENTE = C.ID INNER JOIN CORE_ISLADELAJUVENTUD RECA ON C.NIT = RECA.NUMEROIDENTIDAD WHERE C.UNIDAD = 4001 AND UPPER(C.NOMBRE_COMPLETO) = UPPER(RECA.DATOSPERSONA) AND TT.MATRICULA = RECA.CHAPANUEVA')

    def resolve_isla(self, info):
        return IslaDeLaJuventud.objects.all()


schema = graphene.Schema(query=ContributorsFromIslaDeLaJuventudQuery, auto_camelcase=False)
