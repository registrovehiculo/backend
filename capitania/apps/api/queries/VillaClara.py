import graphene
from capitania.apps.api.types.provincias import VillaClaraType, VillaClaraType
from capitania.apps.core.models import VillaClara, VillaClara


class ContributorsFromVillaClaraQuery(graphene.ObjectType):
    contributors_missing_in_onat_villa_clara = graphene.List(VillaClaraType, city_name=graphene.String())
    contributors_with_different_information_villa_clara_plate = graphene.List(VillaClaraType, city_name=graphene.String())
    contributors_with_different_information_villa_clara_name = graphene.List(VillaClaraType, city_name=graphene.String())
    contributors_with_equals_information_villa_clara = graphene.List(VillaClaraType, city_name=graphene.String())
    villa_clara = graphene.List(VillaClaraType)

    # 1 Contribuyentes que estan en capitania vehiculo que no estan en la onat
    def resolve_contributors_missing_in_onat_villa_clara(self, info, city_name=graphene.String()):

        if city_name == 'Corralillo':
            return VillaClara.objects.raw(
                'select * from RECA.CORE_VILLACLARA v LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON v.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2601')
        if city_name == 'Quemado de Güines':
            return VillaClara.objects.raw(
                'select * from RECA.CORE_VILLACLARA v LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON v.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2602')
        if city_name == 'Sagua la Grande':
            return VillaClara.objects.raw(
                'select * from RECA.CORE_VILLACLARA v LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON v.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2603')
        if city_name == 'Encrucijada':
            return VillaClara.objects.raw(
                'select * from RECA.CORE_VILLACLARA v LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON v.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2604')
        if city_name == 'Camajuaní':
            return VillaClara.objects.raw(
                'select * from RECA.CORE_VILLACLARA v LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON v.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2605')
        if city_name == 'Caibarién':
            return VillaClara.objects.raw(
                'select * from RECA.CORE_VILLACLARA v LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON v.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2606')
        if city_name == 'San Juan de los Remedios':
            return VillaClara.objects.raw(
                'select * from RECA.CORE_VILLACLARA v LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON v.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2607')
        if city_name == 'Placetas':
            return VillaClara.objects.raw(
                'select * from RECA.CORE_VILLACLARA v LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON v.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2608')
        if city_name == 'Santa Clara':
            return VillaClara.objects.raw(
                'select * from RECA.CORE_VILLACLARA v LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON v.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2609')
        if city_name == 'Cifuentes':
            return VillaClara.objects.raw(
                'select * from RECA.CORE_VILLACLARA v LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON v.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2610')
        if city_name == 'Santo Domingo':
            return VillaClara.objects.raw(
                'select * from RECA.CORE_VILLACLARA v LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON v.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2611')
        if city_name == 'Ranchuelo':
            return VillaClara.objects.raw(
                'select * from RECA.CORE_VILLACLARA v LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON v.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2612')
        if city_name == 'Manicaragua':
            return VillaClara.objects.raw(
                'select * from RECA.CORE_VILLACLARA v LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON v.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2613')

    # 2 Contribuyentes que estan en ambos capitania con informaciones diferentes
    def resolve_contributors_with_different_information_villa_clara_plate(self, info, city_name=graphene.String()):

        if city_name == 'Corralillo':
            return VillaClara.objects.raw(
                "select distinct * from CORE_VILLACLARA h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2601 and h.DPA = 2601 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> h.CHAPANUEVA")
        if city_name == 'Quemado de Güines':
            return VillaClara.objects.raw(
                "select distinct * from CORE_VILLACLARA h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2602 and h.DPA = 2602 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> h.CHAPANUEVA")
        if city_name == 'Sagua la Grande':
            return VillaClara.objects.raw(
                "select distinct * from CORE_VILLACLARA h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2603 and h.DPA = 2603 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> h.CHAPANUEVA")
        if city_name == 'Encrucijada':
            return VillaClara.objects.raw(
                "select distinct * from CORE_VILLACLARA h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2604 and h.DPA = 2604 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> h.CHAPANUEVA")
        if city_name == 'Camajuaní':
            return VillaClara.objects.raw(
                "select distinct * from CORE_VILLACLARA h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2605 and h.DPA = 2605 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> h.CHAPANUEVA")
        if city_name == 'Caibarién':
            return VillaClara.objects.raw(
                "select distinct * from CORE_VILLACLARA h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2606 and h.DPA = 2606 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> h.CHAPANUEVA")
        if city_name == 'San Juan de los Remedios':
            return VillaClara.objects.raw(
                "select distinct * from CORE_VILLACLARA h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2607 and h.DPA = 2607 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> h.CHAPANUEVA")
        if city_name == 'Placetas':
            return VillaClara.objects.raw(
                "select distinct * from CORE_VILLACLARA h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2608 and h.DPA = 2608 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> h.CHAPANUEVA")
        if city_name == 'Santa Clara':
            return VillaClara.objects.raw(
                "select distinct * from CORE_VILLACLARA h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2609 and h.DPA = 2609 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> h.CHAPANUEVA")
        if city_name == 'Cifuentes':
            return VillaClara.objects.raw(
                "select distinct * from CORE_VILLACLARA h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2610 and h.DPA = 2610 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> h.CHAPANUEVA")
        if city_name == 'Santo Domingo':
            return VillaClara.objects.raw(
                "select distinct * from CORE_VILLACLARA h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2611 and h.DPA = 2611 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> h.CHAPANUEVA")
        if city_name == 'Ranchuelo':
            return VillaClara.objects.raw(
                "select distinct * from CORE_VILLACLARA h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2612 and h.DPA = 2612 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> h.CHAPANUEVA")
        if city_name == 'Manicaragua':
            return VillaClara.objects.raw(
                "select distinct * from CORE_VILLACLARA h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2613 and h.DPA = 2613 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> h.CHAPANUEVA")

    def resolve_contributors_with_different_information_villa_clara_name(self, info, city_name=graphene.String()):

        if city_name == 'Corralillo':
            return VillaClara.objects.raw(
                "select distinct * from CORE_VILLACLARA h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2601 and h.DPA = 2601 AND cl.NOMBRE_COMPLETO <> h.DATOSPERSONA inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'Quemado de Güines':
            return VillaClara.objects.raw(
                "select distinct * from CORE_VILLACLARA h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2602 and h.DPA = 2602 AND cl.NOMBRE_COMPLETO <> h.DATOSPERSONA inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'Sagua la Grande':
            return VillaClara.objects.raw(
                "select distinct * from CORE_VILLACLARA h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2603 and h.DPA = 2603 AND cl.NOMBRE_COMPLETO <> h.DATOSPERSONA inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'Encrucijada':
            return VillaClara.objects.raw(
                "select distinct * from CORE_VILLACLARA h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2604 and h.DPA = 2604 AND cl.NOMBRE_COMPLETO <> h.DATOSPERSONA inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'Camajuaní':
            return VillaClara.objects.raw(
                "select distinct * from CORE_VILLACLARA h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2605 and h.DPA = 2605 AND cl.NOMBRE_COMPLETO <> h.DATOSPERSONA inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'Caibarién':
            return VillaClara.objects.raw(
                "select distinct * from CORE_VILLACLARA h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2606 and h.DPA = 2606 AND cl.NOMBRE_COMPLETO <> h.DATOSPERSONA inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'San Juan de los Remedios':
            return VillaClara.objects.raw(
                "select distinct * from CORE_VILLACLARA h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2607 and h.DPA = 2607 AND cl.NOMBRE_COMPLETO <> h.DATOSPERSONA inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'Placetas':
            return VillaClara.objects.raw(
                "select distinct * from CORE_VILLACLARA h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2608 and h.DPA = 2608 AND cl.NOMBRE_COMPLETO <> h.DATOSPERSONA inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'Santa Clara':
            return VillaClara.objects.raw(
                "select distinct * from CORE_VILLACLARA h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2609 and h.DPA = 2609 AND cl.NOMBRE_COMPLETO <> h.DATOSPERSONA inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'Cifuentes':
            return VillaClara.objects.raw(
                "select distinct * from CORE_VILLACLARA h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2610 and h.DPA = 2610 AND cl.NOMBRE_COMPLETO <> h.DATOSPERSONA inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'Santo Domingo':
            return VillaClara.objects.raw(
                "select distinct * from CORE_VILLACLARA h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2611 and h.DPA = 2611 AND cl.NOMBRE_COMPLETO <> h.DATOSPERSONA inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'Ranchuelo':
            return VillaClara.objects.raw(
                "select distinct * from CORE_VILLACLARA h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2612 and h.DPA = 2612 AND cl.NOMBRE_COMPLETO <> h.DATOSPERSONA inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'Manicaragua':
            return VillaClara.objects.raw(
                "select distinct * from CORE_VILLACLARA h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2613 and h.DPA = 2613 AND cl.NOMBRE_COMPLETO <> h.DATOSPERSONA inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")

    # 4 Contribuyentes totalmente coincidentes
    def resolve_contributors_with_equals_information_villa_clara(self, info, city_name=graphene.String()):

        if city_name == 'Corralillo':
            return VillaClara.objects.raw(
                'select * from RECA.CORE_VILLACLARA v INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON v.NUMEROIDENTIDAD =  info.NIT WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT and DPA = 2601 order by NUMEROIDENTIDAD')
        if city_name == 'Quemado de Güines':
            return VillaClara.objects.raw(
                'select * from RECA.CORE_VILLACLARA v INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON v.NUMEROIDENTIDAD =  info.NIT WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT and DPA = 2602 order by NUMEROIDENTIDAD')
        if city_name == 'Sagua la Grande':
            return VillaClara.objects.raw(
                'select * from RECA.CORE_VILLACLARA v INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON v.NUMEROIDENTIDAD =  info.NIT WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT and DPA = 2603 order by NUMEROIDENTIDAD')
        if city_name == 'Encrucijada':
            return VillaClara.objects.raw(
                'select * from RECA.CORE_VILLACLARA v INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON v.NUMEROIDENTIDAD =  info.NIT WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT and DPA = 2604 order by NUMEROIDENTIDAD')
        if city_name == 'Camajuaní':
            return VillaClara.objects.raw(
                'select * from RECA.CORE_VILLACLARA v INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON v.NUMEROIDENTIDAD =  info.NIT WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT and DPA = 2605 order by NUMEROIDENTIDAD')
        if city_name == 'Caibarién':
            return VillaClara.objects.raw(
                'select * from RECA.CORE_VILLACLARA v INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON v.NUMEROIDENTIDAD =  info.NIT WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT and DPA = 2606 order by NUMEROIDENTIDAD')
        if city_name == 'San Juan de los Remedios':
            return VillaClara.objects.raw(
                'select * from RECA.CORE_VILLACLARA v INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON v.NUMEROIDENTIDAD =  info.NIT WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT and DPA = 2607 order by NUMEROIDENTIDAD')
        if city_name == 'Placetas':
            return VillaClara.objects.raw(
                'select * from RECA.CORE_VILLACLARA v INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON v.NUMEROIDENTIDAD =  info.NIT WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT and DPA = 2608 order by NUMEROIDENTIDAD')
        if city_name == 'Santa Clara':
            return VillaClara.objects.raw(
                'select * from RECA.CORE_VILLACLARA v INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON v.NUMEROIDENTIDAD =  info.NIT WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT and DPA = 2609 order by NUMEROIDENTIDAD')
        if city_name == 'Cifuentes':
            return VillaClara.objects.raw(
                'select * from RECA.CORE_VILLACLARA v INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON v.NUMEROIDENTIDAD =  info.NIT WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT and DPA = 2610 order by NUMEROIDENTIDAD')
        if city_name == 'Santo Domingo':
            return VillaClara.objects.raw(
                'select * from RECA.CORE_VILLACLARA v INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON v.NUMEROIDENTIDAD =  info.NIT WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT and DPA = 2611 order by NUMEROIDENTIDAD')
        if city_name == 'Ranchuelo':
            return VillaClara.objects.raw(
                'select * from RECA.CORE_VILLACLARA v INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON v.NUMEROIDENTIDAD =  info.NIT WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT and DPA = 2612 order by NUMEROIDENTIDAD')
        if city_name == 'Manicaragua':
            return VillaClara.objects.raw(
                'select * from RECA.CORE_VILLACLARA v INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON v.NUMEROIDENTIDAD =  info.NIT WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT and DPA = 2613 order by NUMEROIDENTIDAD')

    def resolve_villa_clara(self, info):
        return VillaClara.objects.all()


schema = graphene.Schema(query=ContributorsFromVillaClaraQuery, auto_camelcase=False)
