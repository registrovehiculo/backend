import graphene
from capitania.apps.api.types.provincias import  CamagueyType
from capitania.apps.core.models import Camaguey


class ContributorsFromCamagueyQuery(graphene.ObjectType):
    contributors_missing_in_onat_camaguey = graphene.List(CamagueyType, city_name=graphene.String())
    contributors_with_different_information_camaguey_plate = graphene.List(CamagueyType, city_name=graphene.String())
    contributors_with_different_information_camaguey_name = graphene.List(CamagueyType, city_name=graphene.String())
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
    def resolve_contributors_with_different_information_camaguey_plate(self, info, city_name=graphene.String()):

        if city_name == 'Carlos Manuel De Cespedes':
            return Camaguey.objects.raw(
                "select distinct * from CORE_CAMAGUEY cm inner join CLIENTE@infogesti cl on cl.NIT = cm.NUMEROIDENTIDAD AND cl.UNIDAD = 3001 and cm.DPA = 3001 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> cm.CHAPANUEVA")
        if city_name == 'Esmeralda':
            return Camaguey.objects.raw(
                "select distinct * from CORE_CAMAGUEY cm inner join CLIENTE@infogesti cl on cl.NIT = cm.NUMEROIDENTIDAD AND cl.UNIDAD = 3002 and cm.DPA = 3002 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> cm.CHAPANUEVA")
        if city_name == 'Sierra De Cubitas':
            return Camaguey.objects.raw(
                "select distinct * from CORE_CAMAGUEY cm inner join CLIENTE@infogesti cl on cl.NIT = cm.NUMEROIDENTIDAD AND cl.UNIDAD = 3003 and cm.DPA = 3003 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> cm.CHAPANUEVA")
        if city_name == 'Minas':
            return Camaguey.objects.raw(
                "select distinct * from CORE_CAMAGUEY cm inner join CLIENTE@infogesti cl on cl.NIT = cm.NUMEROIDENTIDAD AND cl.UNIDAD = 3004 and cm.DPA = 3004 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> cm.CHAPANUEVA")
        if city_name == 'Nuevitas':
            return Camaguey.objects.raw(
                "select distinct * from CORE_CAMAGUEY cm inner join CLIENTE@infogesti cl on cl.NIT = cm.NUMEROIDENTIDAD AND cl.UNIDAD = 3005 and cm.DPA = 3005 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> cm.CHAPANUEVA")
        if city_name == 'Guaimaro':
            return Camaguey.objects.raw(
                "select distinct * from CORE_CAMAGUEY cm inner join CLIENTE@infogesti cl on cl.NIT = cm.NUMEROIDENTIDAD AND cl.UNIDAD = 3006 and cm.DPA = 3006 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> cm.CHAPANUEVA")
        if city_name == 'Sibanicu':
            return Camaguey.objects.raw(
                "select distinct * from CORE_CAMAGUEY cm inner join CLIENTE@infogesti cl on cl.NIT = cm.NUMEROIDENTIDAD AND cl.UNIDAD = 3007 and cm.DPA = 3007 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> cm.CHAPANUEVA")
        if city_name == 'Camagüey':
            return Camaguey.objects.raw(
                "select distinct * from CORE_CAMAGUEY cm inner join CLIENTE@infogesti cl on cl.NIT = cm.NUMEROIDENTIDAD AND cl.UNIDAD = 3008 and cm.DPA = 3008 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> cm.CHAPANUEVA")
        if city_name == 'Florida':
            return Camaguey.objects.raw(
                "select distinct * from CORE_CAMAGUEY cm inner join CLIENTE@infogesti cl on cl.NIT = cm.NUMEROIDENTIDAD AND cl.UNIDAD = 3009 and cm.DPA = 3009 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> cm.CHAPANUEVA")
        if city_name == 'Vertientes':
            return Camaguey.objects.raw(
                "select distinct * from CORE_CAMAGUEY cm inner join CLIENTE@infogesti cl on cl.NIT = cm.NUMEROIDENTIDAD AND cl.UNIDAD = 3010 and cm.DPA = 3010 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> cm.CHAPANUEVA")
        if city_name == 'Jimaguayu':
            return Camaguey.objects.raw(
                "select distinct * from CORE_CAMAGUEY cm inner join CLIENTE@infogesti cl on cl.NIT = cm.NUMEROIDENTIDAD AND cl.UNIDAD = 3011 and cm.DPA = 3011 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> cm.CHAPANUEVA")
        if city_name == 'Najasa':
            return Camaguey.objects.raw(
                "select distinct * from CORE_CAMAGUEY cm inner join CLIENTE@infogesti cl on cl.NIT = cm.NUMEROIDENTIDAD AND cl.UNIDAD = 3012 and cm.DPA = 3012 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> cm.CHAPANUEVA")
        if city_name == 'Santa Cruz del Sur':
            return Camaguey.objects.raw(
                "select distinct * from CORE_CAMAGUEY cm inner join CLIENTE@infogesti cl on cl.NIT = cm.NUMEROIDENTIDAD AND cl.UNIDAD = 3013 and cm.DPA = 3013 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> cm.CHAPANUEVA")


    def resolve_contributors_with_different_information_camaguey_name(self, info, city_name=graphene.String()):

        if city_name == 'Carlos Manuel De Cespedes':
            return Camaguey.objects.raw(
                "select distinct * from CORE_CAMAGUEY cm inner join CLIENTE@infogesti cl on cl.NIT = cm.NUMEROIDENTIDAD AND cl.UNIDAD = 3001 and cm.DPA = 3001 and cl.NOMBRE_COMPLETO <> cm.DATOSPERSONA inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'Esmeralda':
            return Camaguey.objects.raw(
                "select distinct * from CORE_CAMAGUEY cm inner join CLIENTE@infogesti cl on cl.NIT = cm.NUMEROIDENTIDAD AND cl.UNIDAD = 3002 and cm.DPA = 3002 AND cl.NOMBRE_COMPLETO <> cm.DATOSPERSONA inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'Sierra De Cubitas':
            return Camaguey.objects.raw(
                "select distinct * from CORE_CAMAGUEY cm inner join CLIENTE@infogesti cl on cl.NIT = cm.NUMEROIDENTIDAD AND cl.UNIDAD = 3003 and cm.DPA = 3003 AND cl.NOMBRE_COMPLETO <> cm.DATOSPERSONA inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'Minas':
            return Camaguey.objects.raw(
                "select distinct * from CORE_CAMAGUEY cm inner join CLIENTE@infogesti cl on cl.NIT = cm.NUMEROIDENTIDAD AND cl.UNIDAD = 3004 and cm.DPA = 3004 AND cl.NOMBRE_COMPLETO <> cm.DATOSPERSONA inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'Nuevitas':
            return Camaguey.objects.raw(
                "select distinct * from CORE_CAMAGUEY cm inner join CLIENTE@infogesti cl on cl.NIT = cm.NUMEROIDENTIDAD AND cl.UNIDAD = 3005 and cm.DPA = 3005 AND cl.NOMBRE_COMPLETO <> cm.DATOSPERSONA inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'Guaimaro':
            return Camaguey.objects.raw(
                "select distinct * from CORE_CAMAGUEY cm inner join CLIENTE@infogesti cl on cl.NIT = cm.NUMEROIDENTIDAD AND cl.UNIDAD = 3006 and cm.DPA = 3006 AND cl.NOMBRE_COMPLETO <> cm.DATOSPERSONA inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'Sibanicu':
            return Camaguey.objects.raw(
                "select distinct * from CORE_CAMAGUEY cm inner join CLIENTE@infogesti cl on cl.NIT = cm.NUMEROIDENTIDAD AND cl.UNIDAD = 3007 and cm.DPA = 3007 AND cl.NOMBRE_COMPLETO <> cm.DATOSPERSONA inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'Camagüey':
            return Camaguey.objects.raw(
                "select distinct * from CORE_CAMAGUEY cm inner join CLIENTE@infogesti cl on cl.NIT = cm.NUMEROIDENTIDAD AND cl.UNIDAD = 3008 and cm.DPA = 3008 AND cl.NOMBRE_COMPLETO <> cm.DATOSPERSONA inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'Florida':
            return Camaguey.objects.raw(
                "select distinct * from CORE_CAMAGUEY cm inner join CLIENTE@infogesti cl on cl.NIT = cm.NUMEROIDENTIDAD AND cl.UNIDAD = 3009 and cm.DPA = 3009 AND cl.NOMBRE_COMPLETO <> cm.DATOSPERSONA inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'Vertientes':
            return Camaguey.objects.raw(
                "select distinct * from CORE_CAMAGUEY cm inner join CLIENTE@infogesti cl on cl.NIT = cm.NUMEROIDENTIDAD AND cl.UNIDAD = 3010 and cm.DPA = 3010 AND cl.NOMBRE_COMPLETO <> cm.DATOSPERSONA inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'Jimaguayu':
            return Camaguey.objects.raw(
                "select distinct * from CORE_CAMAGUEY cm inner join CLIENTE@infogesti cl on cl.NIT = cm.NUMEROIDENTIDAD AND cl.UNIDAD = 3011 and cm.DPA = 3011 AND cl.NOMBRE_COMPLETO <> cm.DATOSPERSONA inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'Najasa':
            return Camaguey.objects.raw(
                "select distinct * from CORE_CAMAGUEY cm inner join CLIENTE@infogesti cl on cl.NIT = cm.NUMEROIDENTIDAD AND cl.UNIDAD = 3012 and cm.DPA = 3012 AND cl.NOMBRE_COMPLETO <> cm.DATOSPERSONA inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'Santa Cruz del Sur':
            return Camaguey.objects.raw(
                "select distinct * from CORE_CAMAGUEY cm inner join CLIENTE@infogesti cl on cl.NIT = cm.NUMEROIDENTIDAD AND cl.UNIDAD = 3013 and cm.DPA = 3013 AND cl.NOMBRE_COMPLETO <> cm.DATOSPERSONA inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")

    # 4 Contribuyentes totalmente coincidentes
    def resolve_contributors_with_equals_information_camaguey(self, info, city_name=graphene.String()):
        if city_name == 'Carlos Manuel De Cespedes':
            return Camaguey.objects.raw(
                'select distinct * from CORE_CAMAGUEY h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 3001 and h.DPA = 3001 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA = h.CHAPANUEVA order by  h.NUMEROIDENTIDAD')
        if city_name == 'Esmeralda':
            return Camaguey.objects.raw(
                'select distinct * from CORE_CAMAGUEY h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 3002 and h.DPA = 3002 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA = h.CHAPANUEVA order by  h.NUMEROIDENTIDAD')
        if city_name == 'Sierra De Cubitas':
            return Camaguey.objects.raw(
                'select distinct * from CORE_CAMAGUEY h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 3003 and h.DPA = 3003 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA = h.CHAPANUEVA order by  h.NUMEROIDENTIDAD')
        if city_name == 'Minas':
            return Camaguey.objects.raw(
                'select distinct * from CORE_CAMAGUEY h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 3004 and h.DPA = 3004 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA = h.CHAPANUEVA order by  h.NUMEROIDENTIDAD')
        if city_name == 'Nuevitas':
            return Camaguey.objects.raw(
                'select distinct * from CORE_CAMAGUEY h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 3005 and h.DPA = 3005 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA = h.CHAPANUEVA order by  h.NUMEROIDENTIDAD')
        if city_name == 'Guaimaro':
            return Camaguey.objects.raw(
                'select distinct * from CORE_CAMAGUEY h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 3006 and h.DPA = 3006 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA = h.CHAPANUEVA order by  h.NUMEROIDENTIDAD')
        if city_name == 'Sibanicu':
            return Camaguey.objects.raw(
                'select distinct * from CORE_CAMAGUEY h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 3007 and h.DPA = 3007 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA = h.CHAPANUEVA order by  h.NUMEROIDENTIDAD')
        if city_name == 'Camagüey':
            return Camaguey.objects.raw(
                'select distinct * from CORE_CAMAGUEY h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 3008 and h.DPA = 3008 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA = h.CHAPANUEVA order by  h.NUMEROIDENTIDAD')
        if city_name == 'Florida':
            return Camaguey.objects.raw(
                'select distinct * from CORE_CAMAGUEY h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 3009 and h.DPA = 3009 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA = h.CHAPANUEVA order by  h.NUMEROIDENTIDAD')
        if city_name == 'Vertientes':
            return Camaguey.objects.raw(
                'select distinct * from CORE_CAMAGUEY h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 3010 and h.DPA = 3010 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA = h.CHAPANUEVA order by  h.NUMEROIDENTIDAD')
        if city_name == 'Jimaguayu':
            return Camaguey.objects.raw(
                'select distinct * from CORE_CAMAGUEY h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 3011 and h.DPA = 3011 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA = h.CHAPANUEVA order by  h.NUMEROIDENTIDAD')
        if city_name == 'Najasa':
            return Camaguey.objects.raw(
                'select distinct * from CORE_CAMAGUEY h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 3012 and h.DPA = 3012 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA = h.CHAPANUEVA order by  h.NUMEROIDENTIDAD')
        if city_name == 'Santa Cruz del Sur':
            return Camaguey.objects.raw(
                'select distinct * from CORE_CAMAGUEY h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 3013 and h.DPA = 3013 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA = h.CHAPANUEVA order by  h.NUMEROIDENTIDAD')


    def resolve_camaguey(self, info):
        return Camaguey.objects.all()


schema = graphene.Schema(query=ContributorsFromCamagueyQuery, auto_camelcase=False)
