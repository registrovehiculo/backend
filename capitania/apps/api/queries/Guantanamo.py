import graphene
from capitania.apps.api.types.provincias import GuantanamoType
from capitania.apps.api.types.infogestiShipement import ClienteType
from capitania.apps.core.models import Guantanamo, Cliente


class ContributorsFromGuantanamoQuery(graphene.ObjectType):
    contributors_missing_in_onat_guantanamo = graphene.List(GuantanamoType)
    contributors_with_different_information_guantanamo_plate = graphene.List(GuantanamoType)
    contributors_with_different_information_guantanamo_name = graphene.List(GuantanamoType)
    contributors_with_equals_information_guantanamo = graphene.List(GuantanamoType)
    guantanamo_name_infogesti = graphene.List(ClienteType)
    guantanamo = graphene.List(GuantanamoType)

    # 1 Contribuyentes que estan en capitania vehiculo que no estan en la onat
    def resolve_contributors_missing_in_onat_guantanamo(self, info):
        return Guantanamo.objects.raw('SELECT DISTINCT RECA.* from CORE_GUANTANAMO reca left OUTER JOIN cliente@infogesti C ON C.NIT = RECA.NUMEROIDENTIDAD WHERE C.NIT IS NULL order by reca.NUMEROIDENTIDAD')

    # 2 Contribuyentes que estan en ambos capitania con informaciones diferentes
    def resolve_contributors_with_different_information_guantanamo_plate(self, info):
        return Guantanamo.objects.raw('SELECT DISTINCT RECA.* FROM DIRECCION@INFOGESTI DIR INNER JOIN CLIENTE_DIRECCION@INFOGESTI C_DIR ON DIR.ID = C_DIR.ID_DIRECCION INNER JOIN CLIENTE@INFOGESTI C ON C.ID = C_DIR.ID_CLIENTE INNER JOIN CLIENTE_TT@INFOGESTI TT ON TT.ID_CLIENTE = C.ID INNER JOIN CORE_GUANTANAMO RECA ON C.NIT = RECA.NUMEROIDENTIDAD WHERE C.UNIDAD BETWEEN 3501 AND 3510 AND TT.MATRICULA <> RECA.CHAPANUEVA')


    def resolve_contributors_with_different_information_guantanamo_name(self, info):
        return Guantanamo.objects.raw('SELECT RECA.* FROM DIRECCION@INFOGESTI DIR INNER JOIN CLIENTE_DIRECCION@INFOGESTI C_DIR ON DIR.ID = C_DIR.ID_DIRECCION INNER JOIN CLIENTE@INFOGESTI C ON C.ID = C_DIR.ID_CLIENTE INNER JOIN CLIENTE_TT@INFOGESTI TT ON TT.ID_CLIENTE = C.ID INNER JOIN CORE_GUANTANAMO RECA ON C.NIT = RECA.NUMEROIDENTIDAD WHERE C.UNIDAD BETWEEN 3501 AND 3510 AND UPPER(C.NOMBRE_COMPLETO) <> UPPER(RECA.DATOSPERSONA) AND  upper(substr(C.NOMBRE_COMPLETO, 0, 1)) <> upper(substr(RECA.DATOSPERSONA, 0, 1)) AND  upper(substr(C.NOMBRE_COMPLETO, 2, 1)) <> upper(substr(RECA.DATOSPERSONA, 2, 1)) AND  upper(substr(C.NOMBRE_COMPLETO, 0, 1)) <> upper(substr(RECA.DATOSPERSONA, 2, 1)) AND  upper(substr(C.NOMBRE_COMPLETO, 2, 1)) <> upper(substr(RECA.DATOSPERSONA, 0, 1)) order by RECA.NUMEROIDENTIDAD')

    def resolve_guantanamo_name_infogesti(self, info):
        return Cliente.objects.raw(
            'SELECT C.NOMBRE_COMPLETO, C.id, c.nit FROM DIRECCION@INFOGESTI DIR INNER JOIN CLIENTE_DIRECCION@INFOGESTI C_DIR ON DIR.ID = C_DIR.ID_DIRECCION INNER JOIN CLIENTE@INFOGESTI C ON C.ID = C_DIR.ID_CLIENTE INNER JOIN CLIENTE_TT@INFOGESTI TT ON TT.ID_CLIENTE = C.ID INNER JOIN CORE_GUANTANAMO RECA ON C.NIT = RECA.NUMEROIDENTIDAD WHERE C.UNIDAD BETWEEN 3501 AND 3510 AND UPPER(C.NOMBRE_COMPLETO) <> UPPER(RECA.DATOSPERSONA) AND  upper(substr(C.NOMBRE_COMPLETO, 0, 1)) <> upper(substr(RECA.DATOSPERSONA, 0, 1)) AND  upper(substr(C.NOMBRE_COMPLETO, 2, 1)) <> upper(substr(RECA.DATOSPERSONA, 2, 1)) AND  upper(substr(C.NOMBRE_COMPLETO, 0, 1)) <> upper(substr(RECA.DATOSPERSONA, 2, 1)) AND  upper(substr(C.NOMBRE_COMPLETO, 2, 1)) <> upper(substr(RECA.DATOSPERSONA, 0, 1)) order by C.nit')

    # 4 Contribuyentes totalmente coincidentes
    def resolve_contributors_with_equals_information_guantanamo(self, info):
        return Guantanamo.objects.raw('SELECT DISTINCT RECA.* FROM DIRECCION@INFOGESTI DIR INNER JOIN CLIENTE_DIRECCION@INFOGESTI C_DIR ON DIR.ID = C_DIR.ID_DIRECCION INNER JOIN CLIENTE@INFOGESTI C ON C.ID = C_DIR.ID_CLIENTE INNER JOIN CLIENTE_TT@INFOGESTI TT ON TT.ID_CLIENTE = C.ID INNER JOIN CORE_GUANTANAMO RECA ON C.NIT = RECA.NUMEROIDENTIDAD WHERE C.UNIDAD BETWEEN 3501 AND 3510 AND UPPER(C.NOMBRE_COMPLETO) = UPPER(RECA.DATOSPERSONA) AND TT.MATRICULA = RECA.CHAPANUEVA')

    def resolve_guantanamo(self, info):
        return Guantanamo.objects.all()


schema = graphene.Schema(query=ContributorsFromGuantanamoQuery, auto_camelcase=False)
