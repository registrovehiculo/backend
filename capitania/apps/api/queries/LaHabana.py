import graphene
from capitania.apps.api.types.provincias import LaHabanaType, InfogestiContributorsType
from capitania.apps.core.models import LaHabana, InfogestiContributors


class ContributorsFromLaHabanaQuery(graphene.ObjectType):
    contributors_missing_in_onat_la_habana = graphene.List(LaHabanaType, city_name=graphene.String())
    contributors_with_different_information_la_habana = graphene.List(LaHabanaType, city_name=graphene.String())
    contributors_with_different_information_la_habana_infogesti = graphene.List(InfogestiContributorsType, city_name=graphene.String())
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
    def resolve_contributors_with_different_information_la_habana(self, info, city_name=graphene.String()):
        if city_name == 'Playa':
            return LaHabana.objects.raw(
                "select distinct * from CORE_LAHABANA hab INNER JOIN IG_CONTRIBUYENTE_PN@INFOGESTI info ON hab.NUMEROIDENTIDAD =  info.NIT and UNIDAD = 2301 and DPA = 2301 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NUMEROIDENTIDAD")
        if city_name == 'Plaza De La Revolucion':
            return LaHabana.objects.raw(
                "select distinct * from CORE_LAHABANA hab INNER JOIN IG_CONTRIBUYENTE_PN@INFOGESTI info ON hab.NUMEROIDENTIDAD =  info.NIT and UNIDAD = 2302 and DPA = 2302 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NUMEROIDENTIDAD")
        if city_name == 'Centro Habana':
            return LaHabana.objects.raw(
                "select distinct * from CORE_LAHABANA hab INNER JOIN IG_CONTRIBUYENTE_PN@INFOGESTI info ON hab.NUMEROIDENTIDAD =  info.NIT and UNIDAD = 2303 and DPA = 2303 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NUMEROIDENTIDAD")
        if city_name == 'La Habana Vieja':
            return LaHabana.objects.raw(
                "select distinct * from CORE_LAHABANA hab INNER JOIN IG_CONTRIBUYENTE_PN@INFOGESTI info ON hab.NUMEROIDENTIDAD =  info.NIT and UNIDAD = 2304 and DPA = 2304 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NUMEROIDENTIDAD")
        if city_name == 'Regla':
            return LaHabana.objects.raw(
                "select distinct * from CORE_LAHABANA hab INNER JOIN IG_CONTRIBUYENTE_PN@INFOGESTI info ON hab.NUMEROIDENTIDAD =  info.NIT and UNIDAD = 2305 and DPA = 2305 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NUMEROIDENTIDAD")
        if city_name == 'La Habana Del Este':
            return LaHabana.objects.raw(
                "select distinct * from CORE_LAHABANA hab INNER JOIN IG_CONTRIBUYENTE_PN@INFOGESTI info ON hab.NUMEROIDENTIDAD =  info.NIT and UNIDAD = 2306 and DPA = 2306 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NUMEROIDENTIDAD")
        if city_name == 'Guanabacoa':
            return LaHabana.objects.raw(
                "select distinct * from CORE_LAHABANA hab INNER JOIN IG_CONTRIBUYENTE_PN@INFOGESTI info ON hab.NUMEROIDENTIDAD =  info.NIT and UNIDAD = 2307 and DPA = 2307 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NUMEROIDENTIDAD")
        if city_name == 'San Miguel Del Padron':
            return LaHabana.objects.raw(
                "select distinct * from CORE_LAHABANA hab INNER JOIN IG_CONTRIBUYENTE_PN@INFOGESTI info ON hab.NUMEROIDENTIDAD =  info.NIT and UNIDAD = 2308 and DPA = 2308 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NUMEROIDENTIDAD")
        if city_name == 'Diez De Octubre':
            return LaHabana.objects.raw(
                "select distinct * from CORE_LAHABANA hab INNER JOIN IG_CONTRIBUYENTE_PN@INFOGESTI info ON hab.NUMEROIDENTIDAD =  info.NIT and UNIDAD = 2309 and DPA = 2309 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NUMEROIDENTIDAD")
        if city_name == 'Cerro':
            return LaHabana.objects.raw(
                "select distinct * from CORE_LAHABANA hab INNER JOIN IG_CONTRIBUYENTE_PN@INFOGESTI info ON hab.NUMEROIDENTIDAD =  info.NIT and UNIDAD = 2310 and DPA = 2310 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NUMEROIDENTIDAD")
        if city_name == 'Marianao':
            return LaHabana.objects.raw(
                "select distinct * from CORE_LAHABANA hab INNER JOIN IG_CONTRIBUYENTE_PN@INFOGESTI info ON hab.NUMEROIDENTIDAD =  info.NIT and UNIDAD = 2311 and DPA = 2311 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NUMEROIDENTIDAD")
        if city_name == 'La Lisa':
            return LaHabana.objects.raw(
                "select distinct * from CORE_LAHABANA hab INNER JOIN IG_CONTRIBUYENTE_PN@INFOGESTI info ON hab.NUMEROIDENTIDAD =  info.NIT and UNIDAD = 2312 and DPA = 2312 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NUMEROIDENTIDAD")
        if city_name == 'Boyeros':
            return LaHabana.objects.raw(
                "select distinct * from CORE_LAHABANA hab INNER JOIN IG_CONTRIBUYENTE_PN@INFOGESTI info ON hab.NUMEROIDENTIDAD =  info.NIT and UNIDAD = 2313 and DPA = 2313 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NUMEROIDENTIDAD")
        if city_name == 'Arroyo Naranjo':
            return LaHabana.objects.raw(
                "select distinct * from CORE_LAHABANA hab INNER JOIN IG_CONTRIBUYENTE_PN@INFOGESTI info ON hab.NUMEROIDENTIDAD =  info.NIT and UNIDAD = 2314 and DPA = 2314 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NUMEROIDENTIDAD")
        if city_name == 'Cotorro':
            return LaHabana.objects.raw(
                "select distinct * from CORE_LAHABANA hab INNER JOIN IG_CONTRIBUYENTE_PN@INFOGESTI info ON hab.NUMEROIDENTIDAD =  info.NIT and UNIDAD = 2315 and DPA = 2315 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NUMEROIDENTIDAD")


    def resolve_contributors_with_different_information_la_habana_infogesti(self, info, city_name=graphene.String()):
        if city_name == 'Playa':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@INFOGESTI info INNER JOIN CORE_LAHABANA hab ON hab.NUMEROIDENTIDAD =  info.NIT and UNIDAD = 2301 and DPA = 2301 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NIT")
        if city_name == 'Plaza De La Revolucion':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@INFOGESTI info INNER JOIN CORE_LAHABANA hab ON hab.NUMEROIDENTIDAD =  info.NIT and UNIDAD = 2302 and DPA = 2302 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NIT")
        if city_name == 'Centro Habana':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@INFOGESTI info INNER JOIN CORE_LAHABANA hab ON hab.NUMEROIDENTIDAD =  info.NIT and UNIDAD = 2303 and DPA = 2303 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NIT")
        if city_name == 'La Habana Vieja':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@INFOGESTI info INNER JOIN CORE_LAHABANA hab ON hab.NUMEROIDENTIDAD =  info.NIT and UNIDAD = 2304 and DPA = 2304 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NIT")
        if city_name == 'Regla':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@INFOGESTI info INNER JOIN CORE_LAHABANA hab ON hab.NUMEROIDENTIDAD =  info.NIT and UNIDAD = 2305 and DPA = 2305 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NIT")
        if city_name == 'La Habana Del Este':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@INFOGESTI info INNER JOIN CORE_LAHABANA hab ON hab.NUMEROIDENTIDAD =  info.NIT and UNIDAD = 2306 and DPA = 2306 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NIT")
        if city_name == 'Guanabacoa':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@INFOGESTI info INNER JOIN CORE_LAHABANA hab ON hab.NUMEROIDENTIDAD =  info.NIT and UNIDAD = 2307 and DPA = 2307 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NIT")
        if city_name == 'San Miguel Del Padron':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@INFOGESTI info INNER JOIN CORE_LAHABANA hab ON hab.NUMEROIDENTIDAD =  info.NIT and UNIDAD = 2308 and DPA = 2308 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NIT")
        if city_name == 'Diez De Octubre':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@INFOGESTI info INNER JOIN CORE_LAHABANA hab ON hab.NUMEROIDENTIDAD =  info.NIT and UNIDAD = 2309 and DPA = 2309 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NIT")
        if city_name == 'Cerro':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@INFOGESTI info INNER JOIN CORE_LAHABANA hab ON hab.NUMEROIDENTIDAD =  info.NIT and UNIDAD = 2310 and DPA = 2310 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NIT")
        if city_name == 'Marianao':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@INFOGESTI info INNER JOIN CORE_LAHABANA hab ON hab.NUMEROIDENTIDAD =  info.NIT and UNIDAD = 2311 and DPA = 2311 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NIT")
        if city_name == 'La Lisa':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@INFOGESTI info INNER JOIN CORE_LAHABANA hab ON hab.NUMEROIDENTIDAD =  info.NIT and UNIDAD = 2312 and DPA = 2312 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NIT")
        if city_name == 'Boyeros':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@INFOGESTI info INNER JOIN CORE_LAHABANA hab ON hab.NUMEROIDENTIDAD =  info.NIT and UNIDAD = 2313 and DPA = 2313 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NIT")
        if city_name == 'Arroyo Naranjo':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@INFOGESTI info INNER JOIN CORE_LAHABANA hab ON hab.NUMEROIDENTIDAD =  info.NIT and UNIDAD = 2314 and DPA = 2314 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NIT")
        if city_name == 'Cotorro':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@INFOGESTI info INNER JOIN CORE_LAHABANA hab ON hab.NUMEROIDENTIDAD =  info.NIT and UNIDAD = 2315 and DPA = 2315 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NIT")


    # 4 Contribuyentes totalmente coincidentes
    def resolve_contributors_with_equals_information_la_habana(self, info, city_name=graphene.String()):
        if city_name == 'Playa':
            return LaHabana.objects.raw(
                'select distinct * from CORE_LAHABANA hab INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON hab.NUMEROIDENTIDAD =  info.NIT and DPA = 2301 WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT')
        if city_name == 'Plaza De La Revolucion':
            return LaHabana.objects.raw(
                'select distinct * from CORE_LAHABANA hab INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON hab.NUMEROIDENTIDAD =  info.NIT and DPA = 2302 WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT')
        if city_name == 'Centro Habana':
            return LaHabana.objects.raw(
                'select distinct * from CORE_LAHABANA hab INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON hab.NUMEROIDENTIDAD =  info.NIT and DPA = 2303 WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT')
        if city_name == 'La Habana Vieja':
            return LaHabana.objects.raw(
                'select distinct * from CORE_LAHABANA hab INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON hab.NUMEROIDENTIDAD =  info.NIT and DPA = 2304 WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT')
        if city_name == 'Regla':
            return LaHabana.objects.raw(
                'select distinct * from CORE_LAHABANA hab INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON hab.NUMEROIDENTIDAD =  info.NIT and DPA = 2305 WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT')
        if city_name == 'La Habana Del Este':
            return LaHabana.objects.raw(
                'select distinct * from CORE_LAHABANA hab INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON hab.NUMEROIDENTIDAD =  info.NIT and DPA = 2306 WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT')
        if city_name == 'Guanabacoa':
            return LaHabana.objects.raw(
                'select distinct * from CORE_LAHABANA hab INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON hab.NUMEROIDENTIDAD =  info.NIT and DPA = 2307 WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT')
        if city_name == 'San Miguel Del Padron':
            return LaHabana.objects.raw(
                'select distinct * from CORE_LAHABANA hab INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON hab.NUMEROIDENTIDAD =  info.NIT and DPA = 2308 WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT')
        if city_name == 'Diez De Octubre':
            return LaHabana.objects.raw(
                'select distinct * from CORE_LAHABANA hab INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON hab.NUMEROIDENTIDAD =  info.NIT and DPA = 2309 WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT')
        if city_name == 'Cerro':
            return LaHabana.objects.raw(
                'select distinct * from CORE_LAHABANA hab INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON hab.NUMEROIDENTIDAD =  info.NIT and DPA = 2310 WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT')
        if city_name == 'Marianao':
            return LaHabana.objects.raw(
                'select distinct * from CORE_LAHABANA hab INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON hab.NUMEROIDENTIDAD =  info.NIT and DPA = 2311 WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT')
        if city_name == 'La Lisa':
            return LaHabana.objects.raw(
                'select distinct * from CORE_LAHABANA hab INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON hab.NUMEROIDENTIDAD =  info.NIT and DPA = 2312 WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT')
        if city_name == 'Boyeros':
            return LaHabana.objects.raw(
                'select distinct * from CORE_LAHABANA hab INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON hab.NUMEROIDENTIDAD =  info.NIT and DPA = 2313 WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT')
        if city_name == 'Arroyo Naranjo':
            return LaHabana.objects.raw(
                'select distinct * from CORE_LAHABANA hab INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON hab.NUMEROIDENTIDAD =  info.NIT and DPA = 2314 WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT')
        if city_name == 'Cotorro':
            return LaHabana.objects.raw(
                'select distinct * from CORE_LAHABANA hab INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON hab.NUMEROIDENTIDAD =  info.NIT and DPA = 2315 WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT')


    def resolve_la_habana(self, info):
        return LaHabana.objects.all()


schema = graphene.Schema(query=ContributorsFromLaHabanaQuery, auto_camelcase=False)
