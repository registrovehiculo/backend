import graphene
from capitania.apps.api.types.provincias import SantiagoDeCubaType, InfogestiContributorsType
from capitania.apps.core.models import SantiagoDeCuba, InfogestiContributors


class ContributorsFromSantiagoDeCubaQuery(graphene.ObjectType):
    contributors_missing_in_onat_santiago_de_cuba = graphene.List(SantiagoDeCubaType, city_name=graphene.String())
    contributors_with_different_information_santiago_de_cuba = graphene.List(SantiagoDeCubaType, city_name=graphene.String())
    contributors_with_different_information_santiago_de_cuba_infogesti = graphene.List(InfogestiContributorsType, city_name=graphene.String())
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
    def resolve_contributors_with_different_information_santiago_de_cuba(self, info, city_name=graphene.String()):

        if city_name == 'Contramaestre':
            return SantiagoDeCuba.objects.raw(
                "select distinct * from CORE_SANTIAGODECUBA s LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON s.NUMEROIDENTIDAD =  info.NIT  and info.ES_PROPIETARIO_TT = '1' and UNIDAD = 3401 and DPA = 3401 WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NUMEROIDENTIDAD")
        if city_name == 'Mella':
            return SantiagoDeCuba.objects.raw(
                "select distinct * from CORE_SANTIAGODECUBA s LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON s.NUMEROIDENTIDAD =  info.NIT  and info.ES_PROPIETARIO_TT = '1' and UNIDAD = 3402 and DPA = 3402 WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NUMEROIDENTIDAD")
        if city_name == 'San Luis':
            return SantiagoDeCuba.objects.raw(
                "select distinct * from CORE_SANTIAGODECUBA s LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON s.NUMEROIDENTIDAD =  info.NIT  and info.ES_PROPIETARIO_TT = '1' and UNIDAD = 3403 and DPA = 3403 WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NUMEROIDENTIDAD")
        if city_name == 'Segundo Frente':
            return SantiagoDeCuba.objects.raw(
                "select distinct * from CORE_SANTIAGODECUBA s LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON s.NUMEROIDENTIDAD =  info.NIT  and info.ES_PROPIETARIO_TT = '1' and UNIDAD = 3404 and DPA = 3404 WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NUMEROIDENTIDAD")
        if city_name == 'Songo - La Maya':
            return SantiagoDeCuba.objects.raw(
                "select distinct * from CORE_SANTIAGODECUBA s LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON s.NUMEROIDENTIDAD =  info.NIT  and info.ES_PROPIETARIO_TT = '1' and UNIDAD = 3405 and DPA = 3405 WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NUMEROIDENTIDAD")
        if city_name == 'Santiago de Cuba':
            return SantiagoDeCuba.objects.raw(
                "select distinct * from CORE_SANTIAGODECUBA s LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON s.NUMEROIDENTIDAD =  info.NIT  and info.ES_PROPIETARIO_TT = '1' and UNIDAD = 3406 and DPA = 3406 WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NUMEROIDENTIDAD")
        if city_name == 'Palma Soriano':
            return SantiagoDeCuba.objects.raw(
                "select distinct * from CORE_SANTIAGODECUBA s LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON s.NUMEROIDENTIDAD =  info.NIT  and info.ES_PROPIETARIO_TT = '1' and UNIDAD = 3407 and DPA = 3407 WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NUMEROIDENTIDAD")
        if city_name == 'Tercer Frente':
            return SantiagoDeCuba.objects.raw(
                "select distinct * from CORE_SANTIAGODECUBA s LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON s.NUMEROIDENTIDAD =  info.NIT  and info.ES_PROPIETARIO_TT = '1' and UNIDAD = 3408 and DPA = 3408 WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NUMEROIDENTIDAD")
        if city_name == 'Guamá':
            return SantiagoDeCuba.objects.raw(
                "select distinct * from CORE_SANTIAGODECUBA s LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON s.NUMEROIDENTIDAD =  info.NIT  and info.ES_PROPIETARIO_TT = '1' and UNIDAD = 3409 and DPA = 3409 WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NUMEROIDENTIDAD")

    def resolve_contributors_with_different_information_santiago_de_cuba_infogesti(self, info, city_name=graphene.String()):

        if city_name == 'Contramaestre':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@infogesti info INNER JOIN CORE_SANTIAGODECUBA s ON s.NUMEROIDENTIDAD =  info.NIT and UNIDAD = 3401 and info.ES_PROPIETARIO_TT = '1'WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NIT")
        if city_name == 'Mella':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@infogesti info INNER JOIN CORE_SANTIAGODECUBA s ON s.NUMEROIDENTIDAD =  info.NIT and UNIDAD = 3402 and info.ES_PROPIETARIO_TT = '1'WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NIT")
        if city_name == 'San Luis':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@infogesti info INNER JOIN CORE_SANTIAGODECUBA s ON s.NUMEROIDENTIDAD =  info.NIT and UNIDAD = 3403 and info.ES_PROPIETARIO_TT = '1'WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NIT")
        if city_name == 'Segundo Frente':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@infogesti info INNER JOIN CORE_SANTIAGODECUBA s ON s.NUMEROIDENTIDAD =  info.NIT and UNIDAD = 3404 and info.ES_PROPIETARIO_TT = '1'WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NIT")
        if city_name == 'Songo - La Maya':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@infogesti info INNER JOIN CORE_SANTIAGODECUBA s ON s.NUMEROIDENTIDAD =  info.NIT and UNIDAD = 3405 and info.ES_PROPIETARIO_TT = '1'WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NIT")
        if city_name == 'Santiago de Cuba':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@infogesti info INNER JOIN CORE_SANTIAGODECUBA s ON s.NUMEROIDENTIDAD =  info.NIT and UNIDAD = 3406 and info.ES_PROPIETARIO_TT = '1'WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NIT")
        if city_name == 'Palma Soriano':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@infogesti info INNER JOIN CORE_SANTIAGODECUBA s ON s.NUMEROIDENTIDAD =  info.NIT and UNIDAD = 3407 and info.ES_PROPIETARIO_TT = '1'WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NIT")
        if city_name == 'Tercer Frente':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@infogesti info INNER JOIN CORE_SANTIAGODECUBA s ON s.NUMEROIDENTIDAD =  info.NIT and UNIDAD = 3408 and info.ES_PROPIETARIO_TT = '1'WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NIT")
        if city_name == 'Guamá':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@infogesti info INNER JOIN CORE_SANTIAGODECUBA s ON s.NUMEROIDENTIDAD =  info.NIT and UNIDAD = 3409 and info.ES_PROPIETARIO_TT = '1'WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NIT")

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
