import graphene
from capitania.apps.api.types.provincias import GuantanamoType, InfogestiContributorsType
from capitania.apps.core.models import Guantanamo, InfogestiContributors


class ContributorsFromGuantanamoQuery(graphene.ObjectType):
    contributors_missing_in_onat_guantanamo = graphene.List(GuantanamoType, city_name=graphene.String())
    contributors_with_different_information_guantanamo = graphene.List(GuantanamoType, city_name=graphene.String())
    contributors_with_different_information_guantanamo_infogesti = graphene.List(InfogestiContributorsType, city_name=graphene.String())
    contributors_with_equals_information_guantanamo = graphene.List(GuantanamoType, city_name=graphene.String())
    guantanamo = graphene.List(GuantanamoType)

    # 1 Contribuyentes que estan en capitania vehiculo que no estan en la onat
    def resolve_contributors_missing_in_onat_guantanamo(self, info, city_name=graphene.String()):

        if city_name == 'El Salvador':
            return Guantanamo.objects.raw(
                'select distinct * from CORE_GUANTANAMO gm LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON gm.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 3501')
        if city_name == 'Manuel Tames':
            return Guantanamo.objects.raw(
                'select distinct * from CORE_GUANTANAMO gm LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON gm.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 3502')
        if city_name == 'Yateras':
            return Guantanamo.objects.raw(
                'select distinct * from CORE_GUANTANAMO gm LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON gm.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 3503')
        if city_name == 'Baracoa':
            return Guantanamo.objects.raw(
                'select distinct * from CORE_GUANTANAMO gm LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON gm.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 3504')
        if city_name == 'Maisi':
            return Guantanamo.objects.raw(
                'select distinct * from CORE_GUANTANAMO gm LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON gm.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 3505')
        if city_name == 'Imias':
            return Guantanamo.objects.raw(
                'select distinct * from CORE_GUANTANAMO gm LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON gm.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 3506')
        if city_name == 'San Antonio Del Sur':
            return Guantanamo.objects.raw(
                'select distinct * from CORE_GUANTANAMO gm LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON gm.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 3507')
        if city_name == 'Caimanera':
            return Guantanamo.objects.raw(
                'select distinct * from CORE_GUANTANAMO gm LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON gm.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 3508')
        if city_name == 'Guantanamo':
            return Guantanamo.objects.raw(
                'select distinct * from CORE_GUANTANAMO gm LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON gm.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 3509')
        if city_name == 'Niceto Perez':
            return Guantanamo.objects.raw(
                'select distinct * from CORE_GUANTANAMO gm LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON gm.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 3510')



    # 2 Contribuyentes que estan en ambos capitania con informaciones diferentes
    def resolve_contributors_with_different_information_guantanamo(self, info, city_name=graphene.String()):

        if city_name == 'El Salvador':
            return Guantanamo.objects.raw(
                "select distinct * from CORE_GUANTANAMO gm INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON gm.NUMEROIDENTIDAD =  info.NIT and DPA = 3501 and UNIDAD = 3501 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT order by NUMEROIDENTIDAD")
        if city_name == 'Manuel Tames':
            return Guantanamo.objects.raw(
                "select distinct * from CORE_GUANTANAMO gm INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON gm.NUMEROIDENTIDAD =  info.NIT and DPA = 3502 and UNIDAD = 3502 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT order by NUMEROIDENTIDAD")
        if city_name == 'Yateras':
            return Guantanamo.objects.raw(
                "select distinct * from CORE_GUANTANAMO gm INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON gm.NUMEROIDENTIDAD =  info.NIT and DPA = 3503 and UNIDAD = 3503 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT order by NUMEROIDENTIDAD")
        if city_name == 'Baracoa':
            return Guantanamo.objects.raw(
                "select distinct * from CORE_GUANTANAMO gm INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON gm.NUMEROIDENTIDAD =  info.NIT and DPA = 3504 and UNIDAD = 3504 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT order by NUMEROIDENTIDAD")
        if city_name == 'Maisi':
            return Guantanamo.objects.raw(
                "select distinct * from CORE_GUANTANAMO gm INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON gm.NUMEROIDENTIDAD =  info.NIT and DPA = 3505 and UNIDAD = 3505 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT order by NUMEROIDENTIDAD")
        if city_name == 'Imias':
            return Guantanamo.objects.raw(
                "select distinct * from CORE_GUANTANAMO gm INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON gm.NUMEROIDENTIDAD =  info.NIT and DPA = 3506 and UNIDAD = 3506 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT order by NUMEROIDENTIDAD")
        if city_name == 'San Antonio Del Sur':
            return Guantanamo.objects.raw(
                "select distinct * from CORE_GUANTANAMO gm INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON gm.NUMEROIDENTIDAD =  info.NIT and DPA = 3507 and UNIDAD = 3507 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT order by NUMEROIDENTIDAD")
        if city_name == 'Caimanera':
            return Guantanamo.objects.raw(
                "select distinct * from CORE_GUANTANAMO gm INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON gm.NUMEROIDENTIDAD =  info.NIT and DPA = 3508 and UNIDAD = 3508 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT order by NUMEROIDENTIDAD")
        if city_name == 'Guantanamo':
            return Guantanamo.objects.raw(
                "select distinct * from CORE_GUANTANAMO gm INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON gm.NUMEROIDENTIDAD =  info.NIT and DPA = 3509 and UNIDAD = 3509 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT order by NUMEROIDENTIDAD")
        if city_name == 'Niceto Perez':
            return Guantanamo.objects.raw(
                "select distinct * from CORE_GUANTANAMO gm INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON gm.NUMEROIDENTIDAD =  info.NIT and DPA = 3510 and UNIDAD = 3510 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT order by NUMEROIDENTIDAD")


    def resolve_contributors_with_different_information_guantanamo_infogesti(self, info, city_name=graphene.String()):

        if city_name == 'El Salvador':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@infogesti info INNER JOIN CORE_GUANTANAMO gm ON gm.NUMEROIDENTIDAD =  info.NIT and UNIDAD = 3501 and DPA = 3501 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order  by NIT")
        if city_name == 'Manuel Tames':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@infogesti info INNER JOIN CORE_GUANTANAMO gm ON gm.NUMEROIDENTIDAD =  info.NIT and UNIDAD = 3502 and DPA = 3502 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NIT")
        if city_name == 'Yateras':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@infogesti info INNER JOIN CORE_GUANTANAMO gm ON gm.NUMEROIDENTIDAD =  info.NIT and UNIDAD = 3503 and DPA = 3503 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NIT")
        if city_name == 'Baracoa':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@infogesti info INNER JOIN CORE_GUANTANAMO gm ON gm.NUMEROIDENTIDAD =  info.NIT and UNIDAD = 3504 and DPA = 3504 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NIT")
        if city_name == 'Maisi':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@infogesti info INNER JOIN CORE_GUANTANAMO gm ON gm.NUMEROIDENTIDAD =  info.NIT and UNIDAD = 3505 and DPA = 3505 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NIT")
        if city_name == 'Imias':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@infogesti info INNER JOIN CORE_GUANTANAMO gm ON gm.NUMEROIDENTIDAD =  info.NIT and UNIDAD = 3506 and DPA = 3506 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NIT")
        if city_name == 'San Antonio Del Sur':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@infogesti info INNER JOIN CORE_GUANTANAMO gm ON gm.NUMEROIDENTIDAD =  info.NIT and UNIDAD = 3507 and DPA = 3507 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NIT")
        if city_name == 'Caimanera':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@infogesti info INNER JOIN CORE_GUANTANAMO gm ON gm.NUMEROIDENTIDAD =  info.NIT and UNIDAD = 3508 and DPA = 3508 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NIT")
        if city_name == 'Guantanamo':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@infogesti info INNER JOIN CORE_GUANTANAMO gm ON gm.NUMEROIDENTIDAD =  info.NIT and UNIDAD = 3509 and DPA = 3509 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NIT")
        if city_name == 'Niceto Perez':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@infogesti info INNER JOIN CORE_GUANTANAMO gm ON gm.NUMEROIDENTIDAD =  info.NIT and UNIDAD = 3510 and DPA = 3510 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NIT")


    # 4 Contribuyentes totalmente coincidentes
    def resolve_contributors_with_equals_information_guantanamo(self, info, city_name=graphene.String()):

        if city_name == 'El Salvador':
            return Guantanamo.objects.raw(
                'select distinct * from CORE_GUANTANAMO gm INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON gm.NUMEROIDENTIDAD =  info.NIT and DPA = 3501 WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT order by NUMEROIDENTIDAD')
        if city_name == 'Manuel Tames':
            return Guantanamo.objects.raw(
                'select distinct * from CORE_GUANTANAMO gm INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON gm.NUMEROIDENTIDAD =  info.NIT and DPA = 3502 WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT order by NUMEROIDENTIDAD')
        if city_name == 'Yateras':
            return Guantanamo.objects.raw(
                'select distinct * from CORE_GUANTANAMO gm INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON gm.NUMEROIDENTIDAD =  info.NIT and DPA = 3503 WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT order by NUMEROIDENTIDAD')
        if city_name == 'Baracoa':
            return Guantanamo.objects.raw(
                'select distinct * from CORE_GUANTANAMO gm INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON gm.NUMEROIDENTIDAD =  info.NIT and DPA = 3504 WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT order by NUMEROIDENTIDAD')
        if city_name == 'Maisi':
            return Guantanamo.objects.raw(
                'select distinct * from CORE_GUANTANAMO gm INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON gm.NUMEROIDENTIDAD =  info.NIT and DPA = 3505 WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT order by NUMEROIDENTIDAD')
        if city_name == 'Imias':
            return Guantanamo.objects.raw(
                'select distinct * from CORE_GUANTANAMO gm INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON gm.NUMEROIDENTIDAD =  info.NIT and DPA = 3506 WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT order by NUMEROIDENTIDAD')
        if city_name == 'San Antonio Del Sur':
            return Guantanamo.objects.raw(
                'select distinct * from CORE_GUANTANAMO gm INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON gm.NUMEROIDENTIDAD =  info.NIT and DPA = 3507 WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT order by NUMEROIDENTIDAD')
        if city_name == 'Caimanera':
            return Guantanamo.objects.raw(
                'select distinct * from CORE_GUANTANAMO gm INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON gm.NUMEROIDENTIDAD =  info.NIT and DPA = 3508 WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT order by NUMEROIDENTIDAD')
        if city_name == 'Guantanamo':
            return Guantanamo.objects.raw(
                'select distinct * from CORE_GUANTANAMO gm INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON gm.NUMEROIDENTIDAD =  info.NIT and DPA = 3509 WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT order by NUMEROIDENTIDAD')
        if city_name == 'Niceto Perez':
            return Guantanamo.objects.raw(
                'select distinct * from CORE_GUANTANAMO gm INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON gm.NUMEROIDENTIDAD =  info.NIT and DPA = 3510 WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT order by NUMEROIDENTIDAD')

    def resolve_guantanamo(self, info):
        return Guantanamo.objects.all()


schema = graphene.Schema(query=ContributorsFromGuantanamoQuery, auto_camelcase=False)
