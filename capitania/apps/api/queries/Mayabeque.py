import graphene
from capitania.apps.api.types.provincias import MayabequeType,  InfogestiContributorsType
from capitania.apps.core.models import Mayabeque, InfogestiContributors


class ContributorsFromMayabequeQuery(graphene.ObjectType):
    contributors_missing_in_onat_mayabeque = graphene.List(MayabequeType, city_name=graphene.String())
    contributors_with_different_information_mayabeque = graphene.List(MayabequeType, city_name=graphene.String())
    contributors_with_different_information_mayabeque_infogesti = graphene.List(InfogestiContributorsType, city_name=graphene.String())
    contributors_with_equals_information_mayabeque = graphene.List(MayabequeType, city_name=graphene.String())
    mayabeque = graphene.List(MayabequeType)

    # 1 Contribuyentes que estan en capitania vehiculo que no estan en la onat
    def resolve_contributors_missing_in_onat_mayabeque(self, info, city_name=graphene.String()):
        # Mayabueque
        if city_name == 'Bejucal':
            return Mayabeque.objects.raw(
                'select distinct * from CORE_MAYABEQUE m LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON m.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2401')
        if city_name == 'San Jose de las Lajas':
            return Mayabeque.objects.raw(
                'select distinct * from CORE_MAYABEQUE m LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON m.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2402')
        if city_name == 'Jaruco':
            return Mayabeque.objects.raw(
                'select distinct * from CORE_MAYABEQUE m LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON m.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2403')
        if city_name == 'Santa Cruz del Norte':
            return Mayabeque.objects.raw(
                'select distinct * from CORE_MAYABEQUE m LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON m.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2404')
        if city_name == 'Madruga':
            return Mayabeque.objects.raw(
                'select distinct * from CORE_MAYABEQUE m LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON m.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2405')
        if city_name == 'Nueva Paz':
            return Mayabeque.objects.raw(
                'select distinct * from CORE_MAYABEQUE m LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON m.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2406')
        if city_name == 'San Nicolás':
            return Mayabeque.objects.raw(
                'select distinct * from CORE_MAYABEQUE m LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON m.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2407')
        if city_name == 'Güines':
            return Mayabeque.objects.raw(
                'select distinct * from CORE_MAYABEQUE m LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON m.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2408')
        if city_name == 'Melena del Sur':
            return Mayabeque.objects.raw(
                'select distinct * from CORE_MAYABEQUE m LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON m.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2409')
        if city_name == 'Batabano':
            return Mayabeque.objects.raw(
                'select distinct * from CORE_MAYABEQUE m LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON m.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2410')
        if city_name == 'Quivican':
            return Mayabeque.objects.raw(
                'select distinct * from CORE_MAYABEQUE m LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON m.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2411')

    # 2 Contribuyentes que estan en ambos capitania con informaciones diferentes
    def resolve_contributors_with_different_information_mayabeque(self, info, city_name=graphene.String()):
        if city_name == 'Bejucal':
            return Mayabeque.objects.raw(
                "select distinct * from CORE_MAYABEQUE m INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON m.NUMEROIDENTIDAD =  info.NIT   and info.ES_PROPIETARIO_TT = '1' and UNIDAD = 2401 and DPA = 2401 WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order  by  NUMEROIDENTIDAD")
        if city_name == 'San Jose de las Lajas':
            return Mayabeque.objects.raw(
                "select distinct * from CORE_MAYABEQUE m INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON m.NUMEROIDENTIDAD =  info.NIT   and info.ES_PROPIETARIO_TT = '1' and UNIDAD = 2402 and DPA = 2402 WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order  by  NUMEROIDENTIDAD")
        if city_name == 'Jaruco':
            return Mayabeque.objects.raw(
                "select distinct * from CORE_MAYABEQUE m INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON m.NUMEROIDENTIDAD =  info.NIT   and info.ES_PROPIETARIO_TT = '1' and UNIDAD = 2403 and DPA = 2403 WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order  by  NUMEROIDENTIDAD")
        if city_name == 'Santa Cruz del Norte':
            return Mayabeque.objects.raw(
                "select distinct * from CORE_MAYABEQUE m INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON m.NUMEROIDENTIDAD =  info.NIT   and info.ES_PROPIETARIO_TT = '1' and UNIDAD = 2404 and DPA = 2404 WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order  by  NUMEROIDENTIDAD")
        if city_name == 'Madruga':
            return Mayabeque.objects.raw(
                "select distinct * from CORE_MAYABEQUE m INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON m.NUMEROIDENTIDAD =  info.NIT   and info.ES_PROPIETARIO_TT = '1' and UNIDAD = 2405 and DPA = 2405 WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order  by  NUMEROIDENTIDAD")
        if city_name == 'Nueva Paz':
            return Mayabeque.objects.raw(
                "select distinct * from CORE_MAYABEQUE m INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON m.NUMEROIDENTIDAD =  info.NIT   and info.ES_PROPIETARIO_TT = '1' and UNIDAD = 2406 and DPA = 2406 WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order  by  NUMEROIDENTIDAD")
        if city_name == 'San Nicolás':
            return Mayabeque.objects.raw(
                "select distinct * from CORE_MAYABEQUE m INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON m.NUMEROIDENTIDAD =  info.NIT   and info.ES_PROPIETARIO_TT = '1' and UNIDAD = 2407 and DPA = 2407 WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order  by  NUMEROIDENTIDAD")
        if city_name == 'Güines':
            return Mayabeque.objects.raw(
                "select distinct * from CORE_MAYABEQUE m INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON m.NUMEROIDENTIDAD =  info.NIT   and info.ES_PROPIETARIO_TT = '1' and UNIDAD = 2408 and DPA = 2408 WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order  by  NUMEROIDENTIDAD")
        if city_name == 'Melena del Sur':
            return Mayabeque.objects.raw(
                "select distinct * from CORE_MAYABEQUE m INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON m.NUMEROIDENTIDAD =  info.NIT   and info.ES_PROPIETARIO_TT = '1' and UNIDAD = 2409 and DPA = 2409 WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order  by  NUMEROIDENTIDAD")
        if city_name == 'Batabano':
            return Mayabeque.objects.raw(
                "select distinct * from CORE_MAYABEQUE m INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON m.NUMEROIDENTIDAD =  info.NIT   and info.ES_PROPIETARIO_TT = '1' and UNIDAD = 2410 and DPA = 2410 WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order  by  NUMEROIDENTIDAD")
        if city_name == 'Quivican':
            return Mayabeque.objects.raw(
                "select distinct * from CORE_MAYABEQUE m INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON m.NUMEROIDENTIDAD =  info.NIT   and info.ES_PROPIETARIO_TT = '1' and UNIDAD = 2411 and DPA = 2411 WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order  by  NUMEROIDENTIDAD")


    def resolve_contributors_with_different_information_mayabeque_infogesti(self, info, city_name=graphene.String()):
        if city_name == 'Bejucal':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@infogesti info INNER JOIN CORE_MAYABEQUE m ON m.NUMEROIDENTIDAD =  info.NIT   and info.ES_PROPIETARIO_TT = '1' and UNIDAD = 2401 and DPA = 2401 WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order  by  NIT")
        if city_name == 'San Jose de las Lajas':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@infogesti info INNER JOIN CORE_MAYABEQUE m ON m.NUMEROIDENTIDAD =  info.NIT   and info.ES_PROPIETARIO_TT = '1' and UNIDAD = 2402 and DPA = 2402 WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order  by  NIT")
        if city_name == 'Jaruco':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@infogesti info INNER JOIN CORE_MAYABEQUE m ON m.NUMEROIDENTIDAD =  info.NIT   and info.ES_PROPIETARIO_TT = '1' and UNIDAD = 2403 and DPA = 2403 WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order  by  NIT")
        if city_name == 'Santa Cruz del Norte':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@infogesti info INNER JOIN CORE_MAYABEQUE m ON m.NUMEROIDENTIDAD =  info.NIT   and info.ES_PROPIETARIO_TT = '1' and UNIDAD = 2404 and DPA = 2404 WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order  by  NIT")
        if city_name == 'Madruga':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@infogesti info INNER JOIN CORE_MAYABEQUE m ON m.NUMEROIDENTIDAD =  info.NIT   and info.ES_PROPIETARIO_TT = '1' and UNIDAD = 2405 and DPA = 2405 WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order  by  NIT")
        if city_name == 'Nueva Paz':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@infogesti info INNER JOIN CORE_MAYABEQUE m ON m.NUMEROIDENTIDAD =  info.NIT   and info.ES_PROPIETARIO_TT = '1' and UNIDAD = 2406 and DPA = 2406 WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order  by  NIT")
        if city_name == 'San Nicolás':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@infogesti info INNER JOIN CORE_MAYABEQUE m ON m.NUMEROIDENTIDAD =  info.NIT   and info.ES_PROPIETARIO_TT = '1' and UNIDAD = 2407 and DPA = 2407 WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order  by  NIT")
        if city_name == 'Güines':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@infogesti info INNER JOIN CORE_MAYABEQUE m ON m.NUMEROIDENTIDAD =  info.NIT   and info.ES_PROPIETARIO_TT = '1' and UNIDAD = 2408 and DPA = 2408 WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order  by  NIT")
        if city_name == 'Melena del Sur':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@infogesti info INNER JOIN CORE_MAYABEQUE m ON m.NUMEROIDENTIDAD =  info.NIT   and info.ES_PROPIETARIO_TT = '1' and UNIDAD = 2409 and DPA = 2409 WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order  by  NIT")
        if city_name == 'Batabano':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@infogesti info INNER JOIN CORE_MAYABEQUE m ON m.NUMEROIDENTIDAD =  info.NIT   and info.ES_PROPIETARIO_TT = '1' and UNIDAD = 2410 and DPA = 2410 WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order  by  NIT")
        if city_name == 'Quivican':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@infogesti info INNER JOIN CORE_MAYABEQUE m ON m.NUMEROIDENTIDAD =  info.NIT   and info.ES_PROPIETARIO_TT = '1' and UNIDAD = 2411 and DPA = 2411 WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order  by  NIT")

    # 4 Contribuyentes totalmente coincidentes
    def resolve_contributors_with_equals_information_mayabeque(self, info, city_name=graphene.String()):
        if city_name == 'Bejucal':
            return Mayabeque.objects.raw(
                'select distinct * from CORE_MAYABEQUE m INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON m.NUMEROIDENTIDAD =  info.NIT WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT and DPA = 2401 order  by  NUMEROIDENTIDAD')
        if city_name == 'San Jose de las Lajas':
            return Mayabeque.objects.raw(
                'select distinct * from CORE_MAYABEQUE m INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON m.NUMEROIDENTIDAD =  info.NIT WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT and DPA = 2402 order  by  NUMEROIDENTIDAD')
        if city_name == 'Jaruco':
            return Mayabeque.objects.raw(
                'select distinct * from CORE_MAYABEQUE m INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON m.NUMEROIDENTIDAD =  info.NIT WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT and DPA = 2403 order  by  NUMEROIDENTIDAD')
        if city_name == 'Santa Cruz del Norte':
            return Mayabeque.objects.raw(
                'select distinct * from CORE_MAYABEQUE m INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON m.NUMEROIDENTIDAD =  info.NIT WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT and DPA = 2404 order  by  NUMEROIDENTIDAD')
        if city_name == 'Madruga':
            return Mayabeque.objects.raw(
                'select distinct * from CORE_MAYABEQUE m INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON m.NUMEROIDENTIDAD =  info.NIT WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT and DPA = 2405 order  by  NUMEROIDENTIDAD')
        if city_name == 'Nueva Paz':
            return Mayabeque.objects.raw(
                'select distinct * from CORE_MAYABEQUE m INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON m.NUMEROIDENTIDAD =  info.NIT WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT and DPA = 2406 order  by  NUMEROIDENTIDAD')
        if city_name == 'San Nicolás':
            return Mayabeque.objects.raw(
                'select distinct * from CORE_MAYABEQUE m INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON m.NUMEROIDENTIDAD =  info.NIT WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT and DPA = 2407 order  by  NUMEROIDENTIDAD')
        if city_name == 'Güines':
            return Mayabeque.objects.raw(
                'select distinct * from CORE_MAYABEQUE m INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON m.NUMEROIDENTIDAD =  info.NIT WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT and DPA = 2408 order  by  NUMEROIDENTIDAD')
        if city_name == 'Melena del Sur':
            return Mayabeque.objects.raw(
                'select distinct * from CORE_MAYABEQUE m INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON m.NUMEROIDENTIDAD =  info.NIT WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT and DPA = 2409 order  by  NUMEROIDENTIDAD')
        if city_name == 'Batabano':
            return Mayabeque.objects.raw(
                'select distinct * from CORE_MAYABEQUE m INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON m.NUMEROIDENTIDAD =  info.NIT WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT and DPA = 2410 order  by  NUMEROIDENTIDAD')
        if city_name == 'Quivican':
            return Mayabeque.objects.raw(
                'select distinct * from CORE_MAYABEQUE m INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON m.NUMEROIDENTIDAD =  info.NIT WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT and DPA = 2411 order  by  NUMEROIDENTIDAD')

    def resolve_mayabeque(self, info):
        return Mayabeque.objects.all()


schema = graphene.Schema(query=ContributorsFromMayabequeQuery, auto_camelcase=False)
