import graphene
from capitania.apps.api.types.provincias import SanticEspiritudType, SanticEspiritudType
from capitania.apps.core.models import SanticEspiritud,  SanticEspiritud


class ContributorsFromSanticEspiritudQuery(graphene.ObjectType):
    contributors_missing_in_onat_santic_espiritud = graphene.List(SanticEspiritudType, city_name=graphene.String())
    contributors_with_different_information_santic_espiritud_plate = graphene.List(SanticEspiritudType, city_name=graphene.String())
    contributors_with_different_information_santic_espiritud_name = graphene.List(SanticEspiritudType, city_name=graphene.String())
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
    def resolve_contributors_with_different_information_santic_espiritud_plate(self, info, city_name=graphene.String()):

        if city_name == 'Yaguajay':
            return SanticEspiritud.objects.raw(
                "select distinct * from CORE_SANTICESPIRITUD h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2801 and h.DPA = 2801 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> h.CHAPANUEVA")
        if city_name == 'Jatibonico':
            return SanticEspiritud.objects.raw(
                "select distinct * from CORE_SANTICESPIRITUD h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2802 and h.DPA = 2802 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> h.CHAPANUEVA")
        if city_name == 'Taguasco':
            return SanticEspiritud.objects.raw(
                "select distinct * from CORE_SANTICESPIRITUD h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2803 and h.DPA = 2803 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> h.CHAPANUEVA")
        if city_name == 'Cabaiguán':
            return SanticEspiritud.objects.raw(
                "select distinct * from CORE_SANTICESPIRITUD h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2804 and h.DPA = 2804 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> h.CHAPANUEVA")
        if city_name == 'Fomento':
            return SanticEspiritud.objects.raw(
                "select distinct * from CORE_SANTICESPIRITUD h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2805 and h.DPA = 2805 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> h.CHAPANUEVA")
        if city_name == 'Trinidad':
            return SanticEspiritud.objects.raw(
                "select distinct * from CORE_SANTICESPIRITUD h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2806 and h.DPA = 2806 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> h.CHAPANUEVA")
        if city_name == 'Sancti Spiritus':
            return SanticEspiritud.objects.raw(
                "select distinct * from CORE_SANTICESPIRITUD h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2807 and h.DPA = 2807 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> h.CHAPANUEVA")
        if city_name == 'La Sierpe':
            return SanticEspiritud.objects.raw(
                "select distinct * from CORE_SANTICESPIRITUD h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2808 and h.DPA = 2808 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> h.CHAPANUEVA")

    def resolve_contributors_with_different_information_santic_espiritud_name(self, info, city_name=graphene.String()):

        if city_name == 'Yaguajay':
            return SanticEspiritud.objects.raw(
                "select distinct * from CORE_SANTICESPIRITUD h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2801 and h.DPA = 2801 AND cl.NOMBRE_COMPLETO <> h.DATOSPERSONA inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'Jatibonico':
            return SanticEspiritud.objects.raw(
                "select distinct * from CORE_SANTICESPIRITUD h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2802 and h.DPA = 2802 AND cl.NOMBRE_COMPLETO <> h.DATOSPERSONA inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'Taguasco':
            return SanticEspiritud.objects.raw(
                "select distinct * from CORE_SANTICESPIRITUD h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2803 and h.DPA = 2803 AND cl.NOMBRE_COMPLETO <> h.DATOSPERSONA inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'Cabaiguán':
            return SanticEspiritud.objects.raw(
                "select distinct * from CORE_SANTICESPIRITUD h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2804 and h.DPA = 2804 AND cl.NOMBRE_COMPLETO <> h.DATOSPERSONA inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'Fomento':
            return SanticEspiritud.objects.raw(
                "select distinct * from CORE_SANTICESPIRITUD h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2805 and h.DPA = 2805 AND cl.NOMBRE_COMPLETO <> h.DATOSPERSONA inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'Trinidad':
            return SanticEspiritud.objects.raw(
                "select distinct * from CORE_SANTICESPIRITUD h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2806 and h.DPA = 2806 AND cl.NOMBRE_COMPLETO <> h.DATOSPERSONA inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'Sancti Spiritus':
            return SanticEspiritud.objects.raw(
                "select distinct * from CORE_SANTICESPIRITUD h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2807 and h.DPA = 2807 AND cl.NOMBRE_COMPLETO <> h.DATOSPERSONA inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'La Sierpe':
            return SanticEspiritud.objects.raw(
                "select distinct * from CORE_SANTICESPIRITUD h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2808 and h.DPA = 2808 AND cl.NOMBRE_COMPLETO <> h.DATOSPERSONA inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")

    # 4 Contribuyentes totalmente coincidentes
    def resolve_contributors_with_equals_information_santic_espiritud(self, info, city_name=graphene.String()):

        if city_name == 'Yaguajay':
            return SanticEspiritud.objects.raw(
                'select distinct * from CORE_SANTICESPIRITUD h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2801 and h.DPA = 2801 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA = h.CHAPANUEVA order by  h.NUMEROIDENTIDAD')
        if city_name == 'Jatibonico':
            return SanticEspiritud.objects.raw(
                'select distinct * from CORE_SANTICESPIRITUD h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2802 and h.DPA = 2802 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA = h.CHAPANUEVA order by  h.NUMEROIDENTIDAD')
        if city_name == 'Taguasco':
            return SanticEspiritud.objects.raw(
                'select distinct * from CORE_SANTICESPIRITUD h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2803 and h.DPA = 2803 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA = h.CHAPANUEVA order by  h.NUMEROIDENTIDAD')
        if city_name == 'Cabaiguán':
            return SanticEspiritud.objects.raw(
                'select distinct * from CORE_SANTICESPIRITUD h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2804 and h.DPA = 2804 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA = h.CHAPANUEVA order by  h.NUMEROIDENTIDAD')
        if city_name == 'Fomento':
            return SanticEspiritud.objects.raw(
                'select distinct * from CORE_SANTICESPIRITUD h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2805 and h.DPA = 2805 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA = h.CHAPANUEVA order by  h.NUMEROIDENTIDAD')
        if city_name == 'Trinidad':
            return SanticEspiritud.objects.raw(
                'select distinct * from CORE_SANTICESPIRITUD h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2806 and h.DPA = 2806 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA = h.CHAPANUEVA order by  h.NUMEROIDENTIDAD')
        if city_name == 'Sancti Spiritus':
            return SanticEspiritud.objects.raw(
                'select distinct * from CORE_SANTICESPIRITUD h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2807 and h.DPA = 2807 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA = h.CHAPANUEVA order by  h.NUMEROIDENTIDAD')
        if city_name == 'La Sierpe':
            return SanticEspiritud.objects.raw(
                'select distinct * from CORE_SANTICESPIRITUD h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2808 and h.DPA = 2808 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA = h.CHAPANUEVA order by  h.NUMEROIDENTIDAD')

    def resolve_santic_espiritud(self, info):
        return SanticEspiritud.objects.all()


schema = graphene.Schema(query=ContributorsFromSanticEspiritudQuery, auto_camelcase=False)
