import graphene
from capitania.apps.api.types.provincias import CamagueyType, InfogestiContributorsType
from capitania.apps.core.models import Camaguey, InfogestiContributors


class ContributorsFromCamagueyQuery(graphene.ObjectType):
    contributors_missing_in_onat_camaguey = graphene.List(CamagueyType, city_name=graphene.String())
    contributors_with_different_information_camaguey = graphene.List(CamagueyType, city_name=graphene.String())
    contributors_with_different_information_camaguey_infogesti = graphene.List(InfogestiContributorsType, city_name=graphene.String())
    contributors_with_equals_information_camaguey = graphene.List(CamagueyType, city_name=graphene.String())
    camaguey = graphene.List(CamagueyType)

    # 1 Contribuyentes que estan en capitania vehiculo que no estan en la onat
    def resolve_contributors_missing_in_onat_camaguey(self, info, city_name=graphene.String()):

        if city_name == 'Carlos Manuel De Cespedes':
            return Camaguey.objects.raw(
                'select distinct * from CORE_CAMAGUEY cmg LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON cmg.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA  = 3001')
        if city_name == 'Esmeralda':
            return Camaguey.objects.raw(
                'select distinct * from CORE_CAMAGUEY cmg LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON cmg.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA  = 3002')
        if city_name == 'Sierra De Cubitas':
            return Camaguey.objects.raw(
                'select distinct * from CORE_CAMAGUEY cmg LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON cmg.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA  = 3003')
        if city_name == 'Minas':
            return Camaguey.objects.raw(
                'select distinct * from CORE_CAMAGUEY cmg LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON cmg.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA  = 3004')
        if city_name == 'Nuevitas':
            return Camaguey.objects.raw(
                'select distinct * from CORE_CAMAGUEY cmg LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON cmg.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA  = 3005')
        if city_name == 'Guaimaro':
            return Camaguey.objects.raw(
                'select distinct * from CORE_CAMAGUEY cmg LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON cmg.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA  = 3006')
        if city_name == 'Sibanicu':
            return Camaguey.objects.raw(
                'select distinct * from CORE_CAMAGUEY cmg LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON cmg.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA  = 3007')
        if city_name == 'Camagüey':
            return Camaguey.objects.raw(
                'select distinct * from CORE_CAMAGUEY cmg LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON cmg.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA  = 3008')
        if city_name == 'Florida':
            return Camaguey.objects.raw(
                'select distinct * from CORE_CAMAGUEY cmg LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON cmg.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA  = 3009')
        if city_name == 'Vertientes':
            return Camaguey.objects.raw(
                'select distinct * from CORE_CAMAGUEY cmg LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON cmg.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA  = 3010')
        if city_name == 'Jimaguayu':
            return Camaguey.objects.raw(
                'select distinct * from CORE_CAMAGUEY cmg LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON cmg.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA  = 3011')
        if city_name == 'Najasa':
            return Camaguey.objects.raw(
                'select distinct * from CORE_CAMAGUEY cmg LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON cmg.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA  = 3012')
        if city_name == 'Santa Cruz del Sur':
            return Camaguey.objects.raw(
                'select distinct * from CORE_CAMAGUEY cmg LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON cmg.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA  = 3013')


    # 2 Contribuyentes que estan en ambos capitania con informaciones diferentes
    def resolve_contributors_with_different_information_camaguey(self, info, city_name=graphene.String()):

        if city_name == 'Carlos Manuel De Cespedes':
            return Camaguey.objects.raw(
                "select distinct * from CORE_CAMAGUEY cmg INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON cmg.NUMEROIDENTIDAD =  info.NIT  and info.UNIDAD = 3001  and DPA = 3001 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT ORDER BY  NUMEROIDENTIDAD")
        if city_name == 'Esmeralda':
            return Camaguey.objects.raw(
                "select distinct * from CORE_CAMAGUEY cmg INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON cmg.NUMEROIDENTIDAD =  info.NIT  and info.UNIDAD = 3002  and DPA = 3002 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT ORDER BY  NUMEROIDENTIDAD")
        if city_name == 'Sierra De Cubitas':
            return Camaguey.objects.raw(
                "select distinct * from CORE_CAMAGUEY cmg INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON cmg.NUMEROIDENTIDAD =  info.NIT  and info.UNIDAD = 3003  and DPA = 3003 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT ORDER BY  NUMEROIDENTIDAD")
        if city_name == 'Minas':
            return Camaguey.objects.raw(
                "select distinct * from CORE_CAMAGUEY cmg INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON cmg.NUMEROIDENTIDAD =  info.NIT  and info.UNIDAD = 3004  and DPA = 3004 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT ORDER BY  NUMEROIDENTIDAD")
        if city_name == 'Nuevitas':
            return Camaguey.objects.raw(
                "select distinct * from CORE_CAMAGUEY cmg INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON cmg.NUMEROIDENTIDAD =  info.NIT  and info.UNIDAD = 3005  and DPA = 3005 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT ORDER BY  NUMEROIDENTIDAD")
        if city_name == 'Guaimaro':
            return Camaguey.objects.raw(
                "select distinct * from CORE_CAMAGUEY cmg INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON cmg.NUMEROIDENTIDAD =  info.NIT  and info.UNIDAD = 3006  and DPA = 3006 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT ORDER BY  NUMEROIDENTIDAD")
        if city_name == 'Sibanicu':
            return Camaguey.objects.raw(
                "select distinct * from CORE_CAMAGUEY cmg INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON cmg.NUMEROIDENTIDAD =  info.NIT  and info.UNIDAD = 3007  and DPA = 3007 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT ORDER BY  NUMEROIDENTIDAD")
        if city_name == 'Camagüey':
            return Camaguey.objects.raw(
                "select distinct * from CORE_CAMAGUEY cmg INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON cmg.NUMEROIDENTIDAD =  info.NIT  and info.UNIDAD = 3008  and DPA = 3008 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT ORDER BY  NUMEROIDENTIDAD")
        if city_name == 'Florida':
            return Camaguey.objects.raw(
                "select distinct * from CORE_CAMAGUEY cmg INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON cmg.NUMEROIDENTIDAD =  info.NIT  and info.UNIDAD = 3009  and DPA = 3009 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT ORDER BY  NUMEROIDENTIDAD")
        if city_name == 'Vertientes':
            return Camaguey.objects.raw(
                "select distinct * from CORE_CAMAGUEY cmg INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON cmg.NUMEROIDENTIDAD =  info.NIT  and info.UNIDAD = 3010  and DPA = 3010 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT ORDER BY  NUMEROIDENTIDAD")
        if city_name == 'Jimaguayu':
            return Camaguey.objects.raw(
                "select distinct * from CORE_CAMAGUEY cmg INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON cmg.NUMEROIDENTIDAD =  info.NIT  and info.UNIDAD = 3011  and DPA = 3011 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT ORDER BY  NUMEROIDENTIDAD")
        if city_name == 'Najasa':
            return Camaguey.objects.raw(
                "select distinct * from CORE_CAMAGUEY cmg INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON cmg.NUMEROIDENTIDAD =  info.NIT  and info.UNIDAD = 3012  and DPA = 3012 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT ORDER BY  NUMEROIDENTIDAD")
        if city_name == 'Santa Cruz del Sur':
            return Camaguey.objects.raw(
                "select distinct * from CORE_CAMAGUEY cmg INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON cmg.NUMEROIDENTIDAD =  info.NIT  and info.UNIDAD = 3013  and DPA = 3013 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT ORDER BY  NUMEROIDENTIDAD")


    def resolve_contributors_with_different_information_camaguey_infogesti(self, info, city_name=graphene.String()):

        if city_name == 'Carlos Manuel De Cespedes':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@infogesti info INNER JOIN CORE_CAMAGUEY cmg ON cmg.NUMEROIDENTIDAD =  info.NIT and info.UNIDAD = 3001 and DPA = 3001 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT ORDER BY  NIT")
        if city_name == 'Esmeralda':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@infogesti info INNER JOIN CORE_CAMAGUEY cmg ON cmg.NUMEROIDENTIDAD =  info.NIT and info.UNIDAD = 3002 and DPA = 3002 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT ORDER BY  NIT")
        if city_name == 'Sierra De Cubitas':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@infogesti info INNER JOIN CORE_CAMAGUEY cmg ON cmg.NUMEROIDENTIDAD =  info.NIT and info.UNIDAD = 3003 and DPA = 3003 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT ORDER BY  NIT")
        if city_name == 'Minas':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@infogesti info INNER JOIN CORE_CAMAGUEY cmg ON cmg.NUMEROIDENTIDAD =  info.NIT and info.UNIDAD = 3004 and DPA = 3004 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT ORDER BY  NIT")
        if city_name == 'Nuevitas':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@infogesti info INNER JOIN CORE_CAMAGUEY cmg ON cmg.NUMEROIDENTIDAD =  info.NIT and info.UNIDAD = 3005 and DPA = 3005 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT ORDER BY  NIT")
        if city_name == 'Guaimaro':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@infogesti info INNER JOIN CORE_CAMAGUEY cmg ON cmg.NUMEROIDENTIDAD =  info.NIT and info.UNIDAD = 3006 and DPA = 3006 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT ORDER BY  NIT")
        if city_name == 'Sibanicu':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@infogesti info INNER JOIN CORE_CAMAGUEY cmg ON cmg.NUMEROIDENTIDAD =  info.NIT and info.UNIDAD = 3007 and DPA = 3007 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT ORDER BY  NIT")
        if city_name == 'Camagüey':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@infogesti info INNER JOIN CORE_CAMAGUEY cmg ON cmg.NUMEROIDENTIDAD =  info.NIT and info.UNIDAD = 3008 and DPA = 3008 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT ORDER BY  NIT")
        if city_name == 'Florida':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@infogesti info INNER JOIN CORE_CAMAGUEY cmg ON cmg.NUMEROIDENTIDAD =  info.NIT and info.UNIDAD = 3009 and DPA = 3009 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT ORDER BY  NIT")
        if city_name == 'Vertientes':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@infogesti info INNER JOIN CORE_CAMAGUEY cmg ON cmg.NUMEROIDENTIDAD =  info.NIT and info.UNIDAD = 3010 and DPA = 3010 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT ORDER BY  NIT")
        if city_name == 'Jimaguayu':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@infogesti info INNER JOIN CORE_CAMAGUEY cmg ON cmg.NUMEROIDENTIDAD =  info.NIT and info.UNIDAD = 3011 and DPA = 3011 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT ORDER BY  NIT")
        if city_name == 'Najasa':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@infogesti info INNER JOIN CORE_CAMAGUEY cmg ON cmg.NUMEROIDENTIDAD =  info.NIT and info.UNIDAD = 3012 and DPA = 3012 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT ORDER BY  NIT")
        if city_name == 'Santa Cruz del Sur':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@infogesti info INNER JOIN CORE_CAMAGUEY cmg ON cmg.NUMEROIDENTIDAD =  info.NIT and info.UNIDAD = 3013 and DPA = 3013 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT ORDER BY  NIT")

    # 4 Contribuyentes totalmente coincidentes
    def resolve_contributors_with_equals_information_camaguey(self, info, city_name=graphene.String()):
        if city_name == 'Carlos Manuel De Cespedes':
            return Camaguey.objects.raw(
                'select distinct * from CORE_CAMAGUEY cmg INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON cmg.NUMEROIDENTIDAD =  info.NIT and DPA = 3001 WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT ORDER BY  NUMEROIDENTIDAD')
        if city_name == 'Esmeralda':
            return Camaguey.objects.raw(
                'select distinct * from CORE_CAMAGUEY cmg INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON cmg.NUMEROIDENTIDAD =  info.NIT and DPA = 3002 WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT ORDER BY  NUMEROIDENTIDAD')
        if city_name == 'Sierra De Cubitas':
            return Camaguey.objects.raw(
                'select distinct * from CORE_CAMAGUEY cmg INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON cmg.NUMEROIDENTIDAD =  info.NIT and DPA = 3003 WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT ORDER BY  NUMEROIDENTIDAD')
        if city_name == 'Minas':
            return Camaguey.objects.raw(
                'select distinct * from CORE_CAMAGUEY cmg INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON cmg.NUMEROIDENTIDAD =  info.NIT and DPA = 3004 WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT ORDER BY  NUMEROIDENTIDAD')
        if city_name == 'Nuevitas':
            return Camaguey.objects.raw(
                'select distinct * from CORE_CAMAGUEY cmg INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON cmg.NUMEROIDENTIDAD =  info.NIT and DPA = 3005 WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT ORDER BY  NUMEROIDENTIDAD')
        if city_name == 'Guaimaro':
            return Camaguey.objects.raw(
                'select distinct * from CORE_CAMAGUEY cmg INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON cmg.NUMEROIDENTIDAD =  info.NIT and DPA = 3006 WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT ORDER BY  NUMEROIDENTIDAD')
        if city_name == 'Sibanicu':
            return Camaguey.objects.raw(
                'select distinct * from CORE_CAMAGUEY cmg INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON cmg.NUMEROIDENTIDAD =  info.NIT and DPA = 3007 WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT ORDER BY  NUMEROIDENTIDAD')
        if city_name == 'Camagüey':
            return Camaguey.objects.raw(
                'select distinct * from CORE_CAMAGUEY cmg INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON cmg.NUMEROIDENTIDAD =  info.NIT and DPA = 3008 WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT ORDER BY  NUMEROIDENTIDAD')
        if city_name == 'Florida':
            return Camaguey.objects.raw(
                'select distinct * from CORE_CAMAGUEY cmg INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON cmg.NUMEROIDENTIDAD =  info.NIT and DPA = 3009 WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT ORDER BY  NUMEROIDENTIDAD')
        if city_name == 'Vertientes':
            return Camaguey.objects.raw(
                'select distinct * from CORE_CAMAGUEY cmg INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON cmg.NUMEROIDENTIDAD =  info.NIT and DPA = 3010 WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT ORDER BY  NUMEROIDENTIDAD')
        if city_name == 'Jimaguayu':
            return Camaguey.objects.raw(
                'select distinct * from CORE_CAMAGUEY cmg INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON cmg.NUMEROIDENTIDAD =  info.NIT and DPA = 3011 WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT ORDER BY  NUMEROIDENTIDAD')
        if city_name == 'Najasa':
            return Camaguey.objects.raw(
                'select distinct * from CORE_CAMAGUEY cmg INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON cmg.NUMEROIDENTIDAD =  info.NIT and DPA = 3012 WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT ORDER BY  NUMEROIDENTIDAD')
        if city_name == 'Santa Cruz del Sur':
            return Camaguey.objects.raw(
                'select distinct * from CORE_CAMAGUEY cmg INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON cmg.NUMEROIDENTIDAD =  info.NIT and DPA = 3013 WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT ORDER BY  NUMEROIDENTIDAD')


    def resolve_camaguey(self, info):
        return Camaguey.objects.all()


schema = graphene.Schema(query=ContributorsFromCamagueyQuery, auto_camelcase=False)
