import graphene
from capitania.apps.api.types.provincias import LasTunasType, InfogestiContributorsType
from capitania.apps.core.models import LasTunas, InfogestiContributors


class ContributorsFromLasTunasQuery(graphene.ObjectType):
    contributors_missing_in_onat_las_tunas = graphene.List(LasTunasType, city_name=graphene.String())
    contributors_with_different_information_las_tunas = graphene.List(LasTunasType, city_name=graphene.String())
    contributors_with_different_information_las_tunas_infogesti = graphene.List(InfogestiContributorsType, city_name=graphene.String())
    contributors_with_equals_information_las_tunas = graphene.List(LasTunasType, city_name=graphene.String())
    las_tunas = graphene.List(LasTunasType)

    # 1 Contribuyentes que estan en capitania vehiculo que no estan en la onat
    def resolve_contributors_missing_in_onat_las_tunas(self, info, city_name=graphene.String()):
        if city_name == 'Manati':
            return LasTunas.objects.raw(
                'select distinct * from RECA.CORE_LASTUNAS l LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON l.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 3101')
        if city_name == 'Puerto Padre':
            return LasTunas.objects.raw(
                'select distinct * from RECA.CORE_LASTUNAS l LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON l.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 3102')
        if city_name == 'Jesus Menendez':
            return LasTunas.objects.raw(
                'select distinct * from RECA.CORE_LASTUNAS l LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON l.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 3103')
        if city_name == 'Majibacoa':
            return LasTunas.objects.raw(
                'select distinct * from RECA.CORE_LASTUNAS l LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON l.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 3104')
        if city_name == 'Las Tunas':
            return LasTunas.objects.raw(
                'select distinct * from RECA.CORE_LASTUNAS l LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON l.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 3105')
        if city_name == 'Jobabo':
            return LasTunas.objects.raw(
                'select distinct * from RECA.CORE_LASTUNAS l LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON l.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 3106')
        if city_name == 'Colombia':
            return LasTunas.objects.raw(
                'select distinct * from RECA.CORE_LASTUNAS l LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON l.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 3107')
        if city_name == 'Amancio':
            return LasTunas.objects.raw(
                'select distinct * from RECA.CORE_LASTUNAS l LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON l.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 3108')

    # 2 Contribuyentes que estan en ambos capitania con informaciones diferentes
    def resolve_contributors_with_different_information_las_tunas(self, info, city_name=graphene.String()):
        if city_name == 'Manati':
            return LasTunas.objects.raw(
                "select distinct * from RECA.CORE_LASTUNAS l INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON l.NUMEROIDENTIDAD =  info.NIT and info.ES_PROPIETARIO_TT = '1' and DPA = 3101 and UNIDAD = 3101 WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT  order by NUMEROIDENTIDAD")
        if city_name == 'Puerto Padre':
            return LasTunas.objects.raw(
                "select distinct * from RECA.CORE_LASTUNAS l INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON l.NUMEROIDENTIDAD =  info.NIT and info.ES_PROPIETARIO_TT = '1' and DPA = 3102 and UNIDAD = 3102 WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT  order by NUMEROIDENTIDAD")
        if city_name == 'Jesus Menendez':
            return LasTunas.objects.raw(
                "select distinct * from RECA.CORE_LASTUNAS l INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON l.NUMEROIDENTIDAD =  info.NIT and info.ES_PROPIETARIO_TT = '1' and DPA = 3103 and UNIDAD = 3103 WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT  order by NUMEROIDENTIDAD")
        if city_name == 'Majibacoa':
            return LasTunas.objects.raw(
                "select distinct * from RECA.CORE_LASTUNAS l INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON l.NUMEROIDENTIDAD =  info.NIT and info.ES_PROPIETARIO_TT = '1' and DPA = 3104 and UNIDAD = 3104 WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT  order by NUMEROIDENTIDAD")
        if city_name == 'Las Tunas':
            return LasTunas.objects.raw(
                "select distinct * from RECA.CORE_LASTUNAS l INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON l.NUMEROIDENTIDAD =  info.NIT and info.ES_PROPIETARIO_TT = '1' and DPA = 3105 and UNIDAD = 3105 WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT  order by NUMEROIDENTIDAD")
        if city_name == 'Jobabo':
            return LasTunas.objects.raw(
                "select distinct * from RECA.CORE_LASTUNAS l INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON l.NUMEROIDENTIDAD =  info.NIT and info.ES_PROPIETARIO_TT = '1' and DPA = 3106 and UNIDAD = 3106 WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT  order by NUMEROIDENTIDAD")
        if city_name == 'Colombia':
            return LasTunas.objects.raw(
                "select distinct * from RECA.CORE_LASTUNAS l INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON l.NUMEROIDENTIDAD =  info.NIT and info.ES_PROPIETARIO_TT = '1' and DPA = 3107 and UNIDAD = 3107 WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT  order by NUMEROIDENTIDAD")
        if city_name == 'Amancio':
            return LasTunas.objects.raw(
                "select distinct * from RECA.CORE_LASTUNAS l INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON l.NUMEROIDENTIDAD =  info.NIT and info.ES_PROPIETARIO_TT = '1' and DPA = 3108 and UNIDAD = 3108 WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT  order by NUMEROIDENTIDAD")


    def resolve_contributors_with_different_information_las_tunas_infogesti(self, info, city_name=graphene.String()):
        if city_name == 'Manati':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@infogesti info INNER JOIN RECA.CORE_LASTUNAS l ON l.NUMEROIDENTIDAD =  info.NIT and UNIDAD = 3101 and DPA = 3101 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NIT")
        if city_name == 'Puerto Padre':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@infogesti info INNER JOIN RECA.CORE_LASTUNAS l ON l.NUMEROIDENTIDAD =  info.NIT and UNIDAD = 3102 and DPA = 3102 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NIT")
        if city_name == 'Jesus Menendez':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@infogesti info INNER JOIN RECA.CORE_LASTUNAS l ON l.NUMEROIDENTIDAD =  info.NIT and UNIDAD = 3103 and DPA = 3103 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NIT")
        if city_name == 'Majibacoa':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@infogesti info INNER JOIN RECA.CORE_LASTUNAS l ON l.NUMEROIDENTIDAD =  info.NIT and UNIDAD = 3104 and DPA = 3104 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NIT")
        if city_name == 'Las Tunas':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@infogesti info INNER JOIN RECA.CORE_LASTUNAS l ON l.NUMEROIDENTIDAD =  info.NIT and UNIDAD = 3105 and DPA = 3105 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NIT")
        if city_name == 'Jobabo':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@infogesti info INNER JOIN RECA.CORE_LASTUNAS l ON l.NUMEROIDENTIDAD =  info.NIT and UNIDAD = 3106 and DPA = 3106 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NIT")
        if city_name == 'Colombia':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@infogesti info INNER JOIN RECA.CORE_LASTUNAS l ON l.NUMEROIDENTIDAD =  info.NIT and UNIDAD = 3107 and DPA = 3107 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NIT")
        if city_name == 'Amancio':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@infogesti info INNER JOIN RECA.CORE_LASTUNAS l ON l.NUMEROIDENTIDAD =  info.NIT and UNIDAD = 3108 and DPA = 3108 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NIT")

    # 4 Contribuyentes totalmente coincidentes
    def resolve_contributors_with_equals_information_las_tunas(self, info, city_name=graphene.String()):
        if city_name == 'Manati':
            return LasTunas.objects.raw(
                'select distinct * from RECA.CORE_LASTUNAS l INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON l.NUMEROIDENTIDAD =  info.NIT WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT and DPA = 3101 order by NUMEROIDENTIDAD')
        if city_name == 'Puerto Padre':
            return LasTunas.objects.raw(
                'select distinct * from RECA.CORE_LASTUNAS l INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON l.NUMEROIDENTIDAD =  info.NIT WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT and DPA = 3102 order by NUMEROIDENTIDAD')
        if city_name == 'Jesus Menendez':
            return LasTunas.objects.raw(
                'select distinct * from RECA.CORE_LASTUNAS l INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON l.NUMEROIDENTIDAD =  info.NIT WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT and DPA = 3103 order by NUMEROIDENTIDAD')
        if city_name == 'Majibacoa':
            return LasTunas.objects.raw(
                'select distinct * from RECA.CORE_LASTUNAS l INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON l.NUMEROIDENTIDAD =  info.NIT WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT and DPA = 3104 order by NUMEROIDENTIDAD')
        if city_name == 'Las Tunas':
            return LasTunas.objects.raw(
                'select distinct * from RECA.CORE_LASTUNAS l INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON l.NUMEROIDENTIDAD =  info.NIT WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT and DPA = 3105 order by NUMEROIDENTIDAD')
        if city_name == 'Jobabo':
            return LasTunas.objects.raw(
                'select distinct * from RECA.CORE_LASTUNAS l INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON l.NUMEROIDENTIDAD =  info.NIT WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT and DPA = 3106 order by NUMEROIDENTIDAD')
        if city_name == 'Colombia':
            return LasTunas.objects.raw(
                'select distinct * from RECA.CORE_LASTUNAS l INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON l.NUMEROIDENTIDAD =  info.NIT WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT and DPA = 3107 order by NUMEROIDENTIDAD')
        if city_name == 'Amancio':
            return LasTunas.objects.raw(
                'select distinct * from RECA.CORE_LASTUNAS l INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON l.NUMEROIDENTIDAD =  info.NIT WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT and DPA = 3108 order by NUMEROIDENTIDAD')

    def resolve_las_tunas(self, info):
        return LasTunas.objects.all()


schema = graphene.Schema(query=ContributorsFromLasTunasQuery, auto_camelcase=False)
