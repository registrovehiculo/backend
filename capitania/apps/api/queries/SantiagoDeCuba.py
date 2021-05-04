import graphene
from capitania.apps.api.types.provincias import SantiagoDeCubaType, SantiagoDeCubaType
from capitania.apps.core.models import SantiagoDeCuba, SantiagoDeCuba


class ContributorsFromSantiagoDeCubaQuery(graphene.ObjectType):
    contributors_missing_in_onat_santiago_de_cuba = graphene.List(SantiagoDeCubaType, city_name=graphene.String())
    contributors_with_different_information_santiago_de_cuba_plate = graphene.List(SantiagoDeCubaType, city_name=graphene.String())
    contributors_with_different_information_santiago_de_cuba_name = graphene.List(SantiagoDeCubaType, city_name=graphene.String())
    contributors_with_equals_information_santiago_de_cuba = graphene.List(SantiagoDeCubaType, city_name=graphene.String())
    santiago_de_cuba = graphene.List(SantiagoDeCubaType)

    # 1 Contribuyentes que estan en capitania vehiculo que no estan en la onat
    def resolve_contributors_missing_in_onat_santiago_de_cuba(self, info, city_name=graphene.String()):

        if city_name == 'Contramaestre':
            return SantiagoDeCuba.objects.raw(
                'select distinct * from CORE_SANTIAGODECUBA s LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON s.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 3401')
        if city_name == 'Mella':
            return SantiagoDeCuba.objects.raw(
                'select distinct * from CORE_SANTIAGODECUBA s LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON s.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 3402')
        if city_name == 'San Luis':
            return SantiagoDeCuba.objects.raw(
                'select distinct * from CORE_SANTIAGODECUBA s LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON s.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 3403')
        if city_name == 'Segundo Frente':
            return SantiagoDeCuba.objects.raw(
                'select distinct * from CORE_SANTIAGODECUBA s LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON s.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 3404')
        if city_name == 'Songo - La Maya':
            return SantiagoDeCuba.objects.raw(
                'select distinct * from CORE_SANTIAGODECUBA s LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON s.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 3405')
        if city_name == 'Santiago de Cuba':
            return SantiagoDeCuba.objects.raw(
                'select distinct * from CORE_SANTIAGODECUBA s LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON s.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 3406')
        if city_name == 'Palma Soriano':
            return SantiagoDeCuba.objects.raw(
                'select distinct * from CORE_SANTIAGODECUBA s LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON s.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 3407')
        if city_name == 'Tercer Frente':
            return SantiagoDeCuba.objects.raw(
                'select distinct * from CORE_SANTIAGODECUBA s LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON s.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 3408')
        if city_name == 'Guamá':
            return SantiagoDeCuba.objects.raw(
                'select distinct * from CORE_SANTIAGODECUBA s LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON s.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 3409')



    # 2 Contribuyentes que estan en ambos capitania con informaciones diferentes
    def resolve_contributors_with_different_information_santiago_de_cuba_plate(self, info, city_name=graphene.String()):

        if city_name == 'Contramaestre':
            return SantiagoDeCuba.objects.raw(
                "select distinct * from CORE_SANTIAGODECUBA h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 3401 and h.DPA = 3401 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> h.CHAPANUEVA")
        if city_name == 'Mella':
            return SantiagoDeCuba.objects.raw(
                "select distinct * from CORE_SANTIAGODECUBA h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 3402 and h.DPA = 3402 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> h.CHAPANUEVA")
        if city_name == 'San Luis':
            return SantiagoDeCuba.objects.raw(
                "select distinct * from CORE_SANTIAGODECUBA h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 3403 and h.DPA = 3403 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> h.CHAPANUEVA")
        if city_name == 'Segundo Frente':
            return SantiagoDeCuba.objects.raw(
                "select distinct * from CORE_SANTIAGODECUBA h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 3404 and h.DPA = 3404 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> h.CHAPANUEVA")
        if city_name == 'Songo - La Maya':
            return SantiagoDeCuba.objects.raw(
                "select distinct * from CORE_SANTIAGODECUBA h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 3405 and h.DPA = 3405 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> h.CHAPANUEVA")
        if city_name == 'Santiago de Cuba':
            return SantiagoDeCuba.objects.raw(
                "select distinct * from CORE_SANTIAGODECUBA h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 3406 and h.DPA = 3406 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> h.CHAPANUEVA")
        if city_name == 'Palma Soriano':
            return SantiagoDeCuba.objects.raw(
                "select distinct * from CORE_SANTIAGODECUBA h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 3407 and h.DPA = 3407 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> h.CHAPANUEVA")
        if city_name == 'Tercer Frente':
            return SantiagoDeCuba.objects.raw(
                "select distinct * from CORE_SANTIAGODECUBA h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 3408 and h.DPA = 3408 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> h.CHAPANUEVA")
        if city_name == 'Guamá':
            return SantiagoDeCuba.objects.raw(
                "select distinct * from CORE_SANTIAGODECUBA h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 3409 and h.DPA = 3409 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> h.CHAPANUEVA")

    def resolve_contributors_with_different_information_santiago_de_cuba_name(self, info, city_name=graphene.String()):

        if city_name == 'Contramaestre':
            return SantiagoDeCuba.objects.raw(
                "select distinct * from CORE_SANTIAGODECUBA h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 3401 and h.DPA = 3401 AND cl.NOMBRE_COMPLETO <> h.DATOSPERSONA inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'Mella':
            return SantiagoDeCuba.objects.raw(
                "select distinct * from CORE_SANTIAGODECUBA h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 3402 and h.DPA = 3402 AND cl.NOMBRE_COMPLETO <> h.DATOSPERSONA inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'San Luis':
            return SantiagoDeCuba.objects.raw(
                "select distinct * from CORE_SANTIAGODECUBA h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 3403 and h.DPA = 3403 AND cl.NOMBRE_COMPLETO <> h.DATOSPERSONA inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'Segundo Frente':
            return SantiagoDeCuba.objects.raw(
                "select distinct * from CORE_SANTIAGODECUBA h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 3404 and h.DPA = 3404 AND cl.NOMBRE_COMPLETO <> h.DATOSPERSONA inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'Songo - La Maya':
            return SantiagoDeCuba.objects.raw(
                "select distinct * from CORE_SANTIAGODECUBA h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 3405 and h.DPA = 3405 AND cl.NOMBRE_COMPLETO <> h.DATOSPERSONA inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'Santiago de Cuba':
            return SantiagoDeCuba.objects.raw(
                "select distinct * from CORE_SANTIAGODECUBA h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 3406 and h.DPA = 3406 AND cl.NOMBRE_COMPLETO <> h.DATOSPERSONA inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'Palma Soriano':
            return SantiagoDeCuba.objects.raw(
                "select distinct * from CORE_SANTIAGODECUBA h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 3407 and h.DPA = 3407 AND cl.NOMBRE_COMPLETO <> h.DATOSPERSONA inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'Tercer Frente':
            return SantiagoDeCuba.objects.raw(
                "select distinct * from CORE_SANTIAGODECUBA h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 3408 and h.DPA = 3408 AND cl.NOMBRE_COMPLETO <> h.DATOSPERSONA inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'Guamá':
            return SantiagoDeCuba.objects.raw(
                "select distinct * from CORE_SANTIAGODECUBA h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 3409 and h.DPA = 3409 AND cl.NOMBRE_COMPLETO <> h.DATOSPERSONA inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")

    # 4 Contribuyentes totalmente coincidentes
    def resolve_contributors_with_equals_information_santiago_de_cuba(self, info, city_name=graphene.String()):

        if city_name == 'Contramaestre':
            return SantiagoDeCuba.objects.raw(
                'select distinct * from CORE_SANTIAGODECUBA s INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON s.NUMEROIDENTIDAD =  info.NIT WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT and DPA = 3401 order by NUMEROIDENTIDAD')
        if city_name == 'Mella':
            return SantiagoDeCuba.objects.raw(
                'select distinct * from CORE_SANTIAGODECUBA s INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON s.NUMEROIDENTIDAD =  info.NIT WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT and DPA = 3402 order by NUMEROIDENTIDAD')
        if city_name == 'San Luis':
            return SantiagoDeCuba.objects.raw(
                'select distinct * from CORE_SANTIAGODECUBA s INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON s.NUMEROIDENTIDAD =  info.NIT WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT and DPA = 3403 order by NUMEROIDENTIDAD')
        if city_name == 'Segundo Frente':
            return SantiagoDeCuba.objects.raw(
                'select distinct * from CORE_SANTIAGODECUBA s INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON s.NUMEROIDENTIDAD =  info.NIT WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT and DPA = 3404 order by NUMEROIDENTIDAD')
        if city_name == 'Songo - La Maya':
            return SantiagoDeCuba.objects.raw(
                'select distinct * from CORE_SANTIAGODECUBA s INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON s.NUMEROIDENTIDAD =  info.NIT WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT and DPA = 3405 order by NUMEROIDENTIDAD')
        if city_name == 'Santiago de Cuba':
            return SantiagoDeCuba.objects.raw(
                'select distinct * from CORE_SANTIAGODECUBA s INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON s.NUMEROIDENTIDAD =  info.NIT WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT and DPA = 3406 order by NUMEROIDENTIDAD')
        if city_name == 'Palma Soriano':
            return SantiagoDeCuba.objects.raw(
                'select distinct * from CORE_SANTIAGODECUBA s INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON s.NUMEROIDENTIDAD =  info.NIT WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT and DPA = 3407 order by NUMEROIDENTIDAD')
        if city_name == 'Tercer Frente':
            return SantiagoDeCuba.objects.raw(
                'select distinct * from CORE_SANTIAGODECUBA s INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON s.NUMEROIDENTIDAD =  info.NIT WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT and DPA = 3408 order by NUMEROIDENTIDAD')
        if city_name == 'Guamá':
            return SantiagoDeCuba.objects.raw(
                'select distinct * from CORE_SANTIAGODECUBA s INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON s.NUMEROIDENTIDAD =  info.NIT WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT and DPA = 3409 order by NUMEROIDENTIDAD')

    def resolve_santiago_de_cuba(self, info):
        return SantiagoDeCuba.objects.all()


schema = graphene.Schema(query=ContributorsFromSantiagoDeCubaQuery, auto_camelcase=False)
