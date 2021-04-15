import graphene
from capitania.apps.api.types.provincias import MatanzasType,InfogestiContributorsType
from capitania.apps.core.models import Matanzas, InfogestiContributors


class ContributorsFromMatanzasQuery(graphene.ObjectType):
    contributors_missing_in_onat_matanzas = graphene.List(MatanzasType, city_name=graphene.String())
    contributors_with_different_information_matanzas = graphene.List(MatanzasType, city_name=graphene.String())
    contributors_with_different_information_matanzas_infogesti = graphene.List(InfogestiContributorsType, city_name=graphene.String())
    contributors_with_equals_information_matanzas = graphene.List(MatanzasType, city_name=graphene.String())
    matanzas = graphene.List(MatanzasType)

    # 1 Contribuyentes que estan en capitania vehiculo que no estan en la onat
    def resolve_contributors_missing_in_onat_matanzas(self, info, city_name=graphene.String()):

        if city_name == 'Matanzas':
            return Matanzas.objects.raw(
                'select distinct * from CORE_MATANZAS m LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON m.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2501')
        if city_name == 'Cardenas':
            return Matanzas.objects.raw(
                'select distinct * from CORE_MATANZAS m LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON m.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2502')
        if city_name == 'Marti':
            return Matanzas.objects.raw(
                'select distinct * from CORE_MATANZAS m LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON m.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2503')
        if city_name == 'Colon':
            return Matanzas.objects.raw(
                'select distinct * from CORE_MATANZAS m LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON m.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2504')
        if city_name == 'Perico':
            return Matanzas.objects.raw(
                'select distinct * from CORE_MATANZAS m LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON m.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2505')
        if city_name == 'Jovellanos':
            return Matanzas.objects.raw(
                'select distinct * from CORE_MATANZAS m LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON m.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2506')
        if city_name == 'Pedro Betancourt':
            return Matanzas.objects.raw(
                'select distinct * from CORE_MATANZAS m LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON m.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2507')
        if city_name == 'Limonar':
            return Matanzas.objects.raw(
                'select distinct * from CORE_MATANZAS m LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON m.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2508')
        if city_name == 'Union de Reyes':
            return Matanzas.objects.raw(
                'select distinct * from CORE_MATANZAS m LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON m.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2509')
        if city_name == 'Cienaga De Zapata':
            return Matanzas.objects.raw(
                'select distinct * from CORE_MATANZAS m LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON m.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2510')
        if city_name == 'Jagüey Grande':
            return Matanzas.objects.raw(
                'select distinct * from CORE_MATANZAS m LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON m.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2511')
        if city_name == 'Calimete':
            return Matanzas.objects.raw(
                'select distinct * from CORE_MATANZAS m LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON m.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2512')
        if city_name == 'Los Arabos':
            return Matanzas.objects.raw(
                'select distinct * from CORE_MATANZAS m LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON m.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2513')

    # 2 Contribuyentes que estan en ambos capitania con informaciones diferentes
    def resolve_contributors_with_different_information_matanzas(self, info, city_name=graphene.String()):

        if city_name == 'Matanzas':
            return Matanzas.objects.raw(
                "select distinct * from CORE_MATANZAS m INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON m.NUMEROIDENTIDAD =  info.NIT  and info.ES_PROPIETARIO_TT = '1' and UNIDAD = 2501 and DPA = 2501 WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT")
        if city_name == 'Cardenas':
            return Matanzas.objects.raw(
                "select distinct * from CORE_MATANZAS m INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON m.NUMEROIDENTIDAD =  info.NIT  and info.ES_PROPIETARIO_TT = '1' and UNIDAD = 2502 and DPA = 2502 WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT")
        if city_name == 'Marti':
            return Matanzas.objects.raw(
                "select distinct * from CORE_MATANZAS m INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON m.NUMEROIDENTIDAD =  info.NIT  and info.ES_PROPIETARIO_TT = '1' and UNIDAD = 2503 and DPA = 2503 WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT")
        if city_name == 'Colon':
            return Matanzas.objects.raw(
                "select distinct * from CORE_MATANZAS m INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON m.NUMEROIDENTIDAD =  info.NIT  and info.ES_PROPIETARIO_TT = '1' and UNIDAD = 2504 and DPA = 2504 WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT")
        if city_name == 'Perico':
            return Matanzas.objects.raw(
                "select distinct * from CORE_MATANZAS m INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON m.NUMEROIDENTIDAD =  info.NIT  and info.ES_PROPIETARIO_TT = '1' and UNIDAD = 2505 and DPA = 2505 WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT")
        if city_name == 'Jovellanos':
            return Matanzas.objects.raw(
                "select distinct * from CORE_MATANZAS m INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON m.NUMEROIDENTIDAD =  info.NIT  and info.ES_PROPIETARIO_TT = '1' and UNIDAD = 2506 and DPA = 2506 WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT")
        if city_name == 'Pedro Betancourt':
            return Matanzas.objects.raw(
                "select distinct * from CORE_MATANZAS m INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON m.NUMEROIDENTIDAD =  info.NIT  and info.ES_PROPIETARIO_TT = '1' and UNIDAD = 2507 and DPA = 2507 WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT")
        if city_name == 'Limonar':
            return Matanzas.objects.raw(
                "select distinct * from CORE_MATANZAS m INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON m.NUMEROIDENTIDAD =  info.NIT  and info.ES_PROPIETARIO_TT = '1' and UNIDAD = 2508 and DPA = 2508 WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT")
        if city_name == 'Union de Reyes':
            return Matanzas.objects.raw(
                "select distinct * from CORE_MATANZAS m INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON m.NUMEROIDENTIDAD =  info.NIT  and info.ES_PROPIETARIO_TT = '1' and UNIDAD = 2509 and DPA = 2509 WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT")
        if city_name == 'Cienaga De Zapata':
            return Matanzas.objects.raw(
                "select distinct * from CORE_MATANZAS m INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON m.NUMEROIDENTIDAD =  info.NIT  and info.ES_PROPIETARIO_TT = '1' and UNIDAD = 2510 and DPA = 2510 WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT")
        if city_name == 'Jagüey Grande':
            return Matanzas.objects.raw(
                "select distinct * from CORE_MATANZAS m INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON m.NUMEROIDENTIDAD =  info.NIT  and info.ES_PROPIETARIO_TT = '1' and UNIDAD = 2511 and DPA = 2511 WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT")
        if city_name == 'Calimete':
            return Matanzas.objects.raw(
                "select distinct * from CORE_MATANZAS m INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON m.NUMEROIDENTIDAD =  info.NIT  and info.ES_PROPIETARIO_TT = '1' and UNIDAD = 2512 and DPA = 2512 WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT")
        if city_name == 'Los Arabos':
            return Matanzas.objects.raw(
                "select distinct * from CORE_MATANZAS m INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON m.NUMEROIDENTIDAD =  info.NIT  and info.ES_PROPIETARIO_TT = '1' and UNIDAD = 2513 and DPA = 2513 WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT")


    def resolve_contributors_with_different_information_matanzas_infogesti(self, info, city_name=graphene.String()):

        if city_name == 'Matanzas':
            return InfogestiContributors.objects.raw(
                "select distinct * from CORE_MATANZAS m INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON m.NUMEROIDENTIDAD =  info.NIT and UNIDAD = 2501 and DPA = 2501 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NIT")
        if city_name == 'Cardenas':
            return InfogestiContributors.objects.raw(
                "select distinct * from CORE_MATANZAS m INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON m.NUMEROIDENTIDAD =  info.NIT and UNIDAD = 2502 and DPA = 2502 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NIT")
        if city_name == 'Marti':
            return InfogestiContributors.objects.raw(
                "select distinct * from CORE_MATANZAS m INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON m.NUMEROIDENTIDAD =  info.NIT and UNIDAD = 2503 and DPA = 2503 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NIT")
        if city_name == 'Colon':
            return InfogestiContributors.objects.raw(
                "select distinct * from CORE_MATANZAS m INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON m.NUMEROIDENTIDAD =  info.NIT and UNIDAD = 2504 and DPA = 2504 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NIT")
        if city_name == 'Perico':
            return InfogestiContributors.objects.raw(
                "select distinct * from CORE_MATANZAS m INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON m.NUMEROIDENTIDAD =  info.NIT and UNIDAD = 2505 and DPA = 2505 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NIT")
        if city_name == 'Jovellanos':
            return InfogestiContributors.objects.raw(
                "select distinct * from CORE_MATANZAS m INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON m.NUMEROIDENTIDAD =  info.NIT and UNIDAD = 2506 and DPA = 2506 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NIT")
        if city_name == 'Pedro Betancourt':
            return InfogestiContributors.objects.raw(
                "select distinct * from CORE_MATANZAS m INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON m.NUMEROIDENTIDAD =  info.NIT and UNIDAD = 2507 and DPA = 2507 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NIT")
        if city_name == 'Limonar':
            return InfogestiContributors.objects.raw(
                "select distinct * from CORE_MATANZAS m INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON m.NUMEROIDENTIDAD =  info.NIT and UNIDAD = 2508 and DPA = 2508 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NIT")
        if city_name == 'Union de Reyes':
            return InfogestiContributors.objects.raw(
                "select distinct * from CORE_MATANZAS m INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON m.NUMEROIDENTIDAD =  info.NIT and UNIDAD = 2509 and DPA = 2509 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NIT")
        if city_name == 'Cienaga De Zapata':
            return InfogestiContributors.objects.raw(
                "select distinct * from CORE_MATANZAS m INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON m.NUMEROIDENTIDAD =  info.NIT and UNIDAD = 2510 and DPA = 2510 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NIT")
        if city_name == 'Jagüey Grande':
            return InfogestiContributors.objects.raw(
                "select distinct * from CORE_MATANZAS m INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON m.NUMEROIDENTIDAD =  info.NIT and UNIDAD = 2511 and DPA = 2511 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NIT")
        if city_name == 'Calimete':
            return InfogestiContributors.objects.raw(
                "select distinct * from CORE_MATANZAS m INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON m.NUMEROIDENTIDAD =  info.NIT and UNIDAD = 2512 and DPA = 2512 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NIT")
        if city_name == 'Los Arabos':
            return InfogestiContributors.objects.raw(
                "select distinct * from CORE_MATANZAS m INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON m.NUMEROIDENTIDAD =  info.NIT and UNIDAD = 2513 and DPA = 2513 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NIT")


    # 4 Contribuyentes totalmente coincidentes
    def resolve_contributors_with_equals_information_matanzas(self, info, city_name=graphene.String()):

        if city_name == 'Matanzas':
            return Matanzas.objects.raw(
                'select distinct * from CORE_MATANZAS m INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON m.NUMEROIDENTIDAD =  info.NIT WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT and DPA = 2501')
        if city_name == 'Cardenas':
            return Matanzas.objects.raw(
                'select distinct * from CORE_MATANZAS m INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON m.NUMEROIDENTIDAD =  info.NIT WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT and DPA = 2502')
        if city_name == 'Marti':
            return Matanzas.objects.raw(
                'select distinct * from CORE_MATANZAS m INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON m.NUMEROIDENTIDAD =  info.NIT WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT and DPA = 2503')
        if city_name == 'Colon':
            return Matanzas.objects.raw(
                'select distinct * from CORE_MATANZAS m INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON m.NUMEROIDENTIDAD =  info.NIT WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT and DPA = 2504')
        if city_name == 'Perico':
            return Matanzas.objects.raw(
                'select distinct * from CORE_MATANZAS m INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON m.NUMEROIDENTIDAD =  info.NIT WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT and DPA = 2505')
        if city_name == 'Jovellanos':
            return Matanzas.objects.raw(
                'select distinct * from CORE_MATANZAS m INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON m.NUMEROIDENTIDAD =  info.NIT WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT and DPA = 2506')
        if city_name == 'Pedro Betancourt':
            return Matanzas.objects.raw(
                'select distinct * from CORE_MATANZAS m INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON m.NUMEROIDENTIDAD =  info.NIT WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT and DPA = 2507')
        if city_name == 'Limonar':
            return Matanzas.objects.raw(
                'select distinct * from CORE_MATANZAS m INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON m.NUMEROIDENTIDAD =  info.NIT WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT and DPA = 2508')
        if city_name == 'Union de Reyes':
            return Matanzas.objects.raw(
                'select distinct * from CORE_MATANZAS m INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON m.NUMEROIDENTIDAD =  info.NIT WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT and DPA = 2509')
        if city_name == 'Cienaga De Zapata':
            return Matanzas.objects.raw(
                'select distinct * from CORE_MATANZAS m INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON m.NUMEROIDENTIDAD =  info.NIT WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT and DPA = 2510')
        if city_name == 'Jagüey Grande':
            return Matanzas.objects.raw(
                'select distinct * from CORE_MATANZAS m INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON m.NUMEROIDENTIDAD =  info.NIT WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT and DPA = 2511')
        if city_name == 'Calimete':
            return Matanzas.objects.raw(
                'select distinct * from CORE_MATANZAS m INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON m.NUMEROIDENTIDAD =  info.NIT WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT and DPA = 2512')
        if city_name == 'Los Arabos':
            return Matanzas.objects.raw(
                'select distinct * from CORE_MATANZAS m INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON m.NUMEROIDENTIDAD =  info.NIT WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT and DPA = 2513')

    def resolve_matanzas(self, info):
        return Matanzas.objects.all()


schema = graphene.Schema(query=ContributorsFromMatanzasQuery, auto_camelcase=False)
