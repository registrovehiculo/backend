import graphene
from capitania.apps.api.types.provincias import LasTunasType, LasTunasType
from capitania.apps.core.models import LasTunas, LasTunas


class ContributorsFromLasTunasQuery(graphene.ObjectType):
    contributors_missing_in_onat_las_tunas = graphene.List(LasTunasType, city_name=graphene.String())
    contributors_with_different_information_las_tunas_plate = graphene.List(LasTunasType, city_name=graphene.String())
    contributors_with_different_information_las_tunas_name = graphene.List(LasTunasType, city_name=graphene.String())
    contributors_with_equals_information_las_tunas = graphene.List(LasTunasType, city_name=graphene.String())
    las_tunas = graphene.List(LasTunasType)

    # 1 Contribuyentes que estan en capitania vehiculo que no estan en la onat
    def resolve_contributors_missing_in_onat_las_tunas(self, info, city_name=graphene.String()):
        if city_name == 'Manati':
            return LasTunas.objects.raw(
                'select distinct * from CORE_LASTUNAS l LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON l.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 3101')
        if city_name == 'Puerto Padre':
            return LasTunas.objects.raw(
                'select distinct * from CORE_LASTUNAS l LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON l.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 3102')
        if city_name == 'Jesus Menendez':
            return LasTunas.objects.raw(
                'select distinct * from CORE_LASTUNAS l LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON l.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 3103')
        if city_name == 'Majibacoa':
            return LasTunas.objects.raw(
                'select distinct * from CORE_LASTUNAS l LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON l.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 3104')
        if city_name == 'Las Tunas':
            return LasTunas.objects.raw(
                'select distinct * from CORE_LASTUNAS l LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON l.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 3105')
        if city_name == 'Jobabo':
            return LasTunas.objects.raw(
                'select distinct * from CORE_LASTUNAS l LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON l.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 3106')
        if city_name == 'Colombia':
            return LasTunas.objects.raw(
                'select distinct * from CORE_LASTUNAS l LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON l.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 3107')
        if city_name == 'Amancio':
            return LasTunas.objects.raw(
                'select distinct * from CORE_LASTUNAS l LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON l.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 3108')

    # 2 Contribuyentes que estan en ambos capitania con informaciones diferentes
    def resolve_contributors_with_different_information_las_tunas_plate(self, info, city_name=graphene.String()):
        if city_name == 'Manati':
            return LasTunas.objects.raw(
                "select distinct * from CORE_LASTUNAS h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 3101 and h.DPA = 3101 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> h.CHAPANUEVA")
        if city_name == 'Puerto Padre':
            return LasTunas.objects.raw(
                "select distinct * from CORE_LASTUNAS h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 3102 and h.DPA = 3102 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> h.CHAPANUEVA")
        if city_name == 'Jesus Menendez':
            return LasTunas.objects.raw(
                "select distinct * from CORE_LASTUNAS h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 3103 and h.DPA = 3103 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> h.CHAPANUEVA")
        if city_name == 'Majibacoa':
            return LasTunas.objects.raw(
                "select distinct * from CORE_LASTUNAS h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 3104 and h.DPA = 3104 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> h.CHAPANUEVA")
        if city_name == 'Las Tunas':
            return LasTunas.objects.raw(
                "select distinct * from CORE_LASTUNAS h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 3105 and h.DPA = 3105 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> h.CHAPANUEVA")
        if city_name == 'Jobabo':
            return LasTunas.objects.raw(
                "select distinct * from CORE_LASTUNAS h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 3106 and h.DPA = 3106 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> h.CHAPANUEVA")
        if city_name == 'Colombia':
            return LasTunas.objects.raw(
                "select distinct * from CORE_LASTUNAS h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 3107 and h.DPA = 3107 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> h.CHAPANUEVA")
        if city_name == 'Amancio':
            return LasTunas.objects.raw(
                "select distinct * from CORE_LASTUNAS h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 3108 and h.DPA = 3108 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> h.CHAPANUEVA")


    def resolve_contributors_with_different_information_las_tunas_name(self, info, city_name=graphene.String()):
        if city_name == 'Manati':
            return LasTunas.objects.raw(
                "select distinct * from CORE_LASTUNAS h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 3101 and h.DPA = 3101 AND cl.NOMBRE_COMPLETO <> h.DATOSPERSONA inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'Puerto Padre':
            return LasTunas.objects.raw(
                "select distinct * from CORE_LASTUNAS h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 3102 and h.DPA = 3102 AND cl.NOMBRE_COMPLETO <> h.DATOSPERSONA inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'Jesus Menendez':
            return LasTunas.objects.raw(
                "select distinct * from CORE_LASTUNAS h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 3103 and h.DPA = 3103 AND cl.NOMBRE_COMPLETO <> h.DATOSPERSONA inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'Majibacoa':
            return LasTunas.objects.raw(
                "select distinct * from CORE_LASTUNAS h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 3104 and h.DPA = 3104 AND cl.NOMBRE_COMPLETO <> h.DATOSPERSONA inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'Las Tunas':
            return LasTunas.objects.raw(
                "select distinct * from CORE_LASTUNAS h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 3105 and h.DPA = 3105 AND cl.NOMBRE_COMPLETO <> h.DATOSPERSONA inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'Jobabo':
            return LasTunas.objects.raw(
                "select distinct * from CORE_LASTUNAS h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 3106 and h.DPA = 3106 AND cl.NOMBRE_COMPLETO <> h.DATOSPERSONA inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'Colombia':
            return LasTunas.objects.raw(
                "select distinct * from CORE_LASTUNAS h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 3107 and h.DPA = 3107 AND cl.NOMBRE_COMPLETO <> h.DATOSPERSONA inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'Amancio':
            return LasTunas.objects.raw(
                "select distinct * from CORE_LASTUNAS h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 3108 and h.DPA = 3108 AND cl.NOMBRE_COMPLETO <> h.DATOSPERSONA inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")

    # 4 Contribuyentes totalmente coincidentes
    def resolve_contributors_with_equals_information_las_tunas(self, info, city_name=graphene.String()):
        if city_name == 'Manati':
            return LasTunas.objects.raw(
                'select distinct * from CORE_LASTUNAS h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 3101 and h.DPA = 3101 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA = h.CHAPANUEVA order by  h.NUMEROIDENTIDAD')
        if city_name == 'Puerto Padre':
            return LasTunas.objects.raw(
                'select distinct * from CORE_LASTUNAS h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 3102 and h.DPA = 3102 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA = h.CHAPANUEVA order by  h.NUMEROIDENTIDAD')
        if city_name == 'Jesus Menendez':
            return LasTunas.objects.raw(
                'select distinct * from CORE_LASTUNAS h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 3103 and h.DPA = 3103 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA = h.CHAPANUEVA order by  h.NUMEROIDENTIDAD')
        if city_name == 'Majibacoa':
            return LasTunas.objects.raw(
                'select distinct * from CORE_LASTUNAS h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 3104 and h.DPA = 3104 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA = h.CHAPANUEVA order by  h.NUMEROIDENTIDAD')
        if city_name == 'Las Tunas':
            return LasTunas.objects.raw(
                'select distinct * from CORE_LASTUNAS h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 3105 and h.DPA = 3105 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA = h.CHAPANUEVA order by  h.NUMEROIDENTIDAD')
        if city_name == 'Jobabo':
            return LasTunas.objects.raw(
                'select distinct * from CORE_LASTUNAS h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 3106 and h.DPA = 3106 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA = h.CHAPANUEVA order by  h.NUMEROIDENTIDAD')
        if city_name == 'Colombia':
            return LasTunas.objects.raw(
                'select distinct * from CORE_LASTUNAS h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 3107 and h.DPA = 3107 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA = h.CHAPANUEVA order by  h.NUMEROIDENTIDAD')
        if city_name == 'Amancio':
            return LasTunas.objects.raw(
                'select distinct * from CORE_LASTUNAS h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 3108 and h.DPA = 3108 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA = h.CHAPANUEVA order by  h.NUMEROIDENTIDAD')

    def resolve_las_tunas(self, info):
        return LasTunas.objects.all()


schema = graphene.Schema(query=ContributorsFromLasTunasQuery, auto_camelcase=False)
