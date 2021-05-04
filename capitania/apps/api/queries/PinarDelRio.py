import graphene
from capitania.apps.api.types.provincias import PinarDelRioType, PinarDelRioType
from capitania.apps.core.models import PinarDelRio, PinarDelRio


class ContributorsFromPinarQuery(graphene.ObjectType):
    contributors_missing_in_onat_pinar = graphene.List(PinarDelRioType, city_name=graphene.String())
    contributors_with_different_information_pinar_plate = graphene.List(PinarDelRioType, city_name=graphene.String())
    contributors_with_different_information_pinar_name = graphene.List(PinarDelRioType, city_name=graphene.String())
    contributors_with_equals_information_pinar = graphene.List(PinarDelRioType, city_name=graphene.String())
    pinar_del_rio = graphene.List(PinarDelRioType)

    # 1 Contribuyentes que estan en capitania vehiculo que no estan en la onat
    def resolve_contributors_missing_in_onat_pinar(self, info, city_name=graphene.String()):

        if city_name == 'Sandino':
            return PinarDelRio.objects.raw(
                'select distinct * from CORE_PINARDELRIO p LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON p.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2101')
        if city_name == 'Mantua':
            return PinarDelRio.objects.raw(
                'select distinct * from CORE_PINARDELRIO p LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON p.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2102')
        if city_name == 'Minas De Matahambre':
            return PinarDelRio.objects.raw(
                'select distinct * from CORE_PINARDELRIO p LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON p.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2103')
        if city_name == 'Viñales':
            return PinarDelRio.objects.raw(
                'select distinct * from CORE_PINARDELRIO p LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON p.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2104')
        if city_name == 'La Palma':
            return PinarDelRio.objects.raw(
                'select distinct * from CORE_PINARDELRIO p LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON p.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2105')
        if city_name == 'Los Palacios':
            return PinarDelRio.objects.raw(
                'select distinct * from CORE_PINARDELRIO p LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON p.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2106')
        if city_name == 'Consolacion del Sur':
            return PinarDelRio.objects.raw(
                'select distinct * from CORE_PINARDELRIO p LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON p.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2107')
        if city_name == 'Pinar del Rio':
            return PinarDelRio.objects.raw(
                'select distinct * from CORE_PINARDELRIO p LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON p.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2108')
        if city_name == 'San Luis':
            return PinarDelRio.objects.raw(
                'select distinct * from CORE_PINARDELRIO p LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON p.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2109')
        if city_name == 'San Juan y Martinez':
            return PinarDelRio.objects.raw(
                'select distinct * from CORE_PINARDELRIO p LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON p.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2110')
        if city_name == 'Guane':
            return PinarDelRio.objects.raw(
                'select distinct * from CORE_PINARDELRIO p LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON p.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2111')


    # 2 Contribuyentes que estan en ambos capitania con informaciones diferentes
    def resolve_contributors_with_different_information_pinar_plate(self, info, city_name=graphene.String()):

        if city_name == 'Sandino':
            return PinarDelRio.objects.raw(
                "select distinct * from CORE_PINARDELRIO h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2101 and h.DPA = 2101 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> h.CHAPANUEVA")
        if city_name == 'Mantua':
            return PinarDelRio.objects.raw(
                "select distinct * from CORE_PINARDELRIO h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2102 and h.DPA = 2102 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> h.CHAPANUEVA")
        if city_name == 'Minas De Matahambre':
            return PinarDelRio.objects.raw(
                "select distinct * from CORE_PINARDELRIO h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2103 and h.DPA = 2103 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> h.CHAPANUEVA")
        if city_name == 'Viñales':
            return PinarDelRio.objects.raw(
                "select distinct * from CORE_PINARDELRIO h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2104 and h.DPA = 2104 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> h.CHAPANUEVA")
        if city_name == 'La Palma':
            return PinarDelRio.objects.raw(
                "select distinct * from CORE_PINARDELRIO h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2105 and h.DPA = 2105 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> h.CHAPANUEVA")
        if city_name == 'Los Palacios':
            return PinarDelRio.objects.raw(
                "select distinct * from CORE_PINARDELRIO h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2106 and h.DPA = 2106 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> h.CHAPANUEVA")
        if city_name == 'Consolacion del Sur':
            return PinarDelRio.objects.raw(
                "select distinct * from CORE_PINARDELRIO h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2107 and h.DPA = 2107 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> h.CHAPANUEVA")
        if city_name == 'Pinar del Rio':
            return PinarDelRio.objects.raw(
                "select distinct * from CORE_PINARDELRIO h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2108 and h.DPA = 2108 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> h.CHAPANUEVA")
        if city_name == 'San Luis':
            return PinarDelRio.objects.raw(
                "select distinct * from CORE_PINARDELRIO h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2109 and h.DPA = 2109 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> h.CHAPANUEVA")
        if city_name == 'San Juan y Martinez':
            return PinarDelRio.objects.raw(
                "select distinct * from CORE_PINARDELRIO h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2110 and h.DPA = 2110 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> h.CHAPANUEVA")
        if city_name == 'Guane':
            return PinarDelRio.objects.raw(
                "select distinct * from CORE_PINARDELRIO h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2111 and h.DPA = 2111 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> h.CHAPANUEVA")


    def resolve_contributors_with_different_information_pinar_name(self, info, city_name=graphene.String()):

        if city_name == 'Sandino':
            return PinarDelRio.objects.raw(
                "select distinct * from CORE_PINARDELRIO h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2101 and h.DPA = 2101 AND cl.NOMBRE_COMPLETO <> h.DATOSPERSONA inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'Mantua':
            return PinarDelRio.objects.raw(
                "select distinct * from CORE_PINARDELRIO h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2102 and h.DPA = 2102 AND cl.NOMBRE_COMPLETO <> h.DATOSPERSONA inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'Minas De Matahambre':
            return PinarDelRio.objects.raw(
                "select distinct * from CORE_PINARDELRIO h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2103 and h.DPA = 2103 AND cl.NOMBRE_COMPLETO <> h.DATOSPERSONA inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'Viñales':
            return PinarDelRio.objects.raw(
                "select distinct * from CORE_PINARDELRIO h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2104 and h.DPA = 2104 AND cl.NOMBRE_COMPLETO <> h.DATOSPERSONA inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'La Palma':
            return PinarDelRio.objects.raw(
                "select distinct * from CORE_PINARDELRIO h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2105 and h.DPA = 2105 AND cl.NOMBRE_COMPLETO <> h.DATOSPERSONA inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'Los Palacios':
            return PinarDelRio.objects.raw(
                "select distinct * from CORE_PINARDELRIO h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2106 and h.DPA = 2106 AND cl.NOMBRE_COMPLETO <> h.DATOSPERSONA inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'Consolacion del Sur':
            return PinarDelRio.objects.raw(
                "select distinct * from CORE_PINARDELRIO h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2107 and h.DPA = 2107 AND cl.NOMBRE_COMPLETO <> h.DATOSPERSONA inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'Pinar del Rio':
            return PinarDelRio.objects.raw(
                "select distinct * from CORE_PINARDELRIO h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2108 and h.DPA = 2108 AND cl.NOMBRE_COMPLETO <> h.DATOSPERSONA inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'San Luis':
            return PinarDelRio.objects.raw(
                "select distinct * from CORE_PINARDELRIO h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2109 and h.DPA = 2109 AND cl.NOMBRE_COMPLETO <> h.DATOSPERSONA inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'San Juan y Martinez':
            return PinarDelRio.objects.raw(
                "select distinct * from CORE_PINARDELRIO h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2110 and h.DPA = 2110 AND cl.NOMBRE_COMPLETO <> h.DATOSPERSONA inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'Guane':
            return PinarDelRio.objects.raw(
                "select distinct * from CORE_PINARDELRIO h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2111 and h.DPA = 2111 AND cl.NOMBRE_COMPLETO <> h.DATOSPERSONA inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")

    # 4 Contribuyentes totalmente coincidentes
    def resolve_contributors_with_equals_information_pinar(self, info, city_name=graphene.String()):

        if city_name == 'Sandino':
            return PinarDelRio.objects.raw(
                'select distinct * from CORE_PINARDELRIO p INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON p.NUMEROIDENTIDAD =  info.NIT WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT  and DPA = 2101 order by NUMEROIDENTIDAD')
        if city_name == 'Mantua':
            return PinarDelRio.objects.raw(
                'select distinct * from CORE_PINARDELRIO p INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON p.NUMEROIDENTIDAD =  info.NIT WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT  and DPA = 2102 order by NUMEROIDENTIDAD')
        if city_name == 'Minas De Matahambre':
            return PinarDelRio.objects.raw(
                'select distinct * from CORE_PINARDELRIO p INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON p.NUMEROIDENTIDAD =  info.NIT WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT  and DPA = 2103 order by NUMEROIDENTIDAD')
        if city_name == 'Viñales':
            return PinarDelRio.objects.raw(
                'select distinct * from CORE_PINARDELRIO p INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON p.NUMEROIDENTIDAD =  info.NIT WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT  and DPA = 2104 order by NUMEROIDENTIDAD')
        if city_name == 'La Palma':
            return PinarDelRio.objects.raw(
                'select distinct * from CORE_PINARDELRIO p INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON p.NUMEROIDENTIDAD =  info.NIT WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT  and DPA = 2105 order by NUMEROIDENTIDAD')
        if city_name == 'Los Palacios':
            return PinarDelRio.objects.raw(
                'select distinct * from CORE_PINARDELRIO p INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON p.NUMEROIDENTIDAD =  info.NIT WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT  and DPA = 2106 order by NUMEROIDENTIDAD')
        if city_name == 'Consolacion del Sur':
            return PinarDelRio.objects.raw(
                'select distinct * from CORE_PINARDELRIO p INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON p.NUMEROIDENTIDAD =  info.NIT WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT  and DPA = 2107 order by NUMEROIDENTIDAD')
        if city_name == 'Pinar del Rio':
            return PinarDelRio.objects.raw(
                'select distinct * from CORE_PINARDELRIO p INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON p.NUMEROIDENTIDAD =  info.NIT WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT  and DPA = 2108 order by NUMEROIDENTIDAD')
        if city_name == 'San Luis':
            return PinarDelRio.objects.raw(
                'select distinct * from CORE_PINARDELRIO p INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON p.NUMEROIDENTIDAD =  info.NIT WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT  and DPA = 2109 order by NUMEROIDENTIDAD')
        if city_name == 'San Juan y Martinez':
            return PinarDelRio.objects.raw(
                'select distinct * from CORE_PINARDELRIO p INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON p.NUMEROIDENTIDAD =  info.NIT WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT  and DPA = 2110 order by NUMEROIDENTIDAD')
        if city_name == 'Guane':
            return PinarDelRio.objects.raw(
                'select distinct * from CORE_PINARDELRIO p INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON p.NUMEROIDENTIDAD =  info.NIT WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT  and DPA = 2111 order by NUMEROIDENTIDAD')


    def resolve_pinar_del_rio(self, info):
        return PinarDelRio.objects.all()


schema = graphene.Schema(query=ContributorsFromPinarQuery, auto_camelcase=False)
