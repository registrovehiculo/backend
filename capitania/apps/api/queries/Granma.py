import graphene
from capitania.apps.api.types.provincias import GranmaType, InfogestiContributorsType
from capitania.apps.core.models import Granma, InfogestiContributors


class ContributorsFromGranmaQuery(graphene.ObjectType):
    contributors_missing_in_onat_granma = graphene.List(GranmaType, city_name=graphene.String())
    contributors_with_different_information_granma = graphene.List(GranmaType, city_name=graphene.String())
    contributors_with_different_information_granma_infogesti = graphene.List(InfogestiContributorsType, city_name=graphene.String())
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
    def resolve_contributors_with_different_information_granma(self, info, city_name=graphene.String()):

        if city_name == 'Rio Cauto':
            return Granma.objects.raw(
                "select distinct * from CORE_GRANMA gm INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON gm.NUMEROIDENTIDAD = info.NIT  and info.UNIDAD = 3301 and DPA = 3301 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NUMEROIDENTIDAD")
        if city_name == 'Cauto Cristo':
            return Granma.objects.raw(
                "select distinct * from CORE_GRANMA gm INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON gm.NUMEROIDENTIDAD = info.NIT  and info.UNIDAD = 3302 and DPA = 3302 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NUMEROIDENTIDAD")
        if city_name == 'Jiguani':
            return Granma.objects.raw(
                "select distinct * from CORE_GRANMA gm INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON gm.NUMEROIDENTIDAD = info.NIT  and info.UNIDAD = 3303 and DPA = 3303 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NUMEROIDENTIDAD")
        if city_name == 'Bayamo':
            return Granma.objects.raw(
                "select distinct * from CORE_GRANMA gm INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON gm.NUMEROIDENTIDAD = info.NIT  and info.UNIDAD = 3304 and DPA = 3304 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NUMEROIDENTIDAD")
        if city_name == 'Yara':
            return Granma.objects.raw(
                "select distinct * from CORE_GRANMA gm INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON gm.NUMEROIDENTIDAD = info.NIT  and info.UNIDAD = 3305 and DPA = 3305 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NUMEROIDENTIDAD")
        if city_name == 'Manzanillo':
            return Granma.objects.raw(
                "select distinct * from CORE_GRANMA gm INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON gm.NUMEROIDENTIDAD = info.NIT  and info.UNIDAD = 3306 and DPA = 3306 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NUMEROIDENTIDAD")
        if city_name == 'Campechuela':
            return Granma.objects.raw(
                "select distinct * from CORE_GRANMA gm INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON gm.NUMEROIDENTIDAD = info.NIT  and info.UNIDAD = 3307 and DPA = 3307 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NUMEROIDENTIDAD")
        if city_name == 'Media Luna':
            return Granma.objects.raw(
                "select distinct * from CORE_GRANMA gm INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON gm.NUMEROIDENTIDAD = info.NIT  and info.UNIDAD = 3308 and DPA = 3308 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NUMEROIDENTIDAD")
        if city_name == 'Niquero':
            return Granma.objects.raw(
                "select distinct * from CORE_GRANMA gm INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON gm.NUMEROIDENTIDAD = info.NIT  and info.UNIDAD = 3309 and DPA = 3309 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NUMEROIDENTIDAD")
        if city_name == 'Pilon':
            return Granma.objects.raw(
                "select distinct * from CORE_GRANMA gm INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON gm.NUMEROIDENTIDAD = info.NIT  and info.UNIDAD = 3310 and DPA = 3310 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NUMEROIDENTIDAD")
        if city_name == 'Bartolome Maso':
            return Granma.objects.raw(
                "select distinct * from CORE_GRANMA gm INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON gm.NUMEROIDENTIDAD = info.NIT  and info.UNIDAD = 3311 and DPA = 3311 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NUMEROIDENTIDAD")
        if city_name == 'Buey Arriba':
            return Granma.objects.raw(
                "select distinct * from CORE_GRANMA gm INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON gm.NUMEROIDENTIDAD = info.NIT  and info.UNIDAD = 3312 and DPA = 3312 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NUMEROIDENTIDAD")
        if city_name == 'Guisa':
            return Granma.objects.raw(
                "select distinct * from CORE_GRANMA gm INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON gm.NUMEROIDENTIDAD = info.NIT  and info.UNIDAD = 3313 and DPA = 3313 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NUMEROIDENTIDAD")

    def resolve_contributors_with_different_information_granma_infogesti(self, info, city_name=graphene.String()):
        if city_name == 'Rio Cauto':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@infogesti info INNER JOIN CORE_GRANMA gm ON gm.NUMEROIDENTIDAD =  info.NIT and info.UNIDAD = 3301 and DPA = 3301 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NIT")
        if city_name == 'Cauto Cristo':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@infogesti info INNER JOIN CORE_GRANMA gm ON gm.NUMEROIDENTIDAD =  info.NIT and info.UNIDAD = 3302 and DPA = 3302 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NIT")
        if city_name == 'Jiguani':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@infogesti info INNER JOIN CORE_GRANMA gm ON gm.NUMEROIDENTIDAD =  info.NIT and info.UNIDAD = 3303 and DPA = 3303 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NIT")
        if city_name == 'Bayamo':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@infogesti info INNER JOIN CORE_GRANMA gm ON gm.NUMEROIDENTIDAD =  info.NIT and info.UNIDAD = 3304 and DPA = 3304 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NIT")
        if city_name == 'Yara':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@infogesti info INNER JOIN CORE_GRANMA gm ON gm.NUMEROIDENTIDAD =  info.NIT and info.UNIDAD = 3305 and DPA = 3305 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NIT")
        if city_name == 'Manzanillo':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@infogesti info INNER JOIN CORE_GRANMA gm ON gm.NUMEROIDENTIDAD =  info.NIT and info.UNIDAD = 3306 and DPA = 3306 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NIT")
        if city_name == 'Campechuela':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@infogesti info INNER JOIN CORE_GRANMA gm ON gm.NUMEROIDENTIDAD =  info.NIT and info.UNIDAD = 3307 and DPA = 3307 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NIT")
        if city_name == 'Media Luna':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@infogesti info INNER JOIN CORE_GRANMA gm ON gm.NUMEROIDENTIDAD =  info.NIT and info.UNIDAD = 3308 and DPA = 3308 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NIT")
        if city_name == 'Niquero':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@infogesti info INNER JOIN CORE_GRANMA gm ON gm.NUMEROIDENTIDAD =  info.NIT and info.UNIDAD = 3309 and DPA = 3309 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NIT")
        if city_name == 'Pilon':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@infogesti info INNER JOIN CORE_GRANMA gm ON gm.NUMEROIDENTIDAD =  info.NIT and info.UNIDAD = 3310 and DPA = 3310 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NIT")
        if city_name == 'Bartolome Maso':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@infogesti info INNER JOIN CORE_GRANMA gm ON gm.NUMEROIDENTIDAD =  info.NIT and info.UNIDAD = 3311 and DPA = 3311 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NIT")
        if city_name == 'Buey Arriba':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@infogesti info INNER JOIN CORE_GRANMA gm ON gm.NUMEROIDENTIDAD =  info.NIT and info.UNIDAD = 3312 and DPA = 3312 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NIT")
        if city_name == 'Guisa':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@infogesti info INNER JOIN CORE_GRANMA gm ON gm.NUMEROIDENTIDAD =  info.NIT and info.UNIDAD = 3313 and DPA = 3313 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NIT")

    # 4 Contribuyentes totalmente coincidentes
    def resolve_contributors_with_equals_information_granma(self, info, city_name=graphene.String()):
        if city_name == 'Rio Cauto':
            return Granma.objects.raw(
                'select distinct * from CORE_GRANMA gm INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON gm.NUMEROIDENTIDAD =  info.NIT and DPA = 3301 WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT order by NUMEROIDENTIDAD')
        if city_name == 'Cauto Cristo':
            return Granma.objects.raw(
                'select distinct * from CORE_GRANMA gm INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON gm.NUMEROIDENTIDAD =  info.NIT and DPA = 3302 WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT order by NUMEROIDENTIDAD')
        if city_name == 'Jiguani':
            return Granma.objects.raw(
                'select distinct * from CORE_GRANMA gm INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON gm.NUMEROIDENTIDAD =  info.NIT and DPA = 3303 WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT order by NUMEROIDENTIDAD')
        if city_name == 'Bayamo':
            return Granma.objects.raw(
                'select distinct * from CORE_GRANMA gm INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON gm.NUMEROIDENTIDAD =  info.NIT and DPA = 3304 WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT order by NUMEROIDENTIDAD')
        if city_name == 'Yara':
            return Granma.objects.raw(
                'select distinct * from CORE_GRANMA gm INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON gm.NUMEROIDENTIDAD =  info.NIT and DPA = 3305 WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT order by NUMEROIDENTIDAD')
        if city_name == 'Manzanillo':
            return Granma.objects.raw(
                'select distinct * from CORE_GRANMA gm INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON gm.NUMEROIDENTIDAD =  info.NIT and DPA = 3306 WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT order by NUMEROIDENTIDAD')
        if city_name == 'Campechuela':
            return Granma.objects.raw(
                'select distinct * from CORE_GRANMA gm INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON gm.NUMEROIDENTIDAD =  info.NIT and DPA = 3307 WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT order by NUMEROIDENTIDAD')
        if city_name == 'Media Luna':
            return Granma.objects.raw(
                'select distinct * from CORE_GRANMA gm INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON gm.NUMEROIDENTIDAD =  info.NIT and DPA = 3308 WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT order by NUMEROIDENTIDAD')
        if city_name == 'Niquero':
            return Granma.objects.raw(
                'select distinct * from CORE_GRANMA gm INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON gm.NUMEROIDENTIDAD =  info.NIT and DPA = 3309 WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT order by NUMEROIDENTIDAD')
        if city_name == 'Pilon':
            return Granma.objects.raw(
                'select distinct * from CORE_GRANMA gm INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON gm.NUMEROIDENTIDAD =  info.NIT and DPA = 3310 WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT order by NUMEROIDENTIDAD')
        if city_name == 'Bartolome Maso':
            return Granma.objects.raw(
                'select distinct * from CORE_GRANMA gm INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON gm.NUMEROIDENTIDAD =  info.NIT and DPA = 3311 WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT order by NUMEROIDENTIDAD')
        if city_name == 'Buey Arriba':
            return Granma.objects.raw(
                'select distinct * from CORE_GRANMA gm INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON gm.NUMEROIDENTIDAD =  info.NIT and DPA = 3312 WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT order by NUMEROIDENTIDAD')
        if city_name == 'Guisa':
            return Granma.objects.raw(
                'select distinct * from CORE_GRANMA gm INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON gm.NUMEROIDENTIDAD =  info.NIT and DPA = 3313 WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT order by NUMEROIDENTIDAD')


    def resolve_granma(self, info):
        return Granma.objects.all()


schema = graphene.Schema(query=ContributorsFromGranmaQuery, auto_camelcase=False)
