import graphene
from django.db.models import Q
from django.db.models.functions import Length

from capitania.apps.api.types.provincias import LasTunasType
from capitania.apps.api.types.infogestiShipement import ClienteType
from capitania.apps.core.models import LasTunas, Cliente


class ContributorsFromLasTunasQuery(graphene.ObjectType):
    contributors_missing_in_onat_las_tunas = graphene.List(LasTunasType)
    contributors_with_different_information_las_tunas_plate = graphene.List(LasTunasType)
    contributors_with_different_information_las_tunas_name = graphene.List(LasTunasType)
    contributors_with_equals_information_las_tunas = graphene.List(LasTunasType)
    tunas_name_infogesti = graphene.List(ClienteType)
    wrong_id_las_tunas = graphene.List(LasTunasType)
    las_tunas = graphene.List(LasTunasType)

    # 1 Contribuyentes que estan en capitania vehiculo que no estan en la onat
    def resolve_contributors_missing_in_onat_las_tunas(self, info):
        return LasTunas.objects.raw('select distinct reca.* from CORE_LASTUNAS reca left outer join cliente@infogesti c on reca.NUMEROIDENTIDAD = c.nit left outer join cliente_tt@infogesti tt on tt.id_cliente =c.id where tt.id_cliente is null')

    # 2 Contribuyentes que estan en ambos capitania con informaciones diferentes
    def resolve_contributors_with_different_information_las_tunas_plate(self, info):
        return LasTunas.objects.raw('SELECT DISTINCT RECA.* FROM DIRECCION@INFOGESTI DIR INNER JOIN CLIENTE_DIRECCION@INFOGESTI C_DIR ON DIR.ID = C_DIR.ID_DIRECCION INNER JOIN CLIENTE@INFOGESTI C ON C.ID = C_DIR.ID_CLIENTE INNER JOIN CLIENTE_TT@INFOGESTI TT ON TT.ID_CLIENTE = C.ID INNER JOIN CORE_LASTUNAS RECA ON C.NIT = RECA.NUMEROIDENTIDAD WHERE C.UNIDAD BETWEEN 3101 AND 3108 AND TT.MATRICULA <> RECA.CHAPANUEVA')


    def resolve_contributors_with_different_information_las_tunas_name(self, info):
        return LasTunas.objects.raw('SELECT RECA.* FROM DIRECCION@INFOGESTI DIR INNER JOIN CLIENTE_DIRECCION@INFOGESTI C_DIR ON DIR.ID = C_DIR.ID_DIRECCION INNER JOIN CLIENTE@INFOGESTI C ON C.ID = C_DIR.ID_CLIENTE INNER JOIN CLIENTE_TT@INFOGESTI TT ON TT.ID_CLIENTE = C.ID INNER JOIN CORE_LASTUNAS RECA ON C.NIT = RECA.NUMEROIDENTIDAD WHERE C.UNIDAD BETWEEN 3101 AND 3108 AND UPPER(C.NOMBRE_COMPLETO) <> UPPER(RECA.DATOSPERSONA) AND  upper(substr(C.NOMBRE_COMPLETO, 0, 1)) <> upper(substr(RECA.DATOSPERSONA, 0, 1)) AND  upper(substr(C.NOMBRE_COMPLETO, 2, 1)) <> upper(substr(RECA.DATOSPERSONA, 2, 1)) AND  upper(substr(C.NOMBRE_COMPLETO, 0, 1)) <> upper(substr(RECA.DATOSPERSONA, 2, 1)) AND  upper(substr(C.NOMBRE_COMPLETO, 2, 1)) <> upper(substr(RECA.DATOSPERSONA, 0, 1)) order by RECA.NUMEROIDENTIDAD')

    def resolve_tunas_name_infogesti(self, info):
        return Cliente.objects.raw('SELECT C.NOMBRE_COMPLETO, C.id, c.nit FROM DIRECCION@INFOGESTI DIR INNER JOIN CLIENTE_DIRECCION@INFOGESTI C_DIR ON DIR.ID = C_DIR.ID_DIRECCION INNER JOIN CLIENTE@INFOGESTI C ON C.ID = C_DIR.ID_CLIENTE INNER JOIN CLIENTE_TT@INFOGESTI TT ON TT.ID_CLIENTE = C.ID INNER JOIN CORE_LASTUNAS RECA ON C.NIT = RECA.NUMEROIDENTIDAD WHERE C.UNIDAD BETWEEN 3101 AND 3108 AND UPPER(C.NOMBRE_COMPLETO) <> UPPER(RECA.DATOSPERSONA) AND  upper(substr(C.NOMBRE_COMPLETO, 0, 1)) <> upper(substr(RECA.DATOSPERSONA, 0, 1)) AND  upper(substr(C.NOMBRE_COMPLETO, 2, 1)) <> upper(substr(RECA.DATOSPERSONA, 2, 1)) AND  upper(substr(C.NOMBRE_COMPLETO, 0, 1)) <> upper(substr(RECA.DATOSPERSONA, 2, 1)) AND  upper(substr(C.NOMBRE_COMPLETO, 2, 1)) <> upper(substr(RECA.DATOSPERSONA, 0, 1)) order by C.nit')

    # 4 Contribuyentes totalmente coincidentes
    def resolve_contributors_with_equals_information_las_tunas(self, info):
        return LasTunas.objects.raw('SELECT DISTINCT RECA.* FROM DIRECCION@INFOGESTI DIR INNER JOIN CLIENTE_DIRECCION@INFOGESTI C_DIR ON DIR.ID = C_DIR.ID_DIRECCION INNER JOIN CLIENTE@INFOGESTI C ON C.ID = C_DIR.ID_CLIENTE INNER JOIN CLIENTE_TT@INFOGESTI TT ON TT.ID_CLIENTE = C.ID INNER JOIN CORE_LASTUNAS RECA ON C.NIT = RECA.NUMEROIDENTIDAD WHERE C.UNIDAD BETWEEN 3101 AND 3108 AND UPPER(C.NOMBRE_COMPLETO) = UPPER(RECA.DATOSPERSONA) AND TT.MATRICULA = RECA.CHAPANUEVA')

    def resolve_wrong_id_las_tunas(self, info):
        return LasTunas.objects.annotate(numeroidentidad_len=Length('numeroidentidad')).filter(Q(
            numeroidentidad_len__lt=5) | Q(numeroidentidad__isnull=True) | Q(datospersona__isnull=True))

    def resolve_las_tunas(self, info):
        return LasTunas.objects.all()


schema = graphene.Schema(query=ContributorsFromLasTunasQuery, auto_camelcase=False)
