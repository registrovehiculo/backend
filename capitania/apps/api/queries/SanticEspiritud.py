import graphene
from capitania.apps.api.types.provincias import SanticEspiritudType, InfogestiContributorsType
from capitania.apps.core.models import SanticEspiritud,  InfogestiContributors


class ContributorsFromSanticEspiritudQuery(graphene.ObjectType):
    contributors_missing_in_onat_santic_espiritud = graphene.List(SanticEspiritudType, city_name=graphene.String())
    contributors_with_different_information_santic_espiritud = graphene.List(SanticEspiritudType, city_name=graphene.String())
    contributors_with_different_information_santic_espiritud_infogesti = graphene.List(InfogestiContributorsType, city_name=graphene.String())
    contributors_with_equals_information_santic_espiritud = graphene.List(SanticEspiritudType, city_name=graphene.String())
    santic_espiritud = graphene.List(SanticEspiritudType)

    # 1 Contribuyentes que estan en capitania vehiculo que no estan en la onat
    def resolve_contributors_missing_in_onat_santic_espiritud(self, info, city_name=graphene.String()):
        if city_name == 'Yaguajay':
            return SanticEspiritud.objects.raw(
                'select distinct * from CORE_SANTICESPIRITUD s LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON s.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2801')
        if city_name == 'Jatibonico':
            return SanticEspiritud.objects.raw(
                'select distinct * from CORE_SANTICESPIRITUD s LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON s.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2802')
        if city_name == 'Taguasco':
            return SanticEspiritud.objects.raw(
                'select distinct * from CORE_SANTICESPIRITUD s LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON s.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2803')
        if city_name == 'Cabaiguán':
            return SanticEspiritud.objects.raw(
                'select distinct * from CORE_SANTICESPIRITUD s LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON s.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2804')
        if city_name == 'Fomento':
            return SanticEspiritud.objects.raw(
                'select distinct * from CORE_SANTICESPIRITUD s LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON s.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2805')
        if city_name == 'Trinidad':
            return SanticEspiritud.objects.raw(
                'select distinct * from CORE_SANTICESPIRITUD s LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON s.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2806')
        if city_name == 'Sancti Spiritus':
            return SanticEspiritud.objects.raw(
                'select distinct * from CORE_SANTICESPIRITUD s LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON s.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2807')
        if city_name == 'La Sierpe':
            return SanticEspiritud.objects.raw(
                'select distinct * from CORE_SANTICESPIRITUD s LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON s.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2808')

    # 2 Contribuyentes que estan en ambos capitania con informaciones diferentes
    def resolve_contributors_with_different_information_santic_espiritud(self, info, city_name=graphene.String()):

        if city_name == 'Yaguajay':
            return SanticEspiritud.objects.raw(
                "select distinct * from CORE_SANTICESPIRITUD s INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON s.NUMEROIDENTIDAD =  info.NIT and UNIDAD = 2801  and info.ES_PROPIETARIO_TT = '1' and DPA = 2801 WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NUMEROIDENTIDAD")
        if city_name == 'Jatibonico':
            return SanticEspiritud.objects.raw(
                "select distinct * from CORE_SANTICESPIRITUD s INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON s.NUMEROIDENTIDAD =  info.NIT and UNIDAD = 2802  and info.ES_PROPIETARIO_TT = '1' and DPA = 2802 WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NUMEROIDENTIDAD")
        if city_name == 'Taguasco':
            return SanticEspiritud.objects.raw(
                "select distinct * from CORE_SANTICESPIRITUD s INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON s.NUMEROIDENTIDAD =  info.NIT and UNIDAD = 2803  and info.ES_PROPIETARIO_TT = '1' and DPA = 2803 WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NUMEROIDENTIDAD")
        if city_name == 'Cabaiguán':
            return SanticEspiritud.objects.raw(
                "select distinct * from CORE_SANTICESPIRITUD s INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON s.NUMEROIDENTIDAD =  info.NIT and UNIDAD = 2804  and info.ES_PROPIETARIO_TT = '1' and DPA = 2804 WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NUMEROIDENTIDAD")
        if city_name == 'Fomento':
            return SanticEspiritud.objects.raw(
                "select distinct * from CORE_SANTICESPIRITUD s INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON s.NUMEROIDENTIDAD =  info.NIT  and UNIDAD = 2805 and info.ES_PROPIETARIO_TT = '1' and DPA = 2805 WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NUMEROIDENTIDAD")
        if city_name == 'Trinidad':
            return SanticEspiritud.objects.raw(
                "select distinct * from CORE_SANTICESPIRITUD s INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON s.NUMEROIDENTIDAD =  info.NIT  and UNIDAD = 2806 and info.ES_PROPIETARIO_TT = '1' and DPA = 2806 WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NUMEROIDENTIDAD")
        if city_name == 'Sancti Spiritus':
            return SanticEspiritud.objects.raw(
                "select distinct * from CORE_SANTICESPIRITUD s INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON s.NUMEROIDENTIDAD =  info.NIT and UNIDAD = 2807  and info.ES_PROPIETARIO_TT = '1' and DPA = 2807 WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NUMEROIDENTIDAD")
        if city_name == 'La Sierpe':
            return SanticEspiritud.objects.raw(
                "select distinct * from CORE_SANTICESPIRITUD s INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON s.NUMEROIDENTIDAD =  info.NIT  and UNIDAD = 2808 and info.ES_PROPIETARIO_TT = '1' and DPA = 2808 WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NUMEROIDENTIDAD")

    def resolve_contributors_with_different_information_santic_espiritud_infogesti(self, info, city_name=graphene.String()):

        if city_name == 'Yaguajay':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@infogesti info INNER JOIN CORE_SANTICESPIRITUD s ON s.NUMEROIDENTIDAD =  info.NIT and UNIDAD = 2801 and DPA = 2801 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NIT")
        if city_name == 'Jatibonico':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@infogesti info INNER JOIN CORE_SANTICESPIRITUD s ON s.NUMEROIDENTIDAD =  info.NIT and UNIDAD = 2802 and DPA = 2802 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NIT")
        if city_name == 'Taguasco':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@infogesti info INNER JOIN CORE_SANTICESPIRITUD s ON s.NUMEROIDENTIDAD =  info.NIT and UNIDAD = 2803 and DPA = 2803 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NIT")
        if city_name == 'Cabaiguán':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@infogesti info INNER JOIN CORE_SANTICESPIRITUD s ON s.NUMEROIDENTIDAD =  info.NIT and UNIDAD = 2804 and DPA = 2804 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NIT")
        if city_name == 'Fomento':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@infogesti info INNER JOIN CORE_SANTICESPIRITUD s ON s.NUMEROIDENTIDAD =  info.NIT and UNIDAD = 2805 and DPA = 2805 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NIT")
        if city_name == 'Trinidad':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@infogesti info INNER JOIN CORE_SANTICESPIRITUD s ON s.NUMEROIDENTIDAD =  info.NIT and UNIDAD = 2806 and DPA = 2806 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NIT")
        if city_name == 'Sancti Spiritus':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@infogesti info INNER JOIN CORE_SANTICESPIRITUD s ON s.NUMEROIDENTIDAD =  info.NIT and UNIDAD = 2807 and DPA = 2807 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NIT")
        if city_name == 'La Sierpe':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@infogesti info INNER JOIN CORE_SANTICESPIRITUD s ON s.NUMEROIDENTIDAD =  info.NIT and UNIDAD = 2808 and DPA = 2808 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NIT")

    # 4 Contribuyentes totalmente coincidentes
    def resolve_contributors_with_equals_information_santic_espiritud(self, info, city_name=graphene.String()):

        if city_name == 'Yaguajay':
            return SanticEspiritud.objects.raw(
                'select distinct * from CORE_SANTICESPIRITUD s INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON s.NUMEROIDENTIDAD =  info.NIT WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT and DPA = 2801 order by NUMEROIDENTIDAD')
        if city_name == 'Jatibonico':
            return SanticEspiritud.objects.raw(
                'select distinct * from CORE_SANTICESPIRITUD s INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON s.NUMEROIDENTIDAD =  info.NIT WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT and DPA = 2802 order by NUMEROIDENTIDAD')
        if city_name == 'Taguasco':
            return SanticEspiritud.objects.raw(
                'select distinct * from CORE_SANTICESPIRITUD s INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON s.NUMEROIDENTIDAD =  info.NIT WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT and DPA = 2803 order by NUMEROIDENTIDAD')
        if city_name == 'Cabaiguán':
            return SanticEspiritud.objects.raw(
                'select distinct * from CORE_SANTICESPIRITUD s INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON s.NUMEROIDENTIDAD =  info.NIT WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT and DPA = 2804 order by NUMEROIDENTIDAD')
        if city_name == 'Fomento':
            return SanticEspiritud.objects.raw(
                'select distinct * from CORE_SANTICESPIRITUD s INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON s.NUMEROIDENTIDAD =  info.NIT WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT and DPA = 2805 order by NUMEROIDENTIDAD')
        if city_name == 'Trinidad':
            return SanticEspiritud.objects.raw(
                'select distinct * from CORE_SANTICESPIRITUD s INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON s.NUMEROIDENTIDAD =  info.NIT WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT and DPA = 2806 order by NUMEROIDENTIDAD')
        if city_name == 'Sancti Spiritus':
            return SanticEspiritud.objects.raw(
                'select distinct * from CORE_SANTICESPIRITUD s INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON s.NUMEROIDENTIDAD =  info.NIT WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT and DPA = 2807 order by NUMEROIDENTIDAD')
        if city_name == 'La Sierpe':
            return SanticEspiritud.objects.raw(
                'select distinct * from CORE_SANTICESPIRITUD s INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON s.NUMEROIDENTIDAD =  info.NIT WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT and DPA = 2808 order by NUMEROIDENTIDAD')

    def resolve_santic_espiritud(self, info):
        return SanticEspiritud.objects.all()


schema = graphene.Schema(query=ContributorsFromSanticEspiritudQuery, auto_camelcase=False)
