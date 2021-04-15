import graphene
from capitania.apps.api.types.provincias import CienfuegosType, InfogestiContributorsType
from capitania.apps.core.models import Cienfuegos, InfogestiContributors


class ContributorsFromCienfuegosQuery(graphene.ObjectType):
    contributors_missing_in_onat_cienfuegos = graphene.List(CienfuegosType, city_name=graphene.String())
    contributors_with_different_information_cienfuegos = graphene.List(CienfuegosType, city_name=graphene.String())
    contributors_with_different_information_cienfuegos_infogesti = graphene.List(InfogestiContributorsType, city_name=graphene.String())
    contributors_with_equals_information_cienfuegos = graphene.List(CienfuegosType, city_name=graphene.String())
    cienfuegos = graphene.List(CienfuegosType)

    # 1 Contribuyentes que estan en capitania vehiculo que no estan en la onat
    def resolve_contributors_missing_in_onat_cienfuegos(self, info, city_name=graphene.String()):

        if city_name == 'Aguada de Pasajeros':
            return Cienfuegos.objects.raw(
                'select distinct * from CORE_CIENFUEGOS cf LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON cf.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2701')
        if city_name == 'Rodas':
            return Cienfuegos.objects.raw(
                'select distinct * from CORE_CIENFUEGOS cf LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON cf.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2702')
        if city_name == 'Palmira':
            return Cienfuegos.objects.raw(
                'select distinct * from CORE_CIENFUEGOS cf LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON cf.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2703')
        if city_name == 'las Lajas':
            return Cienfuegos.objects.raw(
                'select distinct * from CORE_CIENFUEGOS cf LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON cf.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2704')
        if city_name == 'Cruces':
            return Cienfuegos.objects.raw(
                'select distinct * from CORE_CIENFUEGOS cf LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON cf.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2705')
        if city_name == 'Cumanayagua':
            return Cienfuegos.objects.raw(
                'select distinct * from CORE_CIENFUEGOS cf LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON cf.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2706')
        if city_name == 'Cienfuegos':
            return Cienfuegos.objects.raw(
                'select distinct * from CORE_CIENFUEGOS cf LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON cf.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2707')
        if city_name == 'Abreus':
            return Cienfuegos.objects.raw(
                'select distinct * from CORE_CIENFUEGOS cf LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON cf.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2708')

    # 2 Contribuyentes que estan en ambos capitania con informaciones diferentes
    def resolve_contributors_with_different_information_cienfuegos(self, info, city_name=graphene.String()):

        if city_name == 'Aguada de Pasajeros':
            return Cienfuegos.objects.raw(
                "select distinct * from CORE_CIENFUEGOS cf INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON cf.NUMEROIDENTIDAD =  info.NIT and DPA = 2701 and info.UNIDAD = 2701 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NUMEROIDENTIDAD")
        if city_name == 'Rodas':
            return Cienfuegos.objects.raw(
                "select distinct * from CORE_CIENFUEGOS cf INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON cf.NUMEROIDENTIDAD =  info.NIT and DPA = 2702 and info.UNIDAD = 2702 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NUMEROIDENTIDAD")
        if city_name == 'Palmira':
            return Cienfuegos.objects.raw(
                "select distinct * from CORE_CIENFUEGOS cf INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON cf.NUMEROIDENTIDAD =  info.NIT and DPA = 2703 and info.UNIDAD = 2703 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NUMEROIDENTIDAD")
        if city_name == 'las Lajas':
            return Cienfuegos.objects.raw(
                "select distinct * from CORE_CIENFUEGOS cf INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON cf.NUMEROIDENTIDAD =  info.NIT and DPA = 2704 and info.UNIDAD = 2704 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NUMEROIDENTIDAD")
        if city_name == 'Cruces':
            return Cienfuegos.objects.raw(
                "select distinct * from CORE_CIENFUEGOS cf INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON cf.NUMEROIDENTIDAD =  info.NIT and DPA = 2705 and info.UNIDAD = 2705 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NUMEROIDENTIDAD")
        if city_name == 'Cumanayagua':
            return Cienfuegos.objects.raw(
                "select distinct * from CORE_CIENFUEGOS cf INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON cf.NUMEROIDENTIDAD =  info.NIT and DPA = 2706 and info.UNIDAD = 2706 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NUMEROIDENTIDAD")
        if city_name == 'Cienfuegos':
            return Cienfuegos.objects.raw(
                "select distinct * from CORE_CIENFUEGOS cf INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON cf.NUMEROIDENTIDAD =  info.NIT and DPA = 2707 and info.UNIDAD = 2707 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NUMEROIDENTIDAD")
        if city_name == 'Abreus':
            return Cienfuegos.objects.raw(
                "select distinct * from CORE_CIENFUEGOS cf INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON cf.NUMEROIDENTIDAD =  info.NIT and DPA = 2708 and info.UNIDAD = 2708 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NUMEROIDENTIDAD")

    def resolve_contributors_with_different_information_cienfuegos_infogesti(self, info, city_name=graphene.String()):

        if city_name == 'Aguada de Pasajeros':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@infogesti info INNER JOIN CORE_CIENFUEGOS cf ON cf.NUMEROIDENTIDAD =  info.NIT and info.UNIDAD = 2701 and DPA = 2701 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NIT")
        if city_name == 'Rodas':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@infogesti info INNER JOIN CORE_CIENFUEGOS cf ON cf.NUMEROIDENTIDAD =  info.NIT and info.UNIDAD = 2702 and DPA = 2702 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NIT")
        if city_name == 'Palmira':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@infogesti info INNER JOIN CORE_CIENFUEGOS cf ON cf.NUMEROIDENTIDAD =  info.NIT and info.UNIDAD = 2703 and DPA = 2703 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NIT")
        if city_name == 'las Lajas':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@infogesti info INNER JOIN CORE_CIENFUEGOS cf ON cf.NUMEROIDENTIDAD =  info.NIT and info.UNIDAD = 2704 and DPA = 2704 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NIT")
        if city_name == 'Cruces':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@infogesti info INNER JOIN CORE_CIENFUEGOS cf ON cf.NUMEROIDENTIDAD =  info.NIT and info.UNIDAD = 2705 and DPA = 2705 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NIT")
        if city_name == 'Cumanayagua':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@infogesti info INNER JOIN CORE_CIENFUEGOS cf ON cf.NUMEROIDENTIDAD =  info.NIT and info.UNIDAD = 2706 and DPA = 2706 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NIT")
        if city_name == 'Cienfuegos':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@infogesti info INNER JOIN CORE_CIENFUEGOS cf ON cf.NUMEROIDENTIDAD =  info.NIT and info.UNIDAD = 2707 and DPA = 2707 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NIT")
        if city_name == 'Abreus':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@infogesti info INNER JOIN CORE_CIENFUEGOS cf ON cf.NUMEROIDENTIDAD =  info.NIT and info.UNIDAD = 2708 and DPA = 2708 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NIT")

    # 4 Contribuyentes totalmente coincidentes
    def resolve_contributors_with_equals_information_cienfuegos(self, info, city_name=graphene.String()):
        if city_name == 'Aguada de Pasajeros':
            return Cienfuegos.objects.raw(
                'select distinct * from CORE_CIENFUEGOS cf INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON cf.NUMEROIDENTIDAD =  info.NIT and DPA = 2701 WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT')
        if city_name == 'Rodas':
            return Cienfuegos.objects.raw(
                'select distinct * from CORE_CIENFUEGOS cf INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON cf.NUMEROIDENTIDAD =  info.NIT and DPA = 2702 WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT')
        if city_name == 'Palmira':
            return Cienfuegos.objects.raw(
                'select distinct * from CORE_CIENFUEGOS cf INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON cf.NUMEROIDENTIDAD =  info.NIT and DPA = 2703 WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT')
        if city_name == 'las Lajas':
            return Cienfuegos.objects.raw(
                'select distinct * from CORE_CIENFUEGOS cf INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON cf.NUMEROIDENTIDAD =  info.NIT and DPA = 2704 WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT')
        if city_name == 'Cruces':
            return Cienfuegos.objects.raw(
                'select distinct * from CORE_CIENFUEGOS cf INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON cf.NUMEROIDENTIDAD =  info.NIT and DPA = 2705 WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT')
        if city_name == 'Cumanayagua':
            return Cienfuegos.objects.raw(
                'select distinct * from CORE_CIENFUEGOS cf INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON cf.NUMEROIDENTIDAD =  info.NIT and DPA = 2706 WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT')
        if city_name == 'Cienfuegos':
            return Cienfuegos.objects.raw(
                'select distinct * from CORE_CIENFUEGOS cf INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON cf.NUMEROIDENTIDAD =  info.NIT and DPA = 2707 WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT')
        if city_name == 'Abreus':
            return Cienfuegos.objects.raw(
                'select distinct * from CORE_CIENFUEGOS cf INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON cf.NUMEROIDENTIDAD =  info.NIT and DPA = 2708 WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT')

    def resolve_cienfuegos(self, info):
        return Cienfuegos.objects.all()


schema = graphene.Schema(query=ContributorsFromCienfuegosQuery, auto_camelcase=False)
