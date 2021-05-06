import graphene
from capitania.apps.api.types.provincias import GuantanamoType, GuantanamoType
from capitania.apps.core.models import Guantanamo, Guantanamo


class ContributorsFromGuantanamoQuery(graphene.ObjectType):
    contributors_missing_in_onat_guantanamo = graphene.List(GuantanamoType, city_name=graphene.String())
    contributors_with_different_information_guantanamo_plate = graphene.List(GuantanamoType, city_name=graphene.String())
    contributors_with_different_information_guantanamo_name = graphene.List(GuantanamoType, city_name=graphene.String())
    contributors_with_equals_information_guantanamo = graphene.List(GuantanamoType, city_name=graphene.String())
    guantanamo = graphene.List(GuantanamoType)

    # 1 Contribuyentes que estan en capitania vehiculo que no estan en la onat
    def resolve_contributors_missing_in_onat_guantanamo(self, info, city_name=graphene.String()):

        if city_name == 'El Salvador':
            return Guantanamo.objects.raw(
                'select distinct * from CORE_GUANTANAMO gm LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON gm.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 3501')
        if city_name == 'Manuel Tames':
            return Guantanamo.objects.raw(
                'select distinct * from CORE_GUANTANAMO gm LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON gm.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 3502')
        if city_name == 'Yateras':
            return Guantanamo.objects.raw(
                'select distinct * from CORE_GUANTANAMO gm LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON gm.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 3503')
        if city_name == 'Baracoa':
            return Guantanamo.objects.raw(
                'select distinct * from CORE_GUANTANAMO gm LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON gm.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 3504')
        if city_name == 'Maisi':
            return Guantanamo.objects.raw(
                'select distinct * from CORE_GUANTANAMO gm LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON gm.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 3505')
        if city_name == 'Imias':
            return Guantanamo.objects.raw(
                'select distinct * from CORE_GUANTANAMO gm LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON gm.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 3506')
        if city_name == 'San Antonio Del Sur':
            return Guantanamo.objects.raw(
                'select distinct * from CORE_GUANTANAMO gm LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON gm.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 3507')
        if city_name == 'Caimanera':
            return Guantanamo.objects.raw(
                'select distinct * from CORE_GUANTANAMO gm LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON gm.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 3508')
        if city_name == 'Guantanamo':
            return Guantanamo.objects.raw(
                'select distinct * from CORE_GUANTANAMO gm LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON gm.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 3509')
        if city_name == 'Niceto Perez':
            return Guantanamo.objects.raw(
                'select distinct * from CORE_GUANTANAMO gm LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON gm.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 3510')



    # 2 Contribuyentes que estan en ambos capitania con informaciones diferentes
    def resolve_contributors_with_different_information_guantanamo_plate(self, info, city_name=graphene.String()):

        if city_name == 'El Salvador':
            return Guantanamo.objects.raw(
                "select distinct * from CORE_GUANTANAMO gm inner join CLIENTE@infogesti cl on cl.NIT = gm.NUMEROIDENTIDAD AND cl.UNIDAD = 3501 and gm.DPA = 3501 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> gm.CHAPANUEVA")
        if city_name == 'Manuel Tames':
            return Guantanamo.objects.raw(
                "select distinct * from CORE_GUANTANAMO gm inner join CLIENTE@infogesti cl on cl.NIT = gm.NUMEROIDENTIDAD AND cl.UNIDAD = 3502 and gm.DPA = 3502 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> gm.CHAPANUEVA")
        if city_name == 'Yateras':
            return Guantanamo.objects.raw(
                "select distinct * from CORE_GUANTANAMO gm inner join CLIENTE@infogesti cl on cl.NIT = gm.NUMEROIDENTIDAD AND cl.UNIDAD = 3503 and gm.DPA = 3503 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> gm.CHAPANUEVA")
        if city_name == 'Baracoa':
            return Guantanamo.objects.raw(
                "select distinct * from CORE_GUANTANAMO gm inner join CLIENTE@infogesti cl on cl.NIT = gm.NUMEROIDENTIDAD AND cl.UNIDAD = 3504 and gm.DPA = 3504 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> gm.CHAPANUEVA")
        if city_name == 'Maisi':
            return Guantanamo.objects.raw(
                "select distinct * from CORE_GUANTANAMO gm inner join CLIENTE@infogesti cl on cl.NIT = gm.NUMEROIDENTIDAD AND cl.UNIDAD = 3505 and gm.DPA = 3505 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> gm.CHAPANUEVA")
        if city_name == 'Imias':
            return Guantanamo.objects.raw(
                "select distinct * from CORE_GUANTANAMO gm inner join CLIENTE@infogesti cl on cl.NIT = gm.NUMEROIDENTIDAD AND cl.UNIDAD = 3506 and gm.DPA = 3506 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> gm.CHAPANUEVA")
        if city_name == 'San Antonio Del Sur':
            return Guantanamo.objects.raw(
                "select distinct * from CORE_GUANTANAMO gm inner join CLIENTE@infogesti cl on cl.NIT = gm.NUMEROIDENTIDAD AND cl.UNIDAD = 3507 and gm.DPA = 3507 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> gm.CHAPANUEVA")
        if city_name == 'Caimanera':
            return Guantanamo.objects.raw(
                "select distinct * from CORE_GUANTANAMO gm inner join CLIENTE@infogesti cl on cl.NIT = gm.NUMEROIDENTIDAD AND cl.UNIDAD = 3508 and gm.DPA = 3508 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> gm.CHAPANUEVA")
        if city_name == 'Guantanamo':
            return Guantanamo.objects.raw(
                "select distinct * from CORE_GUANTANAMO gm inner join CLIENTE@infogesti cl on cl.NIT = gm.NUMEROIDENTIDAD AND cl.UNIDAD = 3509 and gm.DPA = 3509 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> gm.CHAPANUEVA")
        if city_name == 'Niceto Perez':
            return Guantanamo.objects.raw(
                "select distinct * from CORE_GUANTANAMO gm inner join CLIENTE@infogesti cl on cl.NIT = gm.NUMEROIDENTIDAD AND cl.UNIDAD = 3510 and gm.DPA = 3510 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> gm.CHAPANUEVA")


    def resolve_contributors_with_different_information_guantanamo_name(self, info, city_name=graphene.String()):

        if city_name == 'El Salvador':
            return Guantanamo.objects.raw(
                "select distinct * from CORE_GUANTANAMO gm inner join CLIENTE@infogesti cl on cl.NIT = gm.NUMEROIDENTIDAD AND cl.UNIDAD = 3501 and gm.DPA = 3501 AND upper(cl.NOMBRE_COMPLETO) <> upper(gm.DATOSPERSONA) inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'Manuel Tames':
            return Guantanamo.objects.raw(
                "select distinct * from CORE_GUANTANAMO gm inner join CLIENTE@infogesti cl on cl.NIT = gm.NUMEROIDENTIDAD AND cl.UNIDAD = 3502 and gm.DPA = 3502 AND upper(cl.NOMBRE_COMPLETO) <> upper(gm.DATOSPERSONA) inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'Yateras':
            return Guantanamo.objects.raw(
                "select distinct * from CORE_GUANTANAMO gm inner join CLIENTE@infogesti cl on cl.NIT = gm.NUMEROIDENTIDAD AND cl.UNIDAD = 3503 and gm.DPA = 3503 AND upper(cl.NOMBRE_COMPLETO) <> upper(gm.DATOSPERSONA) inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'Baracoa':
            return Guantanamo.objects.raw(
                "select distinct * from CORE_GUANTANAMO gm inner join CLIENTE@infogesti cl on cl.NIT = gm.NUMEROIDENTIDAD AND cl.UNIDAD = 3504 and gm.DPA = 3504 AND upper(cl.NOMBRE_COMPLETO) <> upper(gm.DATOSPERSONA) inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'Maisi':
            return Guantanamo.objects.raw(
                "select distinct * from CORE_GUANTANAMO gm inner join CLIENTE@infogesti cl on cl.NIT = gm.NUMEROIDENTIDAD AND cl.UNIDAD = 3505 and gm.DPA = 3505 AND upper(cl.NOMBRE_COMPLETO) <> upper(gm.DATOSPERSONA) inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'Imias':
            return Guantanamo.objects.raw(
                "select distinct * from CORE_GUANTANAMO gm inner join CLIENTE@infogesti cl on cl.NIT = gm.NUMEROIDENTIDAD AND cl.UNIDAD = 3506 and gm.DPA = 3506 AND upper(cl.NOMBRE_COMPLETO) <> upper(gm.DATOSPERSONA) inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'San Antonio Del Sur':
            return Guantanamo.objects.raw(
                "select distinct * from CORE_GUANTANAMO gm inner join CLIENTE@infogesti cl on cl.NIT = gm.NUMEROIDENTIDAD AND cl.UNIDAD = 3507 and gm.DPA = 3507 AND upper(cl.NOMBRE_COMPLETO) <> upper(gm.DATOSPERSONA) inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'Caimanera':
            return Guantanamo.objects.raw(
                "select distinct * from CORE_GUANTANAMO gm inner join CLIENTE@infogesti cl on cl.NIT = gm.NUMEROIDENTIDAD AND cl.UNIDAD = 3508 and gm.DPA = 3508 AND upper(cl.NOMBRE_COMPLETO) <> upper(gm.DATOSPERSONA) inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'Guantanamo':
            return Guantanamo.objects.raw(
                "select distinct * from CORE_GUANTANAMO gm inner join CLIENTE@infogesti cl on cl.NIT = gm.NUMEROIDENTIDAD AND cl.UNIDAD = 3509 and gm.DPA = 3509 AND upper(cl.NOMBRE_COMPLETO) <> upper(gm.DATOSPERSONA) inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'Niceto Perez':
            return Guantanamo.objects.raw(
                "select distinct * from CORE_GUANTANAMO gm inner join CLIENTE@infogesti cl on cl.NIT = gm.NUMEROIDENTIDAD AND cl.UNIDAD = 3510 and gm.DPA = 3510 AND upper(cl.NOMBRE_COMPLETO) <> upper(gm.DATOSPERSONA) inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")


    # 4 Contribuyentes totalmente coincidentes
    def resolve_contributors_with_equals_information_guantanamo(self, info, city_name=graphene.String()):

        if city_name == 'El Salvador':
            return Guantanamo.objects.raw(
                'select distinct * from CORE_GUANTANAMO h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 3501 and h.DPA = 3501 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA = h.CHAPANUEVA order by  h.NUMEROIDENTIDAD')
        if city_name == 'Manuel Tames':
            return Guantanamo.objects.raw(
                'select distinct * from CORE_GUANTANAMO h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 3502 and h.DPA = 3502 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA = h.CHAPANUEVA order by  h.NUMEROIDENTIDAD')
        if city_name == 'Yateras':
            return Guantanamo.objects.raw(
                'select distinct * from CORE_GUANTANAMO h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 3503 and h.DPA = 3503 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA = h.CHAPANUEVA order by  h.NUMEROIDENTIDAD')
        if city_name == 'Baracoa':
            return Guantanamo.objects.raw(
                'select distinct * from CORE_GUANTANAMO h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 3504 and h.DPA = 3504 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA = h.CHAPANUEVA order by  h.NUMEROIDENTIDAD')
        if city_name == 'Maisi':
            return Guantanamo.objects.raw(
                'select distinct * from CORE_GUANTANAMO h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 3505 and h.DPA = 3505 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA = h.CHAPANUEVA order by  h.NUMEROIDENTIDAD')
        if city_name == 'Imias':
            return Guantanamo.objects.raw(
                'select distinct * from CORE_GUANTANAMO h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 3506 and h.DPA = 3506 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA = h.CHAPANUEVA order by  h.NUMEROIDENTIDAD')
        if city_name == 'San Antonio Del Sur':
            return Guantanamo.objects.raw(
                'select distinct * from CORE_GUANTANAMO h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 3507 and h.DPA = 3507 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA = h.CHAPANUEVA order by  h.NUMEROIDENTIDAD')
        if city_name == 'Caimanera':
            return Guantanamo.objects.raw(
                'select distinct * from CORE_GUANTANAMO h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 3508 and h.DPA = 3508 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA = h.CHAPANUEVA order by  h.NUMEROIDENTIDAD')
        if city_name == 'Guantanamo':
            return Guantanamo.objects.raw(
                'select distinct * from CORE_GUANTANAMO h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 3509 and h.DPA = 3509 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA = h.CHAPANUEVA order by  h.NUMEROIDENTIDAD')
        if city_name == 'Niceto Perez':
            return Guantanamo.objects.raw(
                'select distinct * from CORE_GUANTANAMO h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 3510 and h.DPA = 3510 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA = h.CHAPANUEVA order by  h.NUMEROIDENTIDAD')

    def resolve_guantanamo(self, info):
        return Guantanamo.objects.all()


schema = graphene.Schema(query=ContributorsFromGuantanamoQuery, auto_camelcase=False)
