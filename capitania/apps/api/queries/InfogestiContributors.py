import graphene
from capitania.apps.api.types.infogestiShipement import ClienteType
from capitania.apps.core.models import Cliente


class ContributorsFromInfogestiQuery(graphene.ObjectType):
    infogesti_artemisa = graphene.List(ClienteType)
    infogesti_camaguey = graphene.List(ClienteType)
    infogesti_ciego = graphene.List(ClienteType)
    infogesti_cienfuegos = graphene.List(ClienteType)
    infogesti_granma = graphene.List(ClienteType)
    infogesti_guantanamo = graphene.List(ClienteType)
    infogesti_holguin = graphene.List(ClienteType)
    infogesti_isla = graphene.List(ClienteType)
    infogesti_tunas = graphene.List(ClienteType)
    infogesti_matanzas = graphene.List(ClienteType)
    infogesti_mayabeque = graphene.List(ClienteType)
    infogesti_pinar = graphene.List(ClienteType)
    infogesti_santiago = graphene.List(ClienteType)
    infogesti_espiritud = graphene.List(ClienteType)
    infogesti_villa = graphene.List(ClienteType)
    infogesti_habana = graphene.List(ClienteType)

    def resolve_infogesti_artemisa(self, info):
        return Cliente.objects.raw('SELECT DISTINCT C.ID, C.NIT, C.NOMBRE_COMPLETO, C.DPA, TT.MATRICULA, DIR.DIRECCION FROM DIRECCION@INFOGESTI DIR INNER JOIN CLIENTE_DIRECCION@INFOGESTI C_DIR ON DIR.ID = C_DIR.ID_DIRECCION INNER JOIN CLIENTE@INFOGESTI C ON C.ID = C_DIR.ID_CLIENTE INNER JOIN CLIENTE_TT@INFOGESTI TT ON TT.ID_CLIENTE = C.ID LEFT OUTER JOIN CORE_ARTEMISA RECA ON C.NIT = RECA.NUMEROIDENTIDAD WHERE RECA.NUMEROIDENTIDAD IS NULL AND C.UNIDAD BETWEEN 2201 AND 2211')

    def resolve_infogesti_habana(self, info):
        return Cliente.objects.raw('SELECT DISTINCT C.ID, C.NIT, C.NOMBRE_COMPLETO, C.DPA, TT.MATRICULA, DIR.DIRECCION FROM DIRECCION@INFOGESTI DIR INNER JOIN CLIENTE_DIRECCION@INFOGESTI C_DIR ON DIR.ID = C_DIR.ID_DIRECCION INNER JOIN CLIENTE@INFOGESTI C ON C.ID = C_DIR.ID_CLIENTE INNER JOIN CLIENTE_TT@INFOGESTI TT ON TT.ID_CLIENTE = C.ID LEFT OUTER JOIN CORE_LAHABANA RECA ON C.NIT = RECA.NUMEROIDENTIDAD WHERE RECA.NUMEROIDENTIDAD IS NULL AND C.UNIDAD BETWEEN 2301 AND 2315')

    def resolve_infogesti_camaguey(self, info):
        return Cliente.objects.raw('SELECT DISTINCT C.ID, C.NIT, C.NOMBRE_COMPLETO, C.DPA, TT.MATRICULA, DIR.DIRECCION FROM DIRECCION@INFOGESTI DIR INNER JOIN CLIENTE_DIRECCION@INFOGESTI C_DIR ON DIR.ID = C_DIR.ID_DIRECCION INNER JOIN CLIENTE@INFOGESTI C ON C.ID = C_DIR.ID_CLIENTE INNER JOIN CLIENTE_TT@INFOGESTI TT ON TT.ID_CLIENTE = C.ID LEFT OUTER JOIN CORE_CAMAGUEY RECA ON C.NIT = RECA.NUMEROIDENTIDAD WHERE RECA.NUMEROIDENTIDAD IS NULL AND C.UNIDAD BETWEEN 3001 AND 3008')

    def resolve_infogesti_ciego(self, info):
        return Cliente.objects.raw('SELECT DISTINCT C.ID, C.NIT, C.NOMBRE_COMPLETO, C.DPA, TT.MATRICULA, DIR.DIRECCION FROM DIRECCION@INFOGESTI DIR INNER JOIN CLIENTE_DIRECCION@INFOGESTI C_DIR ON DIR.ID = C_DIR.ID_DIRECCION INNER JOIN CLIENTE@INFOGESTI C ON C.ID = C_DIR.ID_CLIENTE INNER JOIN CLIENTE_TT@INFOGESTI TT ON TT.ID_CLIENTE = C.ID LEFT OUTER JOIN CORE_CIEGODEAVILA RECA ON C.NIT = RECA.NUMEROIDENTIDAD WHERE RECA.NUMEROIDENTIDAD IS NULL AND C.UNIDAD BETWEEN 2901 AND 2910')

    def resolve_infogesti_cienfuegos(self, info):
        return Cliente.objects.raw('SELECT DISTINCT C.ID, C.NIT, C.NOMBRE_COMPLETO, C.DPA, TT.MATRICULA, DIR.DIRECCION FROM DIRECCION@INFOGESTI DIR INNER JOIN CLIENTE_DIRECCION@INFOGESTI C_DIR ON DIR.ID = C_DIR.ID_DIRECCION INNER JOIN CLIENTE@INFOGESTI C ON C.ID = C_DIR.ID_CLIENTE INNER JOIN CLIENTE_TT@INFOGESTI TT ON TT.ID_CLIENTE = C.ID LEFT OUTER JOIN CORE_CIENFUEGOS RECA ON C.NIT = RECA.NUMEROIDENTIDAD WHERE RECA.NUMEROIDENTIDAD IS NULL AND C.UNIDAD BETWEEN 2701 AND 2708')

    def resolve_infogesti_granma(self, info):
        return Cliente.objects.raw('SELECT DISTINCT C.ID, C.NIT, C.NOMBRE_COMPLETO, C.DPA, TT.MATRICULA, DIR.DIRECCION FROM DIRECCION@INFOGESTI DIR INNER JOIN CLIENTE_DIRECCION@INFOGESTI C_DIR ON DIR.ID = C_DIR.ID_DIRECCION INNER JOIN CLIENTE@INFOGESTI C ON C.ID = C_DIR.ID_CLIENTE INNER JOIN CLIENTE_TT@INFOGESTI TT ON TT.ID_CLIENTE = C.ID LEFT OUTER JOIN CORE_GRANMA RECA ON C.NIT = RECA.NUMEROIDENTIDAD WHERE RECA.NUMEROIDENTIDAD IS NULL AND C.UNIDAD BETWEEN 3301 AND 3313')

    def resolve_infogesti_isla(self, info):
        return Cliente.objects.raw('SELECT DISTINCT C.ID, C.NIT, C.NOMBRE_COMPLETO, C.DPA, TT.MATRICULA, DIR.DIRECCION FROM DIRECCION@INFOGESTI DIR INNER JOIN CLIENTE_DIRECCION@INFOGESTI C_DIR ON DIR.ID = C_DIR.ID_DIRECCION INNER JOIN CLIENTE@INFOGESTI C ON C.ID = C_DIR.ID_CLIENTE INNER JOIN CLIENTE_TT@INFOGESTI TT ON TT.ID_CLIENTE = C.ID LEFT OUTER JOIN CORE_ISLADELAJUVENTUD RECA ON C.NIT = RECA.NUMEROIDENTIDAD WHERE RECA.NUMEROIDENTIDAD IS NULL AND C.UNIDAD = 4001')

    def resolve_infogesti_tunas(self, info):
        return Cliente.objects.raw('SELECT DISTINCT C.ID, C.NIT, C.NOMBRE_COMPLETO, C.DPA, TT.MATRICULA, DIR.DIRECCION FROM DIRECCION@INFOGESTI DIR INNER JOIN CLIENTE_DIRECCION@INFOGESTI C_DIR ON DIR.ID = C_DIR.ID_DIRECCION INNER JOIN CLIENTE@INFOGESTI C ON C.ID = C_DIR.ID_CLIENTE INNER JOIN CLIENTE_TT@INFOGESTI TT ON TT.ID_CLIENTE = C.ID LEFT OUTER JOIN CORE_LASTUNAS RECA ON C.NIT = RECA.NUMEROIDENTIDAD WHERE RECA.NUMEROIDENTIDAD IS NULL AND C.UNIDAD BETWEEN 3101 AND 3108')

    def resolve_infogesti_matanzas(self, info):
        return Cliente.objects.raw('SELECT DISTINCT C.ID, C.NIT, C.NOMBRE_COMPLETO, C.DPA, TT.MATRICULA, DIR.DIRECCION FROM DIRECCION@INFOGESTI DIR INNER JOIN CLIENTE_DIRECCION@INFOGESTI C_DIR ON DIR.ID = C_DIR.ID_DIRECCION INNER JOIN CLIENTE@INFOGESTI C ON C.ID = C_DIR.ID_CLIENTE INNER JOIN CLIENTE_TT@INFOGESTI TT ON TT.ID_CLIENTE = C.ID LEFT OUTER JOIN CORE_MATANZAS RECA ON C.NIT = RECA.NUMEROIDENTIDAD WHERE RECA.NUMEROIDENTIDAD IS NULL AND C.UNIDAD BETWEEN 2501 AND 2513')

    def resolve_infogesti_mayabeque(self, info):
        return Cliente.objects.raw('SELECT DISTINCT C.ID, C.NIT, C.NOMBRE_COMPLETO, C.DPA, TT.MATRICULA, DIR.DIRECCION FROM DIRECCION@INFOGESTI DIR INNER JOIN CLIENTE_DIRECCION@INFOGESTI C_DIR ON DIR.ID = C_DIR.ID_DIRECCION INNER JOIN CLIENTE@INFOGESTI C ON C.ID = C_DIR.ID_CLIENTE INNER JOIN CLIENTE_TT@INFOGESTI TT ON TT.ID_CLIENTE = C.ID LEFT OUTER JOIN CORE_MAYABEQUE RECA ON C.NIT = RECA.NUMEROIDENTIDAD WHERE RECA.NUMEROIDENTIDAD IS NULL AND C.UNIDAD BETWEEN 2401 AND 2411')

    def resolve_infogesti_pinar(self, info):
        return Cliente.objects.raw('SELECT DISTINCT C.ID, C.NIT, C.NOMBRE_COMPLETO, C.DPA, TT.MATRICULA, DIR.DIRECCION FROM DIRECCION@INFOGESTI DIR INNER JOIN CLIENTE_DIRECCION@INFOGESTI C_DIR ON DIR.ID = C_DIR.ID_DIRECCION INNER JOIN CLIENTE@INFOGESTI C ON C.ID = C_DIR.ID_CLIENTE INNER JOIN CLIENTE_TT@INFOGESTI TT ON TT.ID_CLIENTE = C.ID LEFT OUTER JOIN CORE_PINARDELRIO RECA ON C.NIT = RECA.NUMEROIDENTIDAD WHERE RECA.NUMEROIDENTIDAD IS NULL AND C.UNIDAD BETWEEN 2101 AND 2111')

    def resolve_infogesti_santiago(self, info):
        return Cliente.objects.raw('SELECT DISTINCT C.ID, C.NIT, C.NOMBRE_COMPLETO, C.DPA, TT.MATRICULA, DIR.DIRECCION FROM DIRECCION@INFOGESTI DIR INNER JOIN CLIENTE_DIRECCION@INFOGESTI C_DIR ON DIR.ID = C_DIR.ID_DIRECCION INNER JOIN CLIENTE@INFOGESTI C ON C.ID = C_DIR.ID_CLIENTE INNER JOIN CLIENTE_TT@INFOGESTI TT ON TT.ID_CLIENTE = C.ID LEFT OUTER JOIN CORE_SANTIAGODECUBA RECA ON C.NIT = RECA.NUMEROIDENTIDAD WHERE RECA.NUMEROIDENTIDAD IS NULL AND C.UNIDAD BETWEEN 3401 AND 3409')


    def resolve_infogesti_espiritud(self, info):
        return Cliente.objects.raw('SELECT DISTINCT C.ID, C.NIT, C.NOMBRE_COMPLETO, C.DPA, TT.MATRICULA, DIR.DIRECCION FROM DIRECCION@INFOGESTI DIR INNER JOIN CLIENTE_DIRECCION@INFOGESTI C_DIR ON DIR.ID = C_DIR.ID_DIRECCION INNER JOIN CLIENTE@INFOGESTI C ON C.ID = C_DIR.ID_CLIENTE INNER JOIN CLIENTE_TT@INFOGESTI TT ON TT.ID_CLIENTE = C.ID LEFT OUTER JOIN CORE_SANTICESPIRITUD RECA ON C.NIT = RECA.NUMEROIDENTIDAD WHERE RECA.NUMEROIDENTIDAD IS NULL AND C.UNIDAD BETWEEN 2801 AND 2808')

    def resolve_infogesti_villa(self, info):
        return Cliente.objects.raw('SELECT DISTINCT C.ID, C.NIT, C.NOMBRE_COMPLETO, C.DPA, TT.MATRICULA, DIR.DIRECCION FROM DIRECCION@INFOGESTI DIR INNER JOIN CLIENTE_DIRECCION@INFOGESTI C_DIR ON DIR.ID = C_DIR.ID_DIRECCION INNER JOIN CLIENTE@INFOGESTI C ON C.ID = C_DIR.ID_CLIENTE INNER JOIN CLIENTE_TT@INFOGESTI TT ON TT.ID_CLIENTE = C.ID LEFT OUTER JOIN CORE_VILLACLARA RECA ON C.NIT = RECA.NUMEROIDENTIDAD WHERE RECA.NUMEROIDENTIDAD IS NULL AND C.UNIDAD BETWEEN 2601 AND 2613')


    def resolve_infogesti_holguin(self, info):
        return Cliente.objects.raw('SELECT DISTINCT C.ID, C.NIT, C.NOMBRE_COMPLETO, C.DPA, TT.MATRICULA, DIR.DIRECCION FROM DIRECCION@INFOGESTI DIR INNER JOIN CLIENTE_DIRECCION@INFOGESTI C_DIR ON DIR.ID = C_DIR.ID_DIRECCION INNER JOIN CLIENTE@INFOGESTI C ON C.ID = C_DIR.ID_CLIENTE INNER JOIN CLIENTE_TT@INFOGESTI TT ON TT.ID_CLIENTE = C.ID LEFT OUTER JOIN CORE_HOLGUIN RECA ON C.NIT = RECA.NUMEROIDENTIDAD WHERE RECA.NUMEROIDENTIDAD IS NULL AND C.UNIDAD BETWEEN 3201 AND 3214')


    def resolve_infogesti_guantanamo(self, info):
        return Cliente.objects.raw('SELECT DISTINCT C.ID, C.NIT, C.NOMBRE_COMPLETO, C.DPA, TT.MATRICULA, DIR.DIRECCION FROM DIRECCION@INFOGESTI DIR INNER JOIN CLIENTE_DIRECCION@INFOGESTI C_DIR ON DIR.ID = C_DIR.ID_DIRECCION INNER JOIN CLIENTE@INFOGESTI C ON C.ID = C_DIR.ID_CLIENTE INNER JOIN CLIENTE_TT@INFOGESTI TT ON TT.ID_CLIENTE = C.ID LEFT OUTER JOIN CORE_GUANTANAMO RECA ON C.NIT = RECA.NUMEROIDENTIDAD WHERE RECA.NUMEROIDENTIDAD IS NULL AND C.UNIDAD BETWEEN 3501 AND 3510')


schema = graphene.Schema(query=ContributorsFromInfogestiQuery, auto_camelcase=False)
