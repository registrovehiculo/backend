import graphene
from capitania.apps.api.types.provincias import CiegoDeAvilaType, InfogestiContributorsType
from capitania.apps.core.models import CiegoDeAvila, InfogestiContributors


class ContributorsFromCiegoDeAvilaQuery(graphene.ObjectType):
    contributors_missing_in_onat_ciego = graphene.List(CiegoDeAvilaType, city_name=graphene.String())
    contributors_with_different_information_ciego = graphene.List(CiegoDeAvilaType, city_name=graphene.String())
    contributors_with_different_information_ciego_infogesti = graphene.List(InfogestiContributorsType, city_name=graphene.String())
    contributors_with_equals_information_ciego = graphene.List(CiegoDeAvilaType, city_name=graphene.String())
    ciego = graphene.List(CiegoDeAvilaType)

    # 1 Contribuyentes que estan en capitania vehiculo que no estan en la onat
    def resolve_contributors_missing_in_onat_ciego(self, info, city_name=graphene.String()):

        if city_name == 'Chambas':
            return CiegoDeAvila.objects.raw(
                'select distinct * from RECA.CORE_CIEGODEAVILA cav LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON cav.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2901')
        if city_name == 'Moron':
            return CiegoDeAvila.objects.raw(
                'select distinct * from RECA.CORE_CIEGODEAVILA cav LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON cav.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2902')
        if city_name == 'Bolivia':
            return CiegoDeAvila.objects.raw(
                'select distinct * from RECA.CORE_CIEGODEAVILA cav LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON cav.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2903')
        if city_name == 'Primero De Enero':
            return CiegoDeAvila.objects.raw(
                'select distinct * from RECA.CORE_CIEGODEAVILA cav LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON cav.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2904')
        if city_name == 'Ciro Redondo':
            return CiegoDeAvila.objects.raw(
                'select distinct * from RECA.CORE_CIEGODEAVILA cav LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON cav.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2905')
        if city_name == 'Florencia':
            return CiegoDeAvila.objects.raw(
                'select distinct * from RECA.CORE_CIEGODEAVILA cav LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON cav.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2906')
        if city_name == 'Majagua':
            return CiegoDeAvila.objects.raw(
                'select distinct * from RECA.CORE_CIEGODEAVILA cav LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON cav.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2907')
        if city_name == 'Ciego de Avila':
            return CiegoDeAvila.objects.raw(
                'select distinct * from RECA.CORE_CIEGODEAVILA cav LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON cav.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2908')
        if city_name == 'Venezuela':
            return CiegoDeAvila.objects.raw(
                'select distinct * from RECA.CORE_CIEGODEAVILA cav LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON cav.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2909')
        if city_name == 'Baragua':
            return CiegoDeAvila.objects.raw(
                'select distinct * from RECA.CORE_CIEGODEAVILA cav LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON cav.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2910')

    # 2 Contribuyentes que estan en ambos capitania con informaciones diferentes
    def resolve_contributors_with_different_information_ciego(self, info, city_name=graphene.String()):

        if city_name == 'Chambas':
            return CiegoDeAvila.objects.raw(
                "select distinct * from RECA.CORE_CIEGODEAVILA cav INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON cav.NUMEROIDENTIDAD =  info.NIT and DPA = 2901 and info.UNIDAD = 2901 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NUMEROIDENTIDAD")
        if city_name == 'Moron':
            return CiegoDeAvila.objects.raw(
                "select distinct * from RECA.CORE_CIEGODEAVILA cav INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON cav.NUMEROIDENTIDAD =  info.NIT and DPA = 2902 and info.UNIDAD = 2902 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NUMEROIDENTIDAD")
        if city_name == 'Bolivia':
            return CiegoDeAvila.objects.raw(
                "select distinct * from RECA.CORE_CIEGODEAVILA cav INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON cav.NUMEROIDENTIDAD =  info.NIT and DPA = 2903 and info.UNIDAD = 2903 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NUMEROIDENTIDAD")
        if city_name == 'Primero De Enero':
            return CiegoDeAvila.objects.raw(
                "select distinct * from RECA.CORE_CIEGODEAVILA cav INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON cav.NUMEROIDENTIDAD =  info.NIT and DPA = 2904 and info.UNIDAD = 2904 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NUMEROIDENTIDAD")
        if city_name == 'Ciro Redondo':
            return CiegoDeAvila.objects.raw(
                "select distinct * from RECA.CORE_CIEGODEAVILA cav INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON cav.NUMEROIDENTIDAD =  info.NIT and DPA = 2905 and info.UNIDAD = 2905 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NUMEROIDENTIDAD")
        if city_name == 'Florencia':
            return CiegoDeAvila.objects.raw(
                "select distinct * from RECA.CORE_CIEGODEAVILA cav INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON cav.NUMEROIDENTIDAD =  info.NIT and DPA = 2906 and info.UNIDAD = 2906 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NUMEROIDENTIDAD")
        if city_name == 'Majagua':
            return CiegoDeAvila.objects.raw(
                "select distinct * from RECA.CORE_CIEGODEAVILA cav INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON cav.NUMEROIDENTIDAD =  info.NIT and DPA = 2907 and info.UNIDAD = 2907 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NUMEROIDENTIDAD")
        if city_name == 'Ciego de Avila':
            return CiegoDeAvila.objects.raw(
                "select distinct * from RECA.CORE_CIEGODEAVILA cav INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON cav.NUMEROIDENTIDAD =  info.NIT and DPA = 2908 and info.UNIDAD = 2908 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NUMEROIDENTIDAD")
        if city_name == 'Venezuela':
            return CiegoDeAvila.objects.raw(
                "select distinct * from RECA.CORE_CIEGODEAVILA cav INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON cav.NUMEROIDENTIDAD =  info.NIT and DPA = 2909 and info.UNIDAD = 2909 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NUMEROIDENTIDAD")
        if city_name == 'Baragua':
            return CiegoDeAvila.objects.raw(
                "select distinct * from RECA.CORE_CIEGODEAVILA cav INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON cav.NUMEROIDENTIDAD =  info.NIT and DPA = 2910 and info.UNIDAD = 2910 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NUMEROIDENTIDAD")


    def resolve_contributors_with_different_information_ciego_infogesti(self, info, city_name=graphene.String()):

        if city_name == 'Chambas':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@infogesti info INNER JOIN RECA.CORE_CIEGODEAVILA cav ON cav.NUMEROIDENTIDAD =  info.NIT and info.UNIDAD = 2901 and DPA = 2901 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NIT")
        if city_name == 'Moron':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@infogesti info INNER JOIN RECA.CORE_CIEGODEAVILA cav ON cav.NUMEROIDENTIDAD =  info.NIT and info.UNIDAD = 2902 and DPA = 2902 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NIT")
        if city_name == 'Bolivia':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@infogesti info INNER JOIN RECA.CORE_CIEGODEAVILA cav ON cav.NUMEROIDENTIDAD =  info.NIT and info.UNIDAD = 2903 and DPA = 2903 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NIT")
        if city_name == 'Primero De Enero':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@infogesti info INNER JOIN RECA.CORE_CIEGODEAVILA cav ON cav.NUMEROIDENTIDAD =  info.NIT and info.UNIDAD = 2904 and DPA = 2904 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NIT")
        if city_name == 'Ciro Redondo':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@infogesti info INNER JOIN RECA.CORE_CIEGODEAVILA cav ON cav.NUMEROIDENTIDAD =  info.NIT and info.UNIDAD = 2905 and DPA = 2905 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NIT")
        if city_name == 'Florencia':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@infogesti info INNER JOIN RECA.CORE_CIEGODEAVILA cav ON cav.NUMEROIDENTIDAD =  info.NIT and info.UNIDAD = 2906 and DPA = 2906 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NIT")
        if city_name == 'Majagua':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@infogesti info INNER JOIN RECA.CORE_CIEGODEAVILA cav ON cav.NUMEROIDENTIDAD =  info.NIT and info.UNIDAD = 2907 and DPA = 2907 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NIT")
        if city_name == 'Ciego de Avila':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@infogesti info INNER JOIN RECA.CORE_CIEGODEAVILA cav ON cav.NUMEROIDENTIDAD =  info.NIT and info.UNIDAD = 2908 and DPA = 2908 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NIT")
        if city_name == 'Venezuela':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@infogesti info INNER JOIN RECA.CORE_CIEGODEAVILA cav ON cav.NUMEROIDENTIDAD =  info.NIT and info.UNIDAD = 2909 and DPA = 2909 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NIT")
        if city_name == 'Baragua':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@infogesti info INNER JOIN RECA.CORE_CIEGODEAVILA cav ON cav.NUMEROIDENTIDAD =  info.NIT and info.UNIDAD = 2910 and DPA = 2910 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NIT")


    # 4 Contribuyentes totalmente coincidentes
    def resolve_contributors_with_equals_information_ciego(self, info, city_name=graphene.String()):

        if city_name == 'Chambas':
            return CiegoDeAvila.objects.raw(
                'select distinct * from RECA.CORE_CIEGODEAVILA cav INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON cav.NUMEROIDENTIDAD =  info.NIT and DPA = 2901 WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT order by NUMEROIDENTIDAD')
        if city_name == 'Moron':
            return CiegoDeAvila.objects.raw(
                'select distinct * from RECA.CORE_CIEGODEAVILA cav INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON cav.NUMEROIDENTIDAD =  info.NIT and DPA = 2902 WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT order by NUMEROIDENTIDAD2')
        if city_name == 'Bolivia':
            return CiegoDeAvila.objects.raw(
                'select distinct * from RECA.CORE_CIEGODEAVILA cav INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON cav.NUMEROIDENTIDAD =  info.NIT and DPA = 2903 WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT order by NUMEROIDENTIDAD')
        if city_name == 'Primero De Enero':
            return CiegoDeAvila.objects.raw(
                'select distinct * from RECA.CORE_CIEGODEAVILA cav INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON cav.NUMEROIDENTIDAD =  info.NIT and DPA = 2904 WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT order by NUMEROIDENTIDAD')
        if city_name == 'Ciro Redondo':
            return CiegoDeAvila.objects.raw(
                'select distinct * from RECA.CORE_CIEGODEAVILA cav INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON cav.NUMEROIDENTIDAD =  info.NIT and DPA = 2905 WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT order by NUMEROIDENTIDAD')
        if city_name == 'Florencia':
            return CiegoDeAvila.objects.raw(
                'select distinct * from RECA.CORE_CIEGODEAVILA cav INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON cav.NUMEROIDENTIDAD =  info.NIT and DPA = 2906 WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT order by NUMEROIDENTIDAD')
        if city_name == 'Majagua':
            return CiegoDeAvila.objects.raw(
                'select distinct * from RECA.CORE_CIEGODEAVILA cav INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON cav.NUMEROIDENTIDAD =  info.NIT and DPA = 2907 WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT order by NUMEROIDENTIDAD')
        if city_name == 'Ciego de Avila':
            return CiegoDeAvila.objects.raw(
                'select distinct * from RECA.CORE_CIEGODEAVILA cav INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON cav.NUMEROIDENTIDAD =  info.NIT and DPA = 2908 WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT order by NUMEROIDENTIDAD')
        if city_name == 'Venezuela':
            return CiegoDeAvila.objects.raw(
                'select distinct * from RECA.CORE_CIEGODEAVILA cav INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON cav.NUMEROIDENTIDAD =  info.NIT and DPA = 2909 WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT order by NUMEROIDENTIDAD')
        if city_name == 'Baragua':
            return CiegoDeAvila.objects.raw(
                'select distinct * from RECA.CORE_CIEGODEAVILA cav INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON cav.NUMEROIDENTIDAD =  info.NIT and DPA = 2910 WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT order by NUMEROIDENTIDAD')

    def resolve_ciego(self, info):
        return CiegoDeAvila.objects.all()


schema = graphene.Schema(query=ContributorsFromCiegoDeAvilaQuery, auto_camelcase=False)
