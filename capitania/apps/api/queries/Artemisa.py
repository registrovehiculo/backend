import graphene

from capitania.apps.api.types.provincias import ArtemisaType, ArtemisaType
from capitania.apps.core.models import Artemisa, Artemisa


class ContributorsFromArtemisaQuery(graphene.ObjectType):
    contributors_missing_in_onat_artemisa = graphene.List(ArtemisaType, city_name=graphene.String())
    contributors_with_different_information_artemisa_plate = graphene.List(ArtemisaType, city_name=graphene.String())
    contributors_with_different_information_artemisa_name = graphene.List(ArtemisaType, city_name=graphene.String())
    contributors_with_equals_information_artemisa = graphene.List(ArtemisaType, city_name=graphene.String())
    artemisa = graphene.List(ArtemisaType)

    # 1 Contribuyentes que estan en capitania vehiculo que no estan en la onat
    def resolve_contributors_missing_in_onat_artemisa(self, info, city_name=graphene.String()):
        # artemisa
        if city_name == 'Bahia Honda':
            return Artemisa.objects.raw(
                'select distinct * from CORE_ARTEMISA art LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON art.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2201')
        if city_name == 'Alquizar':
            return Artemisa.objects.raw(
                'select distinct * from CORE_ARTEMISA art LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON art.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2202')
        if city_name == 'Artemisa':
            return Artemisa.objects.raw(
                'select distinct * from CORE_ARTEMISA art LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON art.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2203')
        if city_name == 'Bauta':
            return Artemisa.objects.raw(
                'select distinct * from CORE_ARTEMISA art LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON art.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2204')
        if city_name == 'Caimito':
            return Artemisa.objects.raw(
                'select distinct * from CORE_ARTEMISA art LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON art.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2205')
        if city_name == 'Candelaria':
            return Artemisa.objects.raw(
                'select distinct * from CORE_ARTEMISA art LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON art.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2206')
        if city_name == 'Guanajay':
            return Artemisa.objects.raw(
                'select distinct * from CORE_ARTEMISA art LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON art.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2207')
        if city_name == 'Gueira de Melena':
            return Artemisa.objects.raw(
                'select distinct * from CORE_ARTEMISA art LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON art.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2208')
        if city_name == 'Mariel':
            return Artemisa.objects.raw(
                'select distinct * from CORE_ARTEMISA art LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON art.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2209')
        if city_name == 'San Antonio de los Banos':
            return Artemisa.objects.raw(
                'select distinct * from CORE_ARTEMISA art LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON art.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2210')
        if city_name == 'San Cristobal':
            return Artemisa.objects.raw(
                'select distinct * from CORE_ARTEMISA art LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON art.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2211')

    # 2 Contribuyentes que estan en ambos capitania con informaciones diferentes
    def resolve_contributors_with_different_information_artemisa_plate(self, info, city_name=graphene.String()):

        if city_name == 'Bahia Honda':
            return Artemisa.objects.raw(
                "select distinct * from CORE_ARTEMISA art inner join CLIENTE@infogesti cl on cl.NIT = art.NUMEROIDENTIDAD AND cl.UNIDAD = 2201 and art.DPA = 2201 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> art.CHAPANUEVA")
        if city_name == 'Alquizar':
            return Artemisa.objects.raw(
                "select distinct * from CORE_ARTEMISA art inner join CLIENTE@infogesti cl on cl.NIT = art.NUMEROIDENTIDAD AND cl.UNIDAD = 2202 and art.DPA = 2202 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> art.CHAPANUEVA")
        if city_name == 'Artemisa':
            return Artemisa.objects.raw(
                "select distinct * from CORE_ARTEMISA art inner join CLIENTE@infogesti cl on cl.NIT = art.NUMEROIDENTIDAD AND cl.UNIDAD = 2203 and art.DPA = 2203 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> art.CHAPANUEVA")
        if city_name == 'Bauta':
            return Artemisa.objects.raw(
                "select distinct * from CORE_ARTEMISA art inner join CLIENTE@infogesti cl on cl.NIT = art.NUMEROIDENTIDAD AND cl.UNIDAD = 2204 and art.DPA = 2204 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> art.CHAPANUEVA")
        if city_name == 'Caimito':
            return Artemisa.objects.raw(
                "select distinct * from CORE_ARTEMISA art inner join CLIENTE@infogesti cl on cl.NIT = art.NUMEROIDENTIDAD AND cl.UNIDAD = 2205 and art.DPA = 2205 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> art.CHAPANUEVA")
        if city_name == 'Candelaria':
            return Artemisa.objects.raw(
                "select distinct * from CORE_ARTEMISA art inner join CLIENTE@infogesti cl on cl.NIT = art.NUMEROIDENTIDAD AND cl.UNIDAD = 2206 and art.DPA = 2206 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> art.CHAPANUEVA")
        if city_name == 'Guanajay':
            return Artemisa.objects.raw(
                "select distinct * from CORE_ARTEMISA art inner join CLIENTE@infogesti cl on cl.NIT = art.NUMEROIDENTIDAD AND cl.UNIDAD = 2207 and art.DPA = 2207 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> art.CHAPANUEVA")
        if city_name == 'Gueira de Melena':
            return Artemisa.objects.raw(
                "select distinct * from CORE_ARTEMISA art inner join CLIENTE@infogesti cl on cl.NIT = art.NUMEROIDENTIDAD AND cl.UNIDAD = 2208 and art.DPA = 2208 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> art.CHAPANUEVA")
        if city_name == 'Mariel':
            return Artemisa.objects.raw(
                "select distinct * from CORE_ARTEMISA art inner join CLIENTE@infogesti cl on cl.NIT = art.NUMEROIDENTIDAD AND cl.UNIDAD = 2209 and art.DPA = 2209 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> art.CHAPANUEVA")
        if city_name == 'San Antonio de los Banos':
            return Artemisa.objects.raw(
                "select distinct * from CORE_ARTEMISA art inner join CLIENTE@infogesti cl on cl.NIT = art.NUMEROIDENTIDAD AND cl.UNIDAD = 2210 and art.DPA = 2210 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> art.CHAPANUEVA")
        if city_name == 'San Cristobal':
            return Artemisa.objects.raw(
                "select distinct * from CORE_ARTEMISA art inner join CLIENTE@infogesti cl on cl.NIT = art.NUMEROIDENTIDAD AND cl.UNIDAD = 2211 and art.DPA = 2211 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> art.CHAPANUEVA")


    def resolve_contributors_with_different_information_artemisa_name(self, info, city_name=graphene.String()):
        if city_name == 'Bahia Honda':
            return Artemisa.objects.raw(
                "select distinct * from CORE_ARTEMISA art inner join CLIENTE@infogesti cl on cl.NIT = art.NUMEROIDENTIDAD AND cl.UNIDAD = 2201 and art.DPA = 2201 AND cl.NOMBRE_COMPLETO <> art.DATOSPERSONA inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'Alquizar':
            return Artemisa.objects.raw(
                "select distinct * from CORE_ARTEMISA art inner join CLIENTE@infogesti cl on cl.NIT = art.NUMEROIDENTIDAD AND cl.UNIDAD = 2202 and art.DPA = 2202 AND cl.NOMBRE_COMPLETO <> art.DATOSPERSONA inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'Artemisa':
            return Artemisa.objects.raw(
                "select distinct * from CORE_ARTEMISA art inner join CLIENTE@infogesti cl on cl.NIT = art.NUMEROIDENTIDAD AND cl.UNIDAD = 2203 and art.DPA = 2203 AND cl.NOMBRE_COMPLETO <> art.DATOSPERSONA inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'Bauta':
            return Artemisa.objects.raw(
                "select distinct * from CORE_ARTEMISA art inner join CLIENTE@infogesti cl on cl.NIT = art.NUMEROIDENTIDAD AND cl.UNIDAD = 2204 and art.DPA = 2204 AND cl.NOMBRE_COMPLETO <> art.DATOSPERSONA inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'Caimito':
            return Artemisa.objects.raw(
                "select distinct * from CORE_ARTEMISA art inner join CLIENTE@infogesti cl on cl.NIT = art.NUMEROIDENTIDAD AND cl.UNIDAD = 2205 and art.DPA = 2205 AND cl.NOMBRE_COMPLETO <> art.DATOSPERSONA inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'Candelaria':
            return Artemisa.objects.raw(
                "select distinct * from CORE_ARTEMISA art inner join CLIENTE@infogesti cl on cl.NIT = art.NUMEROIDENTIDAD AND cl.UNIDAD = 2206 and art.DPA = 2206 AND cl.NOMBRE_COMPLETO <> art.DATOSPERSONA inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'Guanajay':
            return Artemisa.objects.raw(
                "select distinct * from CORE_ARTEMISA art inner join CLIENTE@infogesti cl on cl.NIT = art.NUMEROIDENTIDAD AND cl.UNIDAD = 2207 and art.DPA = 2207 AND cl.NOMBRE_COMPLETO <> art.DATOSPERSONA inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'Gueira de Melena':
            return Artemisa.objects.raw(
                "select distinct * from CORE_ARTEMISA art inner join CLIENTE@infogesti cl on cl.NIT = art.NUMEROIDENTIDAD AND cl.UNIDAD = 2208 and art.DPA = 2208 AND cl.NOMBRE_COMPLETO <> art.DATOSPERSONA inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'Mariel':
            return Artemisa.objects.raw(
                "select distinct * from CORE_ARTEMISA art inner join CLIENTE@infogesti cl on cl.NIT = art.NUMEROIDENTIDAD AND cl.UNIDAD = 2209 and art.DPA = 2209 AND cl.NOMBRE_COMPLETO <> art.DATOSPERSONA inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'San Antonio de los Banos':
            return Artemisa.objects.raw(
                "select distinct * from CORE_ARTEMISA art inner join CLIENTE@infogesti cl on cl.NIT = art.NUMEROIDENTIDAD AND cl.UNIDAD = 2210 and art.DPA = 2210 AND cl.NOMBRE_COMPLETO <> art.DATOSPERSONA inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'San Cristobal':
            return Artemisa.objects.raw(
                "select distinct * from CORE_ARTEMISA art inner join CLIENTE@infogesti cl on cl.NIT = art.NUMEROIDENTIDAD AND cl.UNIDAD = 2211 and art.DPA = 2211 AND cl.NOMBRE_COMPLETO <> art.DATOSPERSONA inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")

    # 4 Contribuyentes totalmente coincidentes
    def resolve_contributors_with_equals_information_artemisa(self, info, city_name=graphene.String()):
        if city_name == 'Bahia Honda':
            return Artemisa.objects.raw(
                'select distinct * from CORE_ARTEMISA art INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON art.NUMEROIDENTIDAD =  info.NIT and DPA = 2201 WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT order  by NIT')
        if city_name == 'Alquizar':
            return Artemisa.objects.raw(
                'select distinct * from CORE_ARTEMISA art INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON art.NUMEROIDENTIDAD =  info.NIT and DPA = 2202 WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT order  by NIT')
        if city_name == 'Artemisa':
            return Artemisa.objects.raw(
                'select distinct * from CORE_ARTEMISA art INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON art.NUMEROIDENTIDAD =  info.NIT and DPA = 2203 WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT order  by NIT')
        if city_name == 'Bauta':
            return Artemisa.objects.raw(
                'select distinct * from CORE_ARTEMISA art INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON art.NUMEROIDENTIDAD =  info.NIT and DPA = 2204 WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT order  by NIT')
        if city_name == 'Caimito':
            return Artemisa.objects.raw(
                'select distinct * from CORE_ARTEMISA art INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON art.NUMEROIDENTIDAD =  info.NIT and DPA = 2205 WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT order  by NIT')
        if city_name == 'Candelaria':
            return Artemisa.objects.raw(
                'select distinct * from CORE_ARTEMISA art INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON art.NUMEROIDENTIDAD =  info.NIT and DPA = 2206 WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT order  by NIT')
        if city_name == 'Guanajay':
            return Artemisa.objects.raw(
                'select distinct * from CORE_ARTEMISA art INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON art.NUMEROIDENTIDAD =  info.NIT and DPA = 2207 WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT order  by NIT')
        if city_name == 'Gueira de Melena':
            return Artemisa.objects.raw(
                'select distinct * from CORE_ARTEMISA art INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON art.NUMEROIDENTIDAD =  info.NIT and DPA = 2208 WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT order  by NIT')
        if city_name == 'Mariel':
            return Artemisa.objects.raw(
                'select distinct * from CORE_ARTEMISA art INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON art.NUMEROIDENTIDAD =  info.NIT and DPA = 2209 WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT order  by NIT')
        if city_name == 'San Antonio de los Banos':
            return Artemisa.objects.raw(
                'select distinct * from CORE_ARTEMISA art INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON art.NUMEROIDENTIDAD =  info.NIT and DPA = 2210 WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT order  by NIT')
        if city_name == 'San Cristobal':
            return Artemisa.objects.raw(
                'select distinct * from CORE_ARTEMISA art INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON art.NUMEROIDENTIDAD =  info.NIT and DPA = 2211 WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT order  by NIT')


    def resolve_artemisa(self, info):
        return Artemisa.objects.all()


schema = graphene.Schema(query=ContributorsFromArtemisaQuery, auto_camelcase=False)
