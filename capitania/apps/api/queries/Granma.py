import graphene
from capitania.apps.api.types.provincias import GranmaType, GranmaType
from capitania.apps.core.models import Granma, Granma


class ContributorsFromGranmaQuery(graphene.ObjectType):
    contributors_missing_in_onat_granma = graphene.List(GranmaType, city_name=graphene.String())
    contributors_with_different_information_granma_name = graphene.List(GranmaType, city_name=graphene.String())
    contributors_with_different_information_granma_plate = graphene.List(GranmaType, city_name=graphene.String())
    contributors_with_equals_information_granma = graphene.List(GranmaType, city_name=graphene.String())
    granma = graphene.List(GranmaType)

    # 1 Contribuyentes que estan en capitania vehiculo que no estan en la onat
    def resolve_contributors_missing_in_onat_granma(self, info, city_name=graphene.String()):

        if city_name == 'Rio Cauto':
            return Granma.objects.raw(
                'select distinct * from CORE_GRANMA gm LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON gm.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 3301')
        if city_name == 'Cauto Cristo':
            return Granma.objects.raw(
                'select distinct * from CORE_GRANMA gm LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON gm.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 3302')
        if city_name == 'Jiguani':
            return Granma.objects.raw(
                'select distinct * from CORE_GRANMA gm LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON gm.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 3303')
        if city_name == 'Bayamo':
            return Granma.objects.raw(
                'select distinct * from CORE_GRANMA gm LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON gm.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 3304')
        if city_name == 'Yara':
            return Granma.objects.raw(
                'select distinct * from CORE_GRANMA gm LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON gm.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 3305')
        if city_name == 'Manzanillo':
            return Granma.objects.raw(
                'select distinct * from CORE_GRANMA gm LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON gm.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 3306')
        if city_name == 'Campechuela':
            return Granma.objects.raw(
                'select distinct * from CORE_GRANMA gm LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON gm.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 3307')
        if city_name == 'Media Luna':
            return Granma.objects.raw(
                'select distinct * from CORE_GRANMA gm LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON gm.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 3308')
        if city_name == 'Niquero':
            return Granma.objects.raw(
                'select distinct * from CORE_GRANMA gm LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON gm.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 3309')
        if city_name == 'Pilon':
            return Granma.objects.raw(
                'select distinct * from CORE_GRANMA gm LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON gm.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 3310')
        if city_name == 'Bartolome Maso':
            return Granma.objects.raw(
                'select distinct * from CORE_GRANMA gm LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON gm.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 3311')
        if city_name == 'Buey Arriba':
            return Granma.objects.raw(
                'select distinct * from CORE_GRANMA gm LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON gm.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 3312')
        if city_name == 'Guisa':
            return Granma.objects.raw(
                'select distinct * from CORE_GRANMA gm LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON gm.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 3313')



    # 2 Contribuyentes que estan en ambos capitania con informaciones diferentes
    def resolve_contributors_with_different_information_granma_plate(self, info, city_name=graphene.String()):

        if city_name == 'Rio Cauto':
            return Granma.objects.raw(
                "select distinct * from CORE_GRANMA gm inner join CLIENTE@infogesti cl on cl.NIT = gm.NUMEROIDENTIDAD AND cl.UNIDAD = 3301 and gm.DPA = 3301 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> gm.CHAPANUEVA")
        if city_name == 'Cauto Cristo':
            return Granma.objects.raw(
                "select distinct * from CORE_GRANMA gm inner join CLIENTE@infogesti cl on cl.NIT = gm.NUMEROIDENTIDAD AND cl.UNIDAD = 3302 and gm.DPA = 3302 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> gm.CHAPANUEVA")
        if city_name == 'Jiguani':
            return Granma.objects.raw(
                "select distinct * from CORE_GRANMA gm inner join CLIENTE@infogesti cl on cl.NIT = gm.NUMEROIDENTIDAD AND cl.UNIDAD = 3303 and gm.DPA = 3303 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> gm.CHAPANUEVA")
        if city_name == 'Bayamo':
            return Granma.objects.raw(
                "select distinct * from CORE_GRANMA gm inner join CLIENTE@infogesti cl on cl.NIT = gm.NUMEROIDENTIDAD AND cl.UNIDAD = 3304 and gm.DPA = 3304 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> gm.CHAPANUEVA")
        if city_name == 'Yara':
            return Granma.objects.raw(
                "select distinct * from CORE_GRANMA gm inner join CLIENTE@infogesti cl on cl.NIT = gm.NUMEROIDENTIDAD AND cl.UNIDAD = 3305 and gm.DPA = 3305 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> gm.CHAPANUEVA")
        if city_name == 'Manzanillo':
            return Granma.objects.raw(
                "select distinct * from CORE_GRANMA gm inner join CLIENTE@infogesti cl on cl.NIT = gm.NUMEROIDENTIDAD AND cl.UNIDAD = 3306 and gm.DPA = 3306 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> gm.CHAPANUEVA")
        if city_name == 'Campechuela':
            return Granma.objects.raw(
                "select distinct * from CORE_GRANMA gm inner join CLIENTE@infogesti cl on cl.NIT = gm.NUMEROIDENTIDAD AND cl.UNIDAD = 3307 and gm.DPA = 3307 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> gm.CHAPANUEVA")
        if city_name == 'Media Luna':
            return Granma.objects.raw(
                "select distinct * from CORE_GRANMA gm inner join CLIENTE@infogesti cl on cl.NIT = gm.NUMEROIDENTIDAD AND cl.UNIDAD = 3308 and gm.DPA = 3308 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> gm.CHAPANUEVA")
        if city_name == 'Niquero':
            return Granma.objects.raw(
                "select distinct * from CORE_GRANMA gm inner join CLIENTE@infogesti cl on cl.NIT = gm.NUMEROIDENTIDAD AND cl.UNIDAD = 3309 and gm.DPA = 3309 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> gm.CHAPANUEVA")
        if city_name == 'Pilon':
            return Granma.objects.raw(
                "select distinct * from CORE_GRANMA gm inner join CLIENTE@infogesti cl on cl.NIT = gm.NUMEROIDENTIDAD AND cl.UNIDAD = 3310 and gm.DPA = 3310 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> gm.CHAPANUEVA")
        if city_name == 'Bartolome Maso':
            return Granma.objects.raw(
                "select distinct * from CORE_GRANMA gm inner join CLIENTE@infogesti cl on cl.NIT = gm.NUMEROIDENTIDAD AND cl.UNIDAD = 3311 and gm.DPA = 3311 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> gm.CHAPANUEVA")
        if city_name == 'Buey Arriba':
            return Granma.objects.raw(
                "select distinct * from CORE_GRANMA gm inner join CLIENTE@infogesti cl on cl.NIT = gm.NUMEROIDENTIDAD AND cl.UNIDAD = 3301 and gm.DPA = 3301 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> gm.CHAPANUEVA")
        if city_name == 'Guisa':
            return Granma.objects.raw(
                "select distinct * from CORE_GRANMA gm inner join CLIENTE@infogesti cl on cl.NIT = gm.NUMEROIDENTIDAD AND cl.UNIDAD = 3301 and gm.DPA = 3301 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> gm.CHAPANUEVA")

    def resolve_contributors_with_different_information_granma_name(self, info, city_name=graphene.String()):
        if city_name == 'Rio Cauto':
            return Granma.objects.raw(
                "select distinct * from CORE_GRANMA gm inner join CLIENTE@infogesti cl on cl.NIT = gm.NUMEROIDENTIDAD AND cl.UNIDAD = 3301 and gm.DPA = 3301 AND upper(cl.NOMBRE_COMPLETO) <> upper(gm.DATOSPERSONA) inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'Cauto Cristo':
            return Granma.objects.raw(
                "select distinct * from CORE_GRANMA gm inner join CLIENTE@infogesti cl on cl.NIT = gm.NUMEROIDENTIDAD AND cl.UNIDAD = 3302 and gm.DPA = 3302 AND upper(cl.NOMBRE_COMPLETO) <> upper(gm.DATOSPERSONA) inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'Jiguani':
            return Granma.objects.raw(
                "select distinct * from CORE_GRANMA gm inner join CLIENTE@infogesti cl on cl.NIT = gm.NUMEROIDENTIDAD AND cl.UNIDAD = 3303 and gm.DPA = 3303 AND upper(cl.NOMBRE_COMPLETO) <> upper(gm.DATOSPERSONA) inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'Bayamo':
            return Granma.objects.raw(
                "select distinct * from CORE_GRANMA gm inner join CLIENTE@infogesti cl on cl.NIT = gm.NUMEROIDENTIDAD AND cl.UNIDAD = 3304 and gm.DPA = 3304 AND upper(cl.NOMBRE_COMPLETO) <> upper(gm.DATOSPERSONA) inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'Yara':
            return Granma.objects.raw(
                "select distinct * from CORE_GRANMA gm inner join CLIENTE@infogesti cl on cl.NIT = gm.NUMEROIDENTIDAD AND cl.UNIDAD = 3305 and gm.DPA = 3305 AND upper(cl.NOMBRE_COMPLETO) <> upper(gm.DATOSPERSONA) inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'Manzanillo':
            return Granma.objects.raw(
                "select distinct * from CORE_GRANMA gm inner join CLIENTE@infogesti cl on cl.NIT = gm.NUMEROIDENTIDAD AND cl.UNIDAD = 3306 and gm.DPA = 3306 AND upper(cl.NOMBRE_COMPLETO) <> upper(gm.DATOSPERSONA) inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'Campechuela':
            return Granma.objects.raw(
                "select distinct * from CORE_GRANMA gm inner join CLIENTE@infogesti cl on cl.NIT = gm.NUMEROIDENTIDAD AND cl.UNIDAD = 3307 and gm.DPA = 3307 AND upper(cl.NOMBRE_COMPLETO) <> upper(gm.DATOSPERSONA) inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'Media Luna':
            return Granma.objects.raw(
                "select distinct * from CORE_GRANMA gm inner join CLIENTE@infogesti cl on cl.NIT = gm.NUMEROIDENTIDAD AND cl.UNIDAD = 3308 and gm.DPA = 3308 AND upper(cl.NOMBRE_COMPLETO) <> upper(gm.DATOSPERSONA) inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'Niquero':
            return Granma.objects.raw(
                "select distinct * from CORE_GRANMA gm inner join CLIENTE@infogesti cl on cl.NIT = gm.NUMEROIDENTIDAD AND cl.UNIDAD = 3309 and gm.DPA = 3309 AND upper(cl.NOMBRE_COMPLETO) <> upper(gm.DATOSPERSONA) inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'Pilon':
            return Granma.objects.raw(
                "select distinct * from CORE_GRANMA gm inner join CLIENTE@infogesti cl on cl.NIT = gm.NUMEROIDENTIDAD AND cl.UNIDAD = 3310 and gm.DPA = 3310 AND upper(cl.NOMBRE_COMPLETO) <> upper(gm.DATOSPERSONA) inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'Bartolome Maso':
            return Granma.objects.raw(
                "select distinct * from CORE_GRANMA gm inner join CLIENTE@infogesti cl on cl.NIT = gm.NUMEROIDENTIDAD AND cl.UNIDAD = 3311 and gm.DPA = 3311 AND upper(cl.NOMBRE_COMPLETO) <> upper(gm.DATOSPERSONA) inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'Buey Arriba':
            return Granma.objects.raw(
                "select distinct * from CORE_GRANMA gm inner join CLIENTE@infogesti cl on cl.NIT = gm.NUMEROIDENTIDAD AND cl.UNIDAD = 3312 and gm.DPA = 3312 AND upper(cl.NOMBRE_COMPLETO) <> upper(gm.DATOSPERSONA) inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'Guisa':
            return Granma.objects.raw(
                "select distinct * from CORE_GRANMA gm inner join CLIENTE@infogesti cl on cl.NIT = gm.NUMEROIDENTIDAD AND cl.UNIDAD = 3313 and gm.DPA = 3313 AND upper(cl.NOMBRE_COMPLETO) <> upper(gm.DATOSPERSONA) inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")

    # 4 Contribuyentes totalmente coincidentes
    def resolve_contributors_with_equals_information_granma(self, info, city_name=graphene.String()):
        if city_name == 'Rio Cauto':
            return Granma.objects.raw(
                'select distinct * from CORE_GRANMA h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 3301 and h.DPA = 3301 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA = h.CHAPANUEVA order by  h.NUMEROIDENTIDAD')
        if city_name == 'Cauto Cristo':
            return Granma.objects.raw(
                'select distinct * from CORE_GRANMA h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 3302 and h.DPA = 3302 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA = h.CHAPANUEVA order by  h.NUMEROIDENTIDAD')
        if city_name == 'Jiguani':
            return Granma.objects.raw(
                'select distinct * from CORE_GRANMA h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 3303 and h.DPA = 3303 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA = h.CHAPANUEVA order by  h.NUMEROIDENTIDAD')
        if city_name == 'Bayamo':
            return Granma.objects.raw(
                'select distinct * from CORE_GRANMA h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 3304 and h.DPA = 3304 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA = h.CHAPANUEVA order by  h.NUMEROIDENTIDAD')
        if city_name == 'Yara':
            return Granma.objects.raw(
                'select distinct * from CORE_GRANMA h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 3305 and h.DPA = 3305 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA = h.CHAPANUEVA order by  h.NUMEROIDENTIDAD')
        if city_name == 'Manzanillo':
            return Granma.objects.raw(
                'select distinct * from CORE_GRANMA h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 3306 and h.DPA = 3306 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA = h.CHAPANUEVA order by  h.NUMEROIDENTIDAD')
        if city_name == 'Campechuela':
            return Granma.objects.raw(
                'select distinct * from CORE_GRANMA h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 3307 and h.DPA = 3307 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA = h.CHAPANUEVA order by  h.NUMEROIDENTIDAD')
        if city_name == 'Media Luna':
            return Granma.objects.raw(
                'select distinct * from CORE_GRANMA h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 3308 and h.DPA = 3308 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA = h.CHAPANUEVA order by  h.NUMEROIDENTIDAD')
        if city_name == 'Niquero':
            return Granma.objects.raw(
                'select distinct * from CORE_GRANMA h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 3309 and h.DPA = 3309 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA = h.CHAPANUEVA order by  h.NUMEROIDENTIDAD')
        if city_name == 'Pilon':
            return Granma.objects.raw(
                'select distinct * from CORE_GRANMA h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 3310 and h.DPA = 3310 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA = h.CHAPANUEVA order by  h.NUMEROIDENTIDAD')
        if city_name == 'Bartolome Maso':
            return Granma.objects.raw(
                'select distinct * from CORE_GRANMA h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 3311 and h.DPA = 3311 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA = h.CHAPANUEVA order by  h.NUMEROIDENTIDAD')
        if city_name == 'Buey Arriba':
            return Granma.objects.raw(
                'select distinct * from CORE_GRANMA h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 3312 and h.DPA = 3312 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA = h.CHAPANUEVA order by  h.NUMEROIDENTIDAD')
        if city_name == 'Guisa':
            return Granma.objects.raw(
                'select distinct * from CORE_GRANMA h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 3313 and h.DPA = 3313 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA = h.CHAPANUEVA order by  h.NUMEROIDENTIDAD')


    def resolve_granma(self, info):
        return Granma.objects.all()


schema = graphene.Schema(query=ContributorsFromGranmaQuery, auto_camelcase=False)
