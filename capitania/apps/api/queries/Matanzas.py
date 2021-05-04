import graphene
from capitania.apps.api.types.provincias import MatanzasType,MatanzasType
from capitania.apps.core.models import Matanzas, Matanzas


class ContributorsFromMatanzasQuery(graphene.ObjectType):
    contributors_missing_in_onat_matanzas = graphene.List(MatanzasType, city_name=graphene.String())
    contributors_with_different_information_matanzas_plate = graphene.List(MatanzasType, city_name=graphene.String())
    contributors_with_different_information_matanzas_name = graphene.List(MatanzasType, city_name=graphene.String())
    contributors_with_equals_information_matanzas = graphene.List(MatanzasType, city_name=graphene.String())
    matanzas = graphene.List(MatanzasType)

    # 1 Contribuyentes que estan en capitania vehiculo que no estan en la onat
    def resolve_contributors_missing_in_onat_matanzas(self, info, city_name=graphene.String()):

        if city_name == 'Matanzas':
            return Matanzas.objects.raw(
                'select distinct * from CORE_MATANZAS m LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON m.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2501')
        if city_name == 'Cardenas':
            return Matanzas.objects.raw(
                'select distinct * from CORE_MATANZAS m LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON m.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2502')
        if city_name == 'Marti':
            return Matanzas.objects.raw(
                'select distinct * from CORE_MATANZAS m LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON m.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2503')
        if city_name == 'Colon':
            return Matanzas.objects.raw(
                'select distinct * from CORE_MATANZAS m LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON m.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2504')
        if city_name == 'Perico':
            return Matanzas.objects.raw(
                'select distinct * from CORE_MATANZAS m LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON m.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2505')
        if city_name == 'Jovellanos':
            return Matanzas.objects.raw(
                'select distinct * from CORE_MATANZAS m LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON m.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2506')
        if city_name == 'Pedro Betancourt':
            return Matanzas.objects.raw(
                'select distinct * from CORE_MATANZAS m LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON m.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2507')
        if city_name == 'Limonar':
            return Matanzas.objects.raw(
                'select distinct * from CORE_MATANZAS m LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON m.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2508')
        if city_name == 'Union de Reyes':
            return Matanzas.objects.raw(
                'select distinct * from CORE_MATANZAS m LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON m.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2509')
        if city_name == 'Cienaga De Zapata':
            return Matanzas.objects.raw(
                'select distinct * from CORE_MATANZAS m LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON m.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2510')
        if city_name == 'Jagüey Grande':
            return Matanzas.objects.raw(
                'select distinct * from CORE_MATANZAS m LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON m.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2511')
        if city_name == 'Calimete':
            return Matanzas.objects.raw(
                'select distinct * from CORE_MATANZAS m LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON m.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2512')
        if city_name == 'Los Arabos':
            return Matanzas.objects.raw(
                'select distinct * from CORE_MATANZAS m LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON m.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2513')

    # 2 Contribuyentes que estan en ambos capitania con informaciones diferentes
    def resolve_contributors_with_different_information_matanzas_name(self, info, city_name=graphene.String()):

        if city_name == 'Matanzas':
            return Matanzas.objects.raw(
                "select distinct * from CORE_MATANZAS h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2501 and h.DPA = 2501 AND cl.NOMBRE_COMPLETO <> h.DATOSPERSONA inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'Cardenas':
            return Matanzas.objects.raw(
                "select distinct * from CORE_MATANZAS h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2502 and h.DPA = 2502 AND cl.NOMBRE_COMPLETO <> h.DATOSPERSONA inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'Marti':
            return Matanzas.objects.raw(
                "select distinct * from CORE_MATANZAS h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2503 and h.DPA = 2503 AND cl.NOMBRE_COMPLETO <> h.DATOSPERSONA inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'Colon':
            return Matanzas.objects.raw(
                "select distinct * from CORE_MATANZAS h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2504 and h.DPA = 2504 AND cl.NOMBRE_COMPLETO <> h.DATOSPERSONA inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'Perico':
            return Matanzas.objects.raw(
                "select distinct * from CORE_MATANZAS h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2505 and h.DPA = 2505 AND cl.NOMBRE_COMPLETO <> h.DATOSPERSONA inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'Jovellanos':
            return Matanzas.objects.raw(
                "select distinct * from CORE_MATANZAS h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2506 and h.DPA = 2506 AND cl.NOMBRE_COMPLETO <> h.DATOSPERSONA inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'Pedro Betancourt':
            return Matanzas.objects.raw(
                "select distinct * from CORE_MATANZAS h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2507 and h.DPA = 2507 AND cl.NOMBRE_COMPLETO <> h.DATOSPERSONA inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'Limonar':
            return Matanzas.objects.raw(
                "select distinct * from CORE_MATANZAS h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2508 and h.DPA = 2508 AND cl.NOMBRE_COMPLETO <> h.DATOSPERSONA inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'Union de Reyes':
            return Matanzas.objects.raw(
                "select distinct * from CORE_MATANZAS h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2509 and h.DPA = 2509 AND cl.NOMBRE_COMPLETO <> h.DATOSPERSONA inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'Cienaga De Zapata':
            return Matanzas.objects.raw(
                "select distinct * from CORE_MATANZAS h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2510 and h.DPA = 2510 AND cl.NOMBRE_COMPLETO <> h.DATOSPERSONA inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'Jagüey Grande':
            return Matanzas.objects.raw(
                "select distinct * from CORE_MATANZAS h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2511 and h.DPA = 2511 AND cl.NOMBRE_COMPLETO <> h.DATOSPERSONA inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'Calimete':
            return Matanzas.objects.raw(
                "select distinct * from CORE_MATANZAS h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2512 and h.DPA = 2512 AND cl.NOMBRE_COMPLETO <> h.DATOSPERSONA inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'Los Arabos':
            return Matanzas.objects.raw(
                "select distinct * from CORE_MATANZAS h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2513 and h.DPA = 2513 AND cl.NOMBRE_COMPLETO <> h.DATOSPERSONA inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")


    def resolve_contributors_with_different_information_matanzas_plate(self, info, city_name=graphene.String()):

        if city_name == 'Matanzas':
            return Matanzas.objects.raw(
                "select distinct * from CORE_MATANZAS h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2501 and h.DPA = 2501 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> h.CHAPANUEVA")
        if city_name == 'Cardenas':
            return Matanzas.objects.raw(
                "select distinct * from CORE_MATANZAS h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2502 and h.DPA = 2502 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> h.CHAPANUEVA")
        if city_name == 'Marti':
            return Matanzas.objects.raw(
                "select distinct * from CORE_MATANZAS h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2503 and h.DPA = 2503 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> h.CHAPANUEVA")
        if city_name == 'Colon':
            return Matanzas.objects.raw(
                "select distinct * from CORE_MATANZAS h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2504 and h.DPA = 2504 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> h.CHAPANUEVA")
        if city_name == 'Perico':
            return Matanzas.objects.raw(
                "select distinct * from CORE_MATANZAS h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2505 and h.DPA = 2505 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> h.CHAPANUEVA")
        if city_name == 'Jovellanos':
            return Matanzas.objects.raw(
                "select distinct * from CORE_MATANZAS h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2506 and h.DPA = 2506 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> h.CHAPANUEVA")
        if city_name == 'Pedro Betancourt':
            return Matanzas.objects.raw(
                "select distinct * from CORE_MATANZAS h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2507 and h.DPA = 2507 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> h.CHAPANUEVA")
        if city_name == 'Limonar':
            return Matanzas.objects.raw(
                "select distinct * from CORE_MATANZAS h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2508 and h.DPA = 2508 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> h.CHAPANUEVA")
        if city_name == 'Union de Reyes':
            return Matanzas.objects.raw(
                "select distinct * from CORE_MATANZAS h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2509 and h.DPA = 2509 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> h.CHAPANUEVA")
        if city_name == 'Cienaga De Zapata':
            return Matanzas.objects.raw(
                "select distinct * from CORE_MATANZAS h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2510 and h.DPA = 2510 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> h.CHAPANUEVA")
        if city_name == 'Jagüey Grande':
            return Matanzas.objects.raw(
                "select distinct * from CORE_MATANZAS h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2511 and h.DPA = 2511 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> h.CHAPANUEVA")
        if city_name == 'Calimete':
            return Matanzas.objects.raw(
                "select distinct * from CORE_MATANZAS h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2512 and h.DPA = 2512 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> h.CHAPANUEVA")
        if city_name == 'Los Arabos':
            return Matanzas.objects.raw(
                "select distinct * from CORE_MATANZAS h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2513 and h.DPA = 2513 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> h.CHAPANUEVA")


    # 4 Contribuyentes totalmente coincidentes
    def resolve_contributors_with_equals_information_matanzas(self, info, city_name=graphene.String()):

        if city_name == 'Matanzas':
            return Matanzas.objects.raw(
                'select distinct * from CORE_MATANZAS h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2501 and h.DPA = 2501 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA = h.CHAPANUEVA order by  h.NUMEROIDENTIDAD')
        if city_name == 'Cardenas':
            return Matanzas.objects.raw(
                'select distinct * from CORE_MATANZAS h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2502 and h.DPA = 2502 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA = h.CHAPANUEVA order by  h.NUMEROIDENTIDAD')
        if city_name == 'Marti':
            return Matanzas.objects.raw(
                'select distinct * from CORE_MATANZAS h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2503 and h.DPA = 2503 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA = h.CHAPANUEVA order by  h.NUMEROIDENTIDAD')
        if city_name == 'Colon':
            return Matanzas.objects.raw(
                'select distinct * from CORE_MATANZAS h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2504 and h.DPA = 2504 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA = h.CHAPANUEVA order by  h.NUMEROIDENTIDAD')
        if city_name == 'Perico':
            return Matanzas.objects.raw(
                'select distinct * from CORE_MATANZAS h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2505 and h.DPA = 2505 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA = h.CHAPANUEVA order by  h.NUMEROIDENTIDAD')
        if city_name == 'Jovellanos':
            return Matanzas.objects.raw(
                'select distinct * from CORE_MATANZAS h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2506 and h.DPA = 2506 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA = h.CHAPANUEVA order by  h.NUMEROIDENTIDAD')
        if city_name == 'Pedro Betancourt':
            return Matanzas.objects.raw(
                'select distinct * from CORE_MATANZAS h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2507 and h.DPA = 2507 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA = h.CHAPANUEVA order by  h.NUMEROIDENTIDAD')
        if city_name == 'Limonar':
            return Matanzas.objects.raw(
                'select distinct * from CORE_MATANZAS h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2508 and h.DPA = 2508 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA = h.CHAPANUEVA order by  h.NUMEROIDENTIDAD')
        if city_name == 'Union de Reyes':
            return Matanzas.objects.raw(
                'select distinct * from CORE_MATANZAS h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2509 and h.DPA = 2509 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA = h.CHAPANUEVA order by  h.NUMEROIDENTIDAD')
        if city_name == 'Cienaga De Zapata':
            return Matanzas.objects.raw(
                'select distinct * from CORE_MATANZAS h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2510 and h.DPA = 2510 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA = h.CHAPANUEVA order by  h.NUMEROIDENTIDAD')
        if city_name == 'Jagüey Grande':
            return Matanzas.objects.raw(
                'select distinct * from CORE_MATANZAS h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2511 and h.DPA = 2511 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA = h.CHAPANUEVA order by  h.NUMEROIDENTIDAD')
        if city_name == 'Calimete':
            return Matanzas.objects.raw(
                'select distinct * from CORE_MATANZAS h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2512 and h.DPA = 2512 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA = h.CHAPANUEVA order by  h.NUMEROIDENTIDAD')
        if city_name == 'Los Arabos':
            return Matanzas.objects.raw(
                'select distinct * from CORE_MATANZAS h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2513 and h.DPA = 2513 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA = h.CHAPANUEVA order by  h.NUMEROIDENTIDAD')

    def resolve_matanzas(self, info):
        return Matanzas.objects.all()


schema = graphene.Schema(query=ContributorsFromMatanzasQuery, auto_camelcase=False)
