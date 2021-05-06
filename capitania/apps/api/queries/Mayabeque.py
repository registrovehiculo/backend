import graphene
from capitania.apps.api.types.provincias import MayabequeType,  MayabequeType
from capitania.apps.core.models import Mayabeque, Mayabeque


class ContributorsFromMayabequeQuery(graphene.ObjectType):
    contributors_missing_in_onat_mayabeque = graphene.List(MayabequeType, city_name=graphene.String())
    contributors_with_different_information_mayabeque_plate = graphene.List(MayabequeType, city_name=graphene.String())
    contributors_with_different_information_mayabeque_name = graphene.List(MayabequeType, city_name=graphene.String())
    contributors_with_equals_information_mayabeque = graphene.List(MayabequeType, city_name=graphene.String())
    mayabeque = graphene.List(MayabequeType)

    # 1 Contribuyentes que estan en capitania vehiculo que no estan en la onat
    def resolve_contributors_missing_in_onat_mayabeque(self, info, city_name=graphene.String()):
        # Mayabueque
        if city_name == 'Bejucal':
            return Mayabeque.objects.raw(
                'select distinct * from CORE_MAYABEQUE m LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON m.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2401')
        if city_name == 'San Jose de las Lajas':
            return Mayabeque.objects.raw(
                'select distinct * from CORE_MAYABEQUE m LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON m.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2402')
        if city_name == 'Jaruco':
            return Mayabeque.objects.raw(
                'select distinct * from CORE_MAYABEQUE m LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON m.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2403')
        if city_name == 'Santa Cruz del Norte':
            return Mayabeque.objects.raw(
                'select distinct * from CORE_MAYABEQUE m LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON m.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2404')
        if city_name == 'Madruga':
            return Mayabeque.objects.raw(
                'select distinct * from CORE_MAYABEQUE m LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON m.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2405')
        if city_name == 'Nueva Paz':
            return Mayabeque.objects.raw(
                'select distinct * from CORE_MAYABEQUE m LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON m.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2406')
        if city_name == 'San Nicolás':
            return Mayabeque.objects.raw(
                'select distinct * from CORE_MAYABEQUE m LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON m.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2407')
        if city_name == 'Güines':
            return Mayabeque.objects.raw(
                'select distinct * from CORE_MAYABEQUE m LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON m.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2408')
        if city_name == 'Melena del Sur':
            return Mayabeque.objects.raw(
                'select distinct * from CORE_MAYABEQUE m LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON m.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2409')
        if city_name == 'Batabano':
            return Mayabeque.objects.raw(
                'select distinct * from CORE_MAYABEQUE m LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON m.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2410')
        if city_name == 'Quivican':
            return Mayabeque.objects.raw(
                'select distinct * from CORE_MAYABEQUE m LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON m.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2411')

    # 2 Contribuyentes que estan en ambos capitania con informaciones diferentes
    def resolve_contributors_with_different_information_mayabeque_plate(self, info, city_name=graphene.String()):
        if city_name == 'Bejucal':
            return Mayabeque.objects.raw(
                "select distinct * from CORE_MAYABEQUE h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2401 and h.DPA = 2401 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> h.CHAPANUEVA")
        if city_name == 'San Jose de las Lajas':
            return Mayabeque.objects.raw(
                "select distinct * from CORE_MAYABEQUE h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2402 and h.DPA = 2402 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> h.CHAPANUEVA")
        if city_name == 'Jaruco':
            return Mayabeque.objects.raw(
                "select distinct * from CORE_MAYABEQUE h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2403 and h.DPA = 2403 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> h.CHAPANUEVA")
        if city_name == 'Santa Cruz del Norte':
            return Mayabeque.objects.raw(
                "select distinct * from CORE_MAYABEQUE h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2404 and h.DPA = 2404 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> h.CHAPANUEVA")
        if city_name == 'Madruga':
            return Mayabeque.objects.raw(
                "select distinct * from CORE_MAYABEQUE h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2405 and h.DPA = 2405 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> h.CHAPANUEVA")
        if city_name == 'Nueva Paz':
            return Mayabeque.objects.raw(
                "select distinct * from CORE_MAYABEQUE h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2406 and h.DPA = 2406 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> h.CHAPANUEVA")
        if city_name == 'San Nicolás':
            return Mayabeque.objects.raw(
                "select distinct * from CORE_MAYABEQUE h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2407 and h.DPA = 2407 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> h.CHAPANUEVA")
        if city_name == 'Güines':
            return Mayabeque.objects.raw(
                "select distinct * from CORE_MAYABEQUE h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2408 and h.DPA = 2408 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> h.CHAPANUEVA")
        if city_name == 'Melena del Sur':
            return Mayabeque.objects.raw(
                "select distinct * from CORE_MAYABEQUE h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2409 and h.DPA = 2409 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> h.CHAPANUEVA")
        if city_name == 'Batabano':
            return Mayabeque.objects.raw(
                "select distinct * from CORE_MAYABEQUE h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2410 and h.DPA = 2410 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> h.CHAPANUEVA")
        if city_name == 'Quivican':
            return Mayabeque.objects.raw(
                "select distinct * from CORE_MAYABEQUE h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2411 and h.DPA = 2411 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> h.CHAPANUEVA")


    def resolve_contributors_with_different_information_mayabeque_name(self, info, city_name=graphene.String()):
        if city_name == 'Bejucal':
            return Mayabeque.objects.raw(
                "select distinct * from CORE_MAYABEQUE h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2401 and h.DPA = 2401 AND upper(cl.NOMBRE_COMPLETO) <> upper(h.DATOSPERSONA) inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'San Jose de las Lajas':
            return Mayabeque.objects.raw(
                "select distinct * from CORE_MAYABEQUE h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2402 and h.DPA = 2402 AND upper(cl.NOMBRE_COMPLETO) <> upper(h.DATOSPERSONA) inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'Jaruco':
            return Mayabeque.objects.raw(
                "select distinct * from CORE_MAYABEQUE h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2403 and h.DPA = 2403 AND upper(cl.NOMBRE_COMPLETO) <> upper(h.DATOSPERSONA) inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'Santa Cruz del Norte':
            return Mayabeque.objects.raw(
                "select distinct * from CORE_MAYABEQUE h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2404 and h.DPA = 2404 AND upper(cl.NOMBRE_COMPLETO) <> upper(h.DATOSPERSONA) inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'Madruga':
            return Mayabeque.objects.raw(
                "select distinct * from CORE_MAYABEQUE h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2405 and h.DPA = 2405 AND upper(cl.NOMBRE_COMPLETO) <> upper(h.DATOSPERSONA) inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'Nueva Paz':
            return Mayabeque.objects.raw(
                "select distinct * from CORE_MAYABEQUE h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2406 and h.DPA = 2406 AND upper(cl.NOMBRE_COMPLETO) <> upper(h.DATOSPERSONA) inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'San Nicolás':
            return Mayabeque.objects.raw(
                "select distinct * from CORE_MAYABEQUE h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2407 and h.DPA = 2407 AND upper(cl.NOMBRE_COMPLETO) <> upper(h.DATOSPERSONA) inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'Güines':
            return Mayabeque.objects.raw(
                "select distinct * from CORE_MAYABEQUE h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2408 and h.DPA = 2408 AND upper(cl.NOMBRE_COMPLETO) <> upper(h.DATOSPERSONA) inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'Melena del Sur':
            return Mayabeque.objects.raw(
                "select distinct * from CORE_MAYABEQUE h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2409 and h.DPA = 2409 AND upper(cl.NOMBRE_COMPLETO) <> upper(h.DATOSPERSONA) inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'Batabano':
            return Mayabeque.objects.raw(
                "select distinct * from CORE_MAYABEQUE h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2410 and h.DPA = 2410 AND upper(cl.NOMBRE_COMPLETO) <> upper(h.DATOSPERSONA) inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'Quivican':
            return Mayabeque.objects.raw(
                "select distinct * from CORE_MAYABEQUE h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2411 and h.DPA = 2411 AND upper(cl.NOMBRE_COMPLETO) <> upper(h.DATOSPERSONA) inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")

    # 4 Contribuyentes totalmente coincidentes
    def resolve_contributors_with_equals_information_mayabeque(self, info, city_name=graphene.String()):
        if city_name == 'Bejucal':
            return Mayabeque.objects.raw(
                'select distinct * from CORE_MAYABEQUE h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2401 and h.DPA = 2401 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA = h.CHAPANUEVA order by  h.NUMEROIDENTIDAD')
        if city_name == 'San Jose de las Lajas':
            return Mayabeque.objects.raw(
                'select distinct * from CORE_MAYABEQUE h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2402 and h.DPA = 2402 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA = h.CHAPANUEVA order by  h.NUMEROIDENTIDAD')
        if city_name == 'Jaruco':
            return Mayabeque.objects.raw(
                'select distinct * from CORE_MAYABEQUE h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2403 and h.DPA = 2403 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA = h.CHAPANUEVA order by  h.NUMEROIDENTIDAD')
        if city_name == 'Santa Cruz del Norte':
            return Mayabeque.objects.raw(
                'select distinct * from CORE_MAYABEQUE h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2404 and h.DPA = 2404 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA = h.CHAPANUEVA order by  h.NUMEROIDENTIDAD')
        if city_name == 'Madruga':
            return Mayabeque.objects.raw(
                'select distinct * from CORE_MAYABEQUE h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2405 and h.DPA = 2405 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA = h.CHAPANUEVA order by  h.NUMEROIDENTIDAD')
        if city_name == 'Nueva Paz':
            return Mayabeque.objects.raw(
                'select distinct * from CORE_MAYABEQUE h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2406 and h.DPA = 2406 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA = h.CHAPANUEVA order by  h.NUMEROIDENTIDAD')
        if city_name == 'San Nicolás':
            return Mayabeque.objects.raw(
                'select distinct * from CORE_MAYABEQUE h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2407 and h.DPA = 2407 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA = h.CHAPANUEVA order by  h.NUMEROIDENTIDAD')
        if city_name == 'Güines':
            return Mayabeque.objects.raw(
                'select distinct * from CORE_MAYABEQUE h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2408 and h.DPA = 2408 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA = h.CHAPANUEVA order by  h.NUMEROIDENTIDAD')
        if city_name == 'Melena del Sur':
            return Mayabeque.objects.raw(
                'select distinct * from CORE_MAYABEQUE h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2409 and h.DPA = 2409 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA = h.CHAPANUEVA order by  h.NUMEROIDENTIDAD')
        if city_name == 'Batabano':
            return Mayabeque.objects.raw(
                'select distinct * from CORE_MAYABEQUE h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2410 and h.DPA = 2410 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA = h.CHAPANUEVA order by  h.NUMEROIDENTIDAD')
        if city_name == 'Quivican':
            return Mayabeque.objects.raw(
                'select distinct * from CORE_MAYABEQUE h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2411 and h.DPA = 2411 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA = h.CHAPANUEVA order by  h.NUMEROIDENTIDAD')

    def resolve_mayabeque(self, info):
        return Mayabeque.objects.all()


schema = graphene.Schema(query=ContributorsFromMayabequeQuery, auto_camelcase=False)
