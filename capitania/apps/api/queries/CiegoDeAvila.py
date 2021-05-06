import graphene
from capitania.apps.api.types.provincias import CiegoDeAvilaType, CiegoDeAvilaType
from capitania.apps.core.models import CiegoDeAvila, CiegoDeAvila


class ContributorsFromCiegoDeAvilaQuery(graphene.ObjectType):
    contributors_missing_in_onat_ciego = graphene.List(CiegoDeAvilaType, city_name=graphene.String())
    contributors_with_different_information_ciego_plate = graphene.List(CiegoDeAvilaType, city_name=graphene.String())
    contributors_with_different_information_ciego_name = graphene.List(CiegoDeAvilaType, city_name=graphene.String())
    contributors_with_equals_information_ciego = graphene.List(CiegoDeAvilaType, city_name=graphene.String())
    ciego = graphene.List(CiegoDeAvilaType)

    # 1 Contribuyentes que estan en capitania vehiculo que no estan en la onat
    def resolve_contributors_missing_in_onat_ciego(self, info, city_name=graphene.String()):

        if city_name == 'Chambas':
            return CiegoDeAvila.objects.raw(
                'select distinct * from CORE_CIEGODEAVILA cav LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON cav.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2901')
        if city_name == 'Moron':
            return CiegoDeAvila.objects.raw(
                'select distinct * from CORE_CIEGODEAVILA cav LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON cav.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2902')
        if city_name == 'Bolivia':
            return CiegoDeAvila.objects.raw(
                'select distinct * from CORE_CIEGODEAVILA cav LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON cav.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2903')
        if city_name == 'Primero De Enero':
            return CiegoDeAvila.objects.raw(
                'select distinct * from CORE_CIEGODEAVILA cav LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON cav.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2904')
        if city_name == 'Ciro Redondo':
            return CiegoDeAvila.objects.raw(
                'select distinct * from CORE_CIEGODEAVILA cav LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON cav.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2905')
        if city_name == 'Florencia':
            return CiegoDeAvila.objects.raw(
                'select distinct * from CORE_CIEGODEAVILA cav LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON cav.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2906')
        if city_name == 'Majagua':
            return CiegoDeAvila.objects.raw(
                'select distinct * from CORE_CIEGODEAVILA cav LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON cav.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2907')
        if city_name == 'Ciego de Avila':
            return CiegoDeAvila.objects.raw(
                'select distinct * from CORE_CIEGODEAVILA cav LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON cav.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2908')
        if city_name == 'Venezuela':
            return CiegoDeAvila.objects.raw(
                'select distinct * from CORE_CIEGODEAVILA cav LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON cav.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2909')
        if city_name == 'Baragua':
            return CiegoDeAvila.objects.raw(
                'select distinct * from CORE_CIEGODEAVILA cav LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON cav.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2910')

    # 2 Contribuyentes que estan en ambos capitania con informaciones diferentes
    def resolve_contributors_with_different_information_ciego_plate(self, info, city_name=graphene.String()):

        if city_name == 'Chambas':
            return CiegoDeAvila.objects.raw(
                "select distinct * from CORE_CIEGODEAVILA cg inner join CLIENTE@infogesti cl on cl.NIT = cg.NUMEROIDENTIDAD AND cl.UNIDAD = 2901 and cg.DPA = 2901 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> cg.CHAPANUEVA")
        if city_name == 'Moron':
            return CiegoDeAvila.objects.raw(
                "select distinct * from CORE_CIEGODEAVILA cg inner join CLIENTE@infogesti cl on cl.NIT = cg.NUMEROIDENTIDAD AND cl.UNIDAD = 2902 and cg.DPA = 2902 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> cg.CHAPANUEVA")
        if city_name == 'Bolivia':
            return CiegoDeAvila.objects.raw(
                "select distinct * from CORE_CIEGODEAVILA cg inner join CLIENTE@infogesti cl on cl.NIT = cg.NUMEROIDENTIDAD AND cl.UNIDAD = 2903 and cg.DPA = 2903 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> cg.CHAPANUEVA")
        if city_name == 'Primero De Enero':
            return CiegoDeAvila.objects.raw(
                "select distinct * from CORE_CIEGODEAVILA cg inner join CLIENTE@infogesti cl on cl.NIT = cg.NUMEROIDENTIDAD AND cl.UNIDAD = 2904 and cg.DPA = 2904 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> cg.CHAPANUEVA")
        if city_name == 'Ciro Redondo':
            return CiegoDeAvila.objects.raw(
                "select distinct * from CORE_CIEGODEAVILA cg inner join CLIENTE@infogesti cl on cl.NIT = cg.NUMEROIDENTIDAD AND cl.UNIDAD = 2905 and cg.DPA = 2905 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> cg.CHAPANUEVA")
        if city_name == 'Florencia':
            return CiegoDeAvila.objects.raw(
                "select distinct * from CORE_CIEGODEAVILA cg inner join CLIENTE@infogesti cl on cl.NIT = cg.NUMEROIDENTIDAD AND cl.UNIDAD = 2906 and cg.DPA = 2906 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> cg.CHAPANUEVA")
        if city_name == 'Majagua':
            return CiegoDeAvila.objects.raw(
                "select distinct * from CORE_CIEGODEAVILA cg inner join CLIENTE@infogesti cl on cl.NIT = cg.NUMEROIDENTIDAD AND cl.UNIDAD = 2907 and cg.DPA = 2907 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> cg.CHAPANUEVA")
        if city_name == 'Ciego de Avila':
            return CiegoDeAvila.objects.raw(
                "select distinct * from CORE_CIEGODEAVILA cg inner join CLIENTE@infogesti cl on cl.NIT = cg.NUMEROIDENTIDAD AND cl.UNIDAD = 2908 and cg.DPA = 2908 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> cg.CHAPANUEVA")
        if city_name == 'Venezuela':
            return CiegoDeAvila.objects.raw(
                "select distinct * from CORE_CIEGODEAVILA cg inner join CLIENTE@infogesti cl on cl.NIT = cg.NUMEROIDENTIDAD AND cl.UNIDAD = 2909 and cg.DPA = 2909 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> cg.CHAPANUEVA")
        if city_name == 'Baragua':
            return CiegoDeAvila.objects.raw(
                "select distinct * from CORE_CIEGODEAVILA cg inner join CLIENTE@infogesti cl on cl.NIT = cg.NUMEROIDENTIDAD AND cl.UNIDAD = 2910 and cg.DPA = 2910 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> cg.CHAPANUEVA")


    def resolve_contributors_with_different_information_ciego_name(self, info, city_name=graphene.String()):

        if city_name == 'Chambas':
            return CiegoDeAvila.objects.raw(
                "select distinct * from CORE_CIEGODEAVILA cg inner join CLIENTE@infogesti cl on cl.NIT = cg.NUMEROIDENTIDAD AND cl.UNIDAD = 2901 and cg.DPA = 2901 AND upper(cl.NOMBRE_COMPLETO) <> upper(cg.DATOSPERSONA) inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'Moron':
            return CiegoDeAvila.objects.raw(
                "select distinct * from CORE_CIEGODEAVILA cg inner join CLIENTE@infogesti cl on cl.NIT = cg.NUMEROIDENTIDAD AND cl.UNIDAD = 2902 and cg.DPA = 2902 AND upper(cl.NOMBRE_COMPLETO) <> upper(cg.DATOSPERSONA) inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'Bolivia':
            return CiegoDeAvila.objects.raw(
                "select distinct * from CORE_CIEGODEAVILA cg inner join CLIENTE@infogesti cl on cl.NIT = cg.NUMEROIDENTIDAD AND cl.UNIDAD = 2903 and cg.DPA = 2903 AND upper(cl.NOMBRE_COMPLETO) <> upper(cg.DATOSPERSONA) inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'Primero De Enero':
            return CiegoDeAvila.objects.raw(
                "select distinct * from CORE_CIEGODEAVILA cg inner join CLIENTE@infogesti cl on cl.NIT = cg.NUMEROIDENTIDAD AND cl.UNIDAD = 2904 and cg.DPA = 2904 AND upper(cl.NOMBRE_COMPLETO) <> upper(cg.DATOSPERSONA) inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'Ciro Redondo':
            return CiegoDeAvila.objects.raw(
                "select distinct * from CORE_CIEGODEAVILA cg inner join CLIENTE@infogesti cl on cl.NIT = cg.NUMEROIDENTIDAD AND cl.UNIDAD = 2905 and cg.DPA = 2905 AND upper(cl.NOMBRE_COMPLETO) <> upper(cg.DATOSPERSONA) inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'Florencia':
            return CiegoDeAvila.objects.raw(
                "select distinct * from CORE_CIEGODEAVILA cg inner join CLIENTE@infogesti cl on cl.NIT = cg.NUMEROIDENTIDAD AND cl.UNIDAD = 2906 and cg.DPA = 2906 AND upper(cl.NOMBRE_COMPLETO) <> upper(cg.DATOSPERSONA) inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'Majagua':
            return CiegoDeAvila.objects.raw(
                "select distinct * from CORE_CIEGODEAVILA cg inner join CLIENTE@infogesti cl on cl.NIT = cg.NUMEROIDENTIDAD AND cl.UNIDAD = 2907 and cg.DPA = 2907 AND upper(cl.NOMBRE_COMPLETO) <> upper(cg.DATOSPERSONA) inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'Ciego de Avila':
            return CiegoDeAvila.objects.raw(
                "select distinct * from CORE_CIEGODEAVILA cg inner join CLIENTE@infogesti cl on cl.NIT = cg.NUMEROIDENTIDAD AND cl.UNIDAD = 2908 and cg.DPA = 2908 AND upper(cl.NOMBRE_COMPLETO) <> upper(cg.DATOSPERSONA) inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'Venezuela':
            return CiegoDeAvila.objects.raw(
                "select distinct * from CORE_CIEGODEAVILA cg inner join CLIENTE@infogesti cl on cl.NIT = cg.NUMEROIDENTIDAD AND cl.UNIDAD = 2909 and cg.DPA = 2909 AND upper(cl.NOMBRE_COMPLETO) <> upper(cg.DATOSPERSONA) inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'Baragua':
            return CiegoDeAvila.objects.raw(
                "select distinct * from CORE_CIEGODEAVILA cg inner join CLIENTE@infogesti cl on cl.NIT = cg.NUMEROIDENTIDAD AND cl.UNIDAD = 2910 and cg.DPA = 2910 AND upper(cl.NOMBRE_COMPLETO) <> upper(cg.DATOSPERSONA) inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")


    # 4 Contribuyentes totalmente coincidentes
    def resolve_contributors_with_equals_information_ciego(self, info, city_name=graphene.String()):

        if city_name == 'Chambas':
            return CiegoDeAvila.objects.raw(
                'select distinct * from CORE_CIEGODEAVILA h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2901 and h.DPA = 2901 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA = h.CHAPANUEVA order by  h.NUMEROIDENTIDAD')
        if city_name == 'Moron':
            return CiegoDeAvila.objects.raw(
                'select distinct * from CORE_CIEGODEAVILA h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2902 and h.DPA = 2902 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA = h.CHAPANUEVA order by  h.NUMEROIDENTIDAD')
        if city_name == 'Bolivia':
            return CiegoDeAvila.objects.raw(
                'select distinct * from CORE_CIEGODEAVILA h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2903 and h.DPA = 2903 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA = h.CHAPANUEVA order by  h.NUMEROIDENTIDAD')
        if city_name == 'Primero De Enero':
            return CiegoDeAvila.objects.raw(
                'select distinct * from CORE_CIEGODEAVILA h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2904 and h.DPA = 2904 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA = h.CHAPANUEVA order by  h.NUMEROIDENTIDAD')
        if city_name == 'Ciro Redondo':
            return CiegoDeAvila.objects.raw(
                'select distinct * from CORE_CIEGODEAVILA h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2905 and h.DPA = 2905 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA = h.CHAPANUEVA order by  h.NUMEROIDENTIDAD')
        if city_name == 'Florencia':
            return CiegoDeAvila.objects.raw(
                'select distinct * from CORE_CIEGODEAVILA h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2906 and h.DPA = 2906 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA = h.CHAPANUEVA order by  h.NUMEROIDENTIDAD')
        if city_name == 'Majagua':
            return CiegoDeAvila.objects.raw(
                'select distinct * from CORE_CIEGODEAVILA h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2907 and h.DPA = 2907 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA = h.CHAPANUEVA order by  h.NUMEROIDENTIDAD')
        if city_name == 'Ciego de Avila':
            return CiegoDeAvila.objects.raw(
                'select distinct * from CORE_CIEGODEAVILA h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2908 and h.DPA = 2908 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA = h.CHAPANUEVA order by  h.NUMEROIDENTIDAD')
        if city_name == 'Venezuela':
            return CiegoDeAvila.objects.raw(
                'select distinct * from CORE_CIEGODEAVILA h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2909 and h.DPA = 2909 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA = h.CHAPANUEVA order by  h.NUMEROIDENTIDAD')
        if city_name == 'Baragua':
            return CiegoDeAvila.objects.raw(
                'select distinct * from CORE_CIEGODEAVILA h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2910 and h.DPA = 2910 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA = h.CHAPANUEVA order by  h.NUMEROIDENTIDAD')

    def resolve_ciego(self, info):
        return CiegoDeAvila.objects.all()


schema = graphene.Schema(query=ContributorsFromCiegoDeAvilaQuery, auto_camelcase=False)
