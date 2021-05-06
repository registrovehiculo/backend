import graphene
from capitania.apps.api.types.provincias import LaHabanaType, LaHabanaType
from capitania.apps.core.models import LaHabana, LaHabana


class ContributorsFromLaHabanaQuery(graphene.ObjectType):
    contributors_missing_in_onat_la_habana = graphene.List(LaHabanaType, city_name=graphene.String())
    contributors_with_different_information_la_habana_plate = graphene.List(LaHabanaType, city_name=graphene.String())
    contributors_with_different_information_la_habana_name = graphene.List(LaHabanaType, city_name=graphene.String())
    contributors_with_equals_information_la_habana = graphene.List(LaHabanaType, city_name=graphene.String())
    habana = graphene.List(LaHabanaType)

    # 1 Contribuyentes que estan en capitania vehiculo que no estan en la onat
    def resolve_contributors_missing_in_onat_la_habana(self, info, city_name=graphene.String()):
        # La Habana
        if city_name == 'Playa':
            return LaHabana.objects.raw(
                'select distinct * from CORE_LAHABANA hab LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@INFOGESTI I ON hab.NUMEROIDENTIDAD =  I.NIT WHERE I.NIT IS NULL and DPA = 2301')
        if city_name == 'Plaza De La Revolucion':
            return LaHabana.objects.raw(
                'select distinct * from CORE_LAHABANA hab LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@INFOGESTI I ON hab.NUMEROIDENTIDAD =  I.NIT WHERE I.NIT IS NULL and DPA = 2302')
        if city_name == 'Centro Habana':
            return LaHabana.objects.raw(
                'select distinct * from CORE_LAHABANA hab LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@INFOGESTI I ON hab.NUMEROIDENTIDAD =  I.NIT WHERE I.NIT IS NULL and DPA = 2303')
        if city_name == 'La Habana Vieja':
            return LaHabana.objects.raw(
                'select distinct * from CORE_LAHABANA hab LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@INFOGESTI I ON hab.NUMEROIDENTIDAD =  I.NIT WHERE I.NIT IS NULL and DPA = 2304')
        if city_name == 'Regla':
            return LaHabana.objects.raw(
                'select distinct * from CORE_LAHABANA hab LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@INFOGESTI I ON hab.NUMEROIDENTIDAD =  I.NIT WHERE I.NIT IS NULL and DPA = 2305')
        if city_name == 'La Habana Del Este':
            return LaHabana.objects.raw(
                'select distinct * from CORE_LAHABANA hab LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@INFOGESTI I ON hab.NUMEROIDENTIDAD =  I.NIT WHERE I.NIT IS NULL and DPA = 2306')
        if city_name == 'Guanabacoa':
            return LaHabana.objects.raw(
                'select distinct * from CORE_LAHABANA hab LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@INFOGESTI I ON hab.NUMEROIDENTIDAD =  I.NIT WHERE I.NIT IS NULL and DPA = 2307')
        if city_name == 'San Miguel Del Padron':
            return LaHabana.objects.raw(
                'select distinct * from CORE_LAHABANA hab LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@INFOGESTI I ON hab.NUMEROIDENTIDAD =  I.NIT WHERE I.NIT IS NULL and DPA = 2308')
        if city_name == 'Diez De Octubre':
            return LaHabana.objects.raw(
                'select distinct * from CORE_LAHABANA hab LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@INFOGESTI I ON hab.NUMEROIDENTIDAD =  I.NIT WHERE I.NIT IS NULL and DPA = 2309')
        if city_name == 'Cerro':
            return LaHabana.objects.raw(
                'select distinct * from CORE_LAHABANA hab LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@INFOGESTI I ON hab.NUMEROIDENTIDAD =  I.NIT WHERE I.NIT IS NULL and DPA = 2310')
        if city_name == 'Marianao':
            return LaHabana.objects.raw(
                'select distinct * from CORE_LAHABANA hab LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@INFOGESTI I ON hab.NUMEROIDENTIDAD =  I.NIT WHERE I.NIT IS NULL and DPA = 2311')
        if city_name == 'La Lisa':
            return LaHabana.objects.raw(
                'select distinct * from CORE_LAHABANA hab LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@INFOGESTI I ON hab.NUMEROIDENTIDAD =  I.NIT WHERE I.NIT IS NULL and DPA = 2312')
        if city_name == 'Boyeros':
            return LaHabana.objects.raw(
                'select distinct * from CORE_LAHABANA hab LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@INFOGESTI I ON hab.NUMEROIDENTIDAD =  I.NIT WHERE I.NIT IS NULL and DPA = 2313')
        if city_name == 'Arroyo Naranjo':
            return LaHabana.objects.raw(
                'select distinct * from CORE_LAHABANA hab LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@INFOGESTI I ON hab.NUMEROIDENTIDAD =  I.NIT WHERE I.NIT IS NULL and DPA = 2314')
        if city_name == 'Cotorro':
            return LaHabana.objects.raw(
                'select distinct * from CORE_LAHABANA hab LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@INFOGESTI I ON hab.NUMEROIDENTIDAD =  I.NIT WHERE I.NIT IS NULL and DPA = 2315')

    # 2 Contribuyentes que estan en ambos capitania con informaciones diferentes
    def resolve_contributors_with_different_information_la_habana_plate(self, info, city_name=graphene.String()):
        if city_name == 'Playa':
            return LaHabana.objects.raw(
                "select distinct * from CORE_LAHABANA h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2301 and h.DPA = 2301 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> h.CHAPANUEVA")
        if city_name == 'Plaza De La Revolucion':
            return LaHabana.objects.raw(
                "select distinct * from CORE_LAHABANA h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2302 and h.DPA = 2302 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> h.CHAPANUEVA")
        if city_name == 'Centro Habana':
            return LaHabana.objects.raw(
                "select distinct * from CORE_LAHABANA h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2303 and h.DPA = 2303 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> h.CHAPANUEVA")
        if city_name == 'La Habana Vieja':
            return LaHabana.objects.raw(
                "select distinct * from CORE_LAHABANA h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2304 and h.DPA = 2304 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> h.CHAPANUEVA")
        if city_name == 'Regla':
            return LaHabana.objects.raw(
                "select distinct * from CORE_LAHABANA h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2305 and h.DPA = 2305 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> h.CHAPANUEVA")
        if city_name == 'La Habana Del Este':
            return LaHabana.objects.raw(
                "select distinct * from CORE_LAHABANA h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2306 and h.DPA = 2306 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> h.CHAPANUEVA")
        if city_name == 'Guanabacoa':
            return LaHabana.objects.raw(
                "select distinct * from CORE_LAHABANA h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2307 and h.DPA = 2307 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> h.CHAPANUEVA")
        if city_name == 'San Miguel Del Padron':
            return LaHabana.objects.raw(
                "select distinct * from CORE_LAHABANA h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2308 and h.DPA = 2308 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> h.CHAPANUEVA")
        if city_name == 'Diez De Octubre':
            return LaHabana.objects.raw(
                "select distinct * from CORE_LAHABANA h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2309 and h.DPA = 2309 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> h.CHAPANUEVA")
        if city_name == 'Cerro':
            return LaHabana.objects.raw(
                "select distinct * from CORE_LAHABANA h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2310 and h.DPA = 2310 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> h.CHAPANUEVA")
        if city_name == 'Marianao':
            return LaHabana.objects.raw(
                "select distinct * from CORE_LAHABANA h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2311 and h.DPA = 2311 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> h.CHAPANUEVA")
        if city_name == 'La Lisa':
            return LaHabana.objects.raw(
                "select distinct * from CORE_LAHABANA h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2312 and h.DPA = 2312 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> h.CHAPANUEVA")
        if city_name == 'Boyeros':
            return LaHabana.objects.raw(
                "select distinct * from CORE_LAHABANA h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2313 and h.DPA = 2313 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> h.CHAPANUEVA")
        if city_name == 'Arroyo Naranjo':
            return LaHabana.objects.raw(
                "select distinct * from CORE_LAHABANA h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2314 and h.DPA = 2314 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> h.CHAPANUEVA")
        if city_name == 'Cotorro':
            return LaHabana.objects.raw(
                "select distinct * from CORE_LAHABANA h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2315 and h.DPA = 2315 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> h.CHAPANUEVA")


    def resolve_contributors_with_different_information_la_habana_name(self, info, city_name=graphene.String()):
        if city_name == 'Playa':
            return LaHabana.objects.raw(
                "select distinct * from CORE_LAHABANA h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2301 and h.DPA = 2301 AND cl.NOMBRE_COMPLETO <> h.DATOSPERSONA inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'Plaza De La Revolucion':
            return LaHabana.objects.raw(
                "select distinct * from CORE_LAHABANA h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2302 and h.DPA = 2302 AND cl.NOMBRE_COMPLETO <> h.DATOSPERSONA inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'Centro Habana':
            return LaHabana.objects.raw(
                "select distinct * from CORE_LAHABANA h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2303 and h.DPA = 2303 AND cl.NOMBRE_COMPLETO <> h.DATOSPERSONA inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'La Habana Vieja':
            return LaHabana.objects.raw(
                "select distinct * from CORE_LAHABANA h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2304 and h.DPA = 2304 AND cl.NOMBRE_COMPLETO <> h.DATOSPERSONA inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'Regla':
            return LaHabana.objects.raw(
                "select distinct * from CORE_LAHABANA h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2305 and h.DPA = 2305 AND cl.NOMBRE_COMPLETO <> h.DATOSPERSONA inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'La Habana Del Este':
            return LaHabana.objects.raw(
                "select distinct * from CORE_LAHABANA h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2306 and h.DPA = 2306 AND cl.NOMBRE_COMPLETO <> h.DATOSPERSONA inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'Guanabacoa':
            return LaHabana.objects.raw(
                "select distinct * from CORE_LAHABANA h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2307 and h.DPA = 2307 AND cl.NOMBRE_COMPLETO <> h.DATOSPERSONA inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'San Miguel Del Padron':
            return LaHabana.objects.raw(
                "select distinct * from CORE_LAHABANA h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2308 and h.DPA = 2308 AND cl.NOMBRE_COMPLETO <> h.DATOSPERSONA inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'Diez De Octubre':
            return LaHabana.objects.raw(
                "select distinct * from CORE_LAHABANA h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2309 and h.DPA = 2309 AND cl.NOMBRE_COMPLETO <> h.DATOSPERSONA inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'Cerro':
            return LaHabana.objects.raw(
                "select distinct * from CORE_LAHABANA h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2310 and h.DPA = 2310 AND cl.NOMBRE_COMPLETO <> h.DATOSPERSONA inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'Marianao':
            return LaHabana.objects.raw(
                "select distinct * from CORE_LAHABANA h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2311 and h.DPA = 2311 AND cl.NOMBRE_COMPLETO <> h.DATOSPERSONA inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'La Lisa':
            return LaHabana.objects.raw(
                "select distinct * from CORE_LAHABANA h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2312 and h.DPA = 2312 AND cl.NOMBRE_COMPLETO <> h.DATOSPERSONA inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'Boyeros':
            return LaHabana.objects.raw(
                "select distinct * from CORE_LAHABANA h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2313 and h.DPA = 2313 AND cl.NOMBRE_COMPLETO <> h.DATOSPERSONA inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'Arroyo Naranjo':
            return LaHabana.objects.raw(
                "select distinct * from CORE_LAHABANA h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2314 and h.DPA = 2314 AND cl.NOMBRE_COMPLETO <> h.DATOSPERSONA inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'Cotorro':
            return LaHabana.objects.raw(
                "select distinct * from CORE_LAHABANA h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2315 and h.DPA = 2315 AND cl.NOMBRE_COMPLETO <> h.DATOSPERSONA inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")


    # 4 Contribuyentes totalmente coincidentes
    def resolve_contributors_with_equals_information_la_habana(self, info, city_name=graphene.String()):
        if city_name == 'Playa':
            return LaHabana.objects.raw(
                'select distinct * from CORE_LAHABANA h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2301 and h.DPA = 2301 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA = h.CHAPANUEVA order by  h.NUMEROIDENTIDAD')
        if city_name == 'Plaza De La Revolucion':
            return LaHabana.objects.raw(
                'select distinct * from CORE_LAHABANA h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2302 and h.DPA = 2302 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA = h.CHAPANUEVA order by  h.NUMEROIDENTIDAD')
        if city_name == 'Centro Habana':
            return LaHabana.objects.raw(
                'select distinct * from CORE_LAHABANA h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2303 and h.DPA = 2303 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA = h.CHAPANUEVA order by  h.NUMEROIDENTIDAD')
        if city_name == 'La Habana Vieja':
            return LaHabana.objects.raw(
                'select distinct * from CORE_LAHABANA h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2304 and h.DPA = 2304 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA = h.CHAPANUEVA order by  h.NUMEROIDENTIDAD')
        if city_name == 'Regla':
            return LaHabana.objects.raw(
                'select distinct * from CORE_LAHABANA h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2305 and h.DPA = 2305 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA = h.CHAPANUEVA order by  h.NUMEROIDENTIDAD')
        if city_name == 'La Habana Del Este':
            return LaHabana.objects.raw(
                'select distinct * from CORE_LAHABANA h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2306 and h.DPA = 2306 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA = h.CHAPANUEVA order by  h.NUMEROIDENTIDAD')
        if city_name == 'Guanabacoa':
            return LaHabana.objects.raw(
                'select distinct * from CORE_LAHABANA h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2307 and h.DPA = 2307 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA = h.CHAPANUEVA order by  h.NUMEROIDENTIDAD')
        if city_name == 'San Miguel Del Padron':
            return LaHabana.objects.raw(
                'select distinct * from CORE_LAHABANA h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2308 and h.DPA = 2308 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA = h.CHAPANUEVA order by  h.NUMEROIDENTIDAD')
        if city_name == 'Diez De Octubre':
            return LaHabana.objects.raw(
                'select distinct * from CORE_LAHABANA h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2309 and h.DPA = 2309 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA = h.CHAPANUEVA order by  h.NUMEROIDENTIDAD')
        if city_name == 'Cerro':
            return LaHabana.objects.raw(
                'select distinct * from CORE_LAHABANA h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2310 and h.DPA = 2310 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA = h.CHAPANUEVA order by  h.NUMEROIDENTIDAD')
        if city_name == 'Marianao':
            return LaHabana.objects.raw(
                'select distinct * from CORE_LAHABANA h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2311 and h.DPA = 2311 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA = h.CHAPANUEVA order by  h.NUMEROIDENTIDAD')
        if city_name == 'La Lisa':
            return LaHabana.objects.raw(
                'select distinct * from CORE_LAHABANA h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2312 and h.DPA = 2312 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA = h.CHAPANUEVA order by  h.NUMEROIDENTIDAD')
        if city_name == 'Boyeros':
            return LaHabana.objects.raw(
                'select distinct * from CORE_LAHABANA h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2313 and h.DPA = 2313 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA = h.CHAPANUEVA order by  h.NUMEROIDENTIDAD')
        if city_name == 'Arroyo Naranjo':
            return LaHabana.objects.raw(
                'select distinct * from CORE_LAHABANA h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2314 and h.DPA = 2314 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA = h.CHAPANUEVA order by  h.NUMEROIDENTIDAD')
        if city_name == 'Cotorro':
            return LaHabana.objects.raw(
                'select distinct * from CORE_LAHABANA h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2315 and h.DPA = 2315 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA = h.CHAPANUEVA order by  h.NUMEROIDENTIDAD')


    def resolve_la_habana(self, info):
        return LaHabana.objects.all()


schema = graphene.Schema(query=ContributorsFromLaHabanaQuery, auto_camelcase=False)
