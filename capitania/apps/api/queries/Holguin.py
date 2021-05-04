import graphene
from capitania.apps.api.types.provincias import HolguinType, HolguinType
from capitania.apps.core.models import Holguin, Holguin


class ContributorsFromHolguinQuery(graphene.ObjectType):
    contributors_missing_in_onat_holguin = graphene.List(HolguinType, city_name=graphene.String())
    contributors_with_different_information_holguin_plate = graphene.List(HolguinType, city_name=graphene.String())
    contributors_with_different_information_holguin_name = graphene.List(HolguinType, city_name=graphene.String())
    contributors_with_equals_information_holguin = graphene.List(HolguinType, city_name=graphene.String())
    holguin = graphene.List(HolguinType)

    # 1 Contribuyentes que estan en capitania vehiculo que no estan en la onat
    def resolve_contributors_missing_in_onat_holguin(self, info, city_name=graphene.String()):

        if city_name == 'Gibara':
            return Holguin.objects.raw(
                'select distinct * from CORE_HOLGUIN h LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON h.NUMEROIDENTIDAD =  info.NIT WHERE INFOGESTI.IG_CONTRIBUYENTE_PN.NIT IS NULL and DPA = 3201')
        if city_name == 'Rafael Freyre':
            return Holguin.objects.raw(
                'select distinct * from CORE_HOLGUIN h LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON h.NUMEROIDENTIDAD =  info.NIT WHERE INFOGESTI.IG_CONTRIBUYENTE_PN.NIT IS NULL and DPA = 3202')
        if city_name == 'Banes':
            return Holguin.objects.raw(
                'select distinct * from CORE_HOLGUIN h LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON h.NUMEROIDENTIDAD =  info.NIT WHERE INFOGESTI.IG_CONTRIBUYENTE_PN.NIT IS NULL and DPA = 3203')
        if city_name == 'Antilla':
            return Holguin.objects.raw(
                'select distinct * from CORE_HOLGUIN h LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON h.NUMEROIDENTIDAD =  info.NIT WHERE INFOGESTI.IG_CONTRIBUYENTE_PN.NIT IS NULL and DPA = 3204')
        if city_name == 'Baguanos':
            return Holguin.objects.raw(
                'select distinct * from CORE_HOLGUIN h LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON h.NUMEROIDENTIDAD =  info.NIT WHERE INFOGESTI.IG_CONTRIBUYENTE_PN.NIT IS NULL and DPA = 3205')
        if city_name == 'Holguin':
            return Holguin.objects.raw(
                'select distinct * from CORE_HOLGUIN h LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON h.NUMEROIDENTIDAD =  info.NIT WHERE INFOGESTI.IG_CONTRIBUYENTE_PN.NIT IS NULL and DPA = 3206')
        if city_name == 'Calixto Garcia':
            return Holguin.objects.raw(
                'select distinct * from CORE_HOLGUIN h LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON h.NUMEROIDENTIDAD =  info.NIT WHERE INFOGESTI.IG_CONTRIBUYENTE_PN.NIT IS NULL and DPA = 3207')
        if city_name == 'Cacocum':
            return Holguin.objects.raw(
                'select distinct * from CORE_HOLGUIN h LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON h.NUMEROIDENTIDAD =  info.NIT WHERE INFOGESTI.IG_CONTRIBUYENTE_PN.NIT IS NULL and DPA = 3208')
        if city_name == 'Urbano Noris':
            return Holguin.objects.raw(
                'select distinct * from CORE_HOLGUIN h LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON h.NUMEROIDENTIDAD =  info.NIT WHERE INFOGESTI.IG_CONTRIBUYENTE_PN.NIT IS NULL and DPA = 3209')
        if city_name == 'Cueto':
            return Holguin.objects.raw(
                'select distinct * from CORE_HOLGUIN h LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON h.NUMEROIDENTIDAD =  info.NIT WHERE INFOGESTI.IG_CONTRIBUYENTE_PN.NIT IS NULL and DPA = 3210')
        if city_name == 'Mayari':
            return Holguin.objects.raw(
                'select distinct * from CORE_HOLGUIN h LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON h.NUMEROIDENTIDAD =  info.NIT WHERE INFOGESTI.IG_CONTRIBUYENTE_PN.NIT IS NULL and DPA = 3211')
        if city_name == 'Frank Pais':
            return Holguin.objects.raw(
                'select distinct * from CORE_HOLGUIN h LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON h.NUMEROIDENTIDAD =  info.NIT WHERE INFOGESTI.IG_CONTRIBUYENTE_PN.NIT IS NULL and DPA = 3212')
        if city_name == 'Sagua de Tanamo':
            return Holguin.objects.raw(
                'select distinct * from CORE_HOLGUIN h LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON h.NUMEROIDENTIDAD =  info.NIT WHERE INFOGESTI.IG_CONTRIBUYENTE_PN.NIT IS NULL and DPA = 3213')
        if city_name == 'Moa':
            return Holguin.objects.raw(
                'select distinct * from CORE_HOLGUIN h LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON h.NUMEROIDENTIDAD =  info.NIT WHERE INFOGESTI.IG_CONTRIBUYENTE_PN.NIT IS NULL and DPA = 3214')


    # 2 Contribuyentes que estan en ambos capitania con informaciones diferentes
    def resolve_contributors_with_different_information_holguin_plate(self, info, city_name=graphene.String()):

        if city_name == 'Gibara':
            return Holguin.objects.raw(
                "select distinct * from CORE_HOLGUIN h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 3201 and h.DPA = 3201 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> h.CHAPANUEVA")
        if city_name == 'Rafael Freyre':
            return Holguin.objects.raw(
                "select distinct * from CORE_HOLGUIN h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 3202 and h.DPA = 3202 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> h.CHAPANUEVA")
        if city_name == 'Banes':
            return Holguin.objects.raw(
                "select distinct * from CORE_HOLGUIN h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 3203 and h.DPA = 3203 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> h.CHAPANUEVA")
        if city_name == 'Antilla':
            return Holguin.objects.raw(
                "select distinct * from CORE_HOLGUIN h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 3204 and h.DPA = 3204 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> h.CHAPANUEVA")
        if city_name == 'Baguanos':
            return Holguin.objects.raw(
                "select distinct * from CORE_HOLGUIN h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 3205 and h.DPA = 3205 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> h.CHAPANUEVA")
        if city_name == 'Holguin':
            return Holguin.objects.raw(
                "select distinct * from CORE_HOLGUIN h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 3206 and h.DPA = 3206 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> h.CHAPANUEVA")
        if city_name == 'Calixto Garcia':
            return Holguin.objects.raw(
                "select distinct * from CORE_HOLGUIN h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 3207 and h.DPA = 3207 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> h.CHAPANUEVA")
        if city_name == 'Cacocum':
            return Holguin.objects.raw(
                "select distinct * from CORE_HOLGUIN h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 3208 and h.DPA = 3208 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> h.CHAPANUEVA")
        if city_name == 'Urbano Noris':
            return Holguin.objects.raw(
                "select distinct * from CORE_HOLGUIN h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 3209 and h.DPA = 3209 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> h.CHAPANUEVA")
        if city_name == 'Cueto':
            return Holguin.objects.raw(
                "select distinct * from CORE_HOLGUIN h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 3210 and h.DPA = 3210 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> h.CHAPANUEVA")
        if city_name == 'Mayari':
            return Holguin.objects.raw(
                "select distinct * from CORE_HOLGUIN h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 3211 and h.DPA = 3211 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> h.CHAPANUEVA")
        if city_name == 'Frank Pais':
            return Holguin.objects.raw(
                "select distinct * from CORE_HOLGUIN h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 3212 and h.DPA = 3212 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> h.CHAPANUEVA")
        if city_name == 'Sagua de Tanamo':
            return Holguin.objects.raw(
                "select distinct * from CORE_HOLGUIN h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 3213 and h.DPA = 3213 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> h.CHAPANUEVA")
        if city_name == 'Moa':
            return Holguin.objects.raw(
                "select distinct * from CORE_HOLGUIN h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 3214 and h.DPA = 3214 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> h.CHAPANUEVA")

    def resolve_contributors_with_different_information_holguin_name(self, info, city_name=graphene.String()):

        if city_name == 'Gibara':
            return Holguin.objects.raw(
                "select distinct * from CORE_HOLGUIN h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 3201 and h.DPA = 3201 AND cl.NOMBRE_COMPLETO <> h.DATOSPERSONA inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'Rafael Freyre':
            return Holguin.objects.raw(
                "select distinct * from CORE_HOLGUIN h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 3202 and h.DPA = 3202 AND cl.NOMBRE_COMPLETO <> h.DATOSPERSONA inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'Banes':
            return Holguin.objects.raw(
                "select distinct * from CORE_HOLGUIN h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 3203 and h.DPA = 3203 AND cl.NOMBRE_COMPLETO <> h.DATOSPERSONA inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'Antilla':
            return Holguin.objects.raw(
                "select distinct * from CORE_HOLGUIN h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 3204 and h.DPA = 3204 AND cl.NOMBRE_COMPLETO <> h.DATOSPERSONA inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'Baguanos':
            return Holguin.objects.raw(
                "select distinct * from CORE_HOLGUIN h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 3205 and h.DPA = 3205 AND cl.NOMBRE_COMPLETO <> h.DATOSPERSONA inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'Holguin':
            return Holguin.objects.raw(
                "select distinct * from CORE_HOLGUIN h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 3206 and h.DPA = 3206 AND cl.NOMBRE_COMPLETO <> h.DATOSPERSONA inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'Calixto Garcia':
            return Holguin.objects.raw(
                "select distinct * from CORE_HOLGUIN h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 3207 and h.DPA = 3207 AND cl.NOMBRE_COMPLETO <> h.DATOSPERSONA inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'Cacocum':
            return Holguin.objects.raw(
                "select distinct * from CORE_HOLGUIN h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 3208 and h.DPA = 3208 AND cl.NOMBRE_COMPLETO <> h.DATOSPERSONA inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'Urbano Noris':
            return Holguin.objects.raw(
                "select distinct * from CORE_HOLGUIN h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 3209 and h.DPA = 3209 AND cl.NOMBRE_COMPLETO <> h.DATOSPERSONA inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'Cueto':
            return Holguin.objects.raw(
                "select distinct * from CORE_HOLGUIN h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 3210 and h.DPA = 3210 AND cl.NOMBRE_COMPLETO <> h.DATOSPERSONA inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'Mayari':
            return Holguin.objects.raw(
                "select distinct * from CORE_HOLGUIN h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 3211 and h.DPA = 3211 AND cl.NOMBRE_COMPLETO <> h.DATOSPERSONA inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'Frank Pais':
            return Holguin.objects.raw(
                "select distinct * from CORE_HOLGUIN h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 3212 and h.DPA = 3212 AND cl.NOMBRE_COMPLETO <> h.DATOSPERSONA inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'Sagua de Tanamo':
            return Holguin.objects.raw(
                "select distinct * from CORE_HOLGUIN h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 3213 and h.DPA = 3213 AND cl.NOMBRE_COMPLETO <> h.DATOSPERSONA inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'Moa':
            return Holguin.objects.raw(
                "select distinct * from CORE_HOLGUIN h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 3214 and h.DPA = 3214 AND cl.NOMBRE_COMPLETO <> h.DATOSPERSONA inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")


    # 4 Contribuyentes totalmente coincidentes
    def resolve_contributors_with_equals_information_holguin(self, info, city_name=graphene.String()):

        if city_name == 'Gibara':
            return Holguin.objects.raw(
                'select distinct * from CORE_HOLGUIN h INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON h.NUMEROIDENTIDAD =  info.NIT and DPA = 3201 WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT order by NUMEROIDENTIDAD')
        if city_name == 'Rafael Freyre':
            return Holguin.objects.raw(
                'select distinct * from CORE_HOLGUIN h INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON h.NUMEROIDENTIDAD =  info.NIT and DPA = 3202 WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT order by NUMEROIDENTIDAD')
        if city_name == 'Banes':
            return Holguin.objects.raw(
                'select distinct * from CORE_HOLGUIN h INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON h.NUMEROIDENTIDAD =  info.NIT and DPA = 3203 WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT order by NUMEROIDENTIDAD')
        if city_name == 'Antilla':
            return Holguin.objects.raw(
                'select distinct * from CORE_HOLGUIN h INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON h.NUMEROIDENTIDAD =  info.NIT and DPA = 3204 WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT order by NUMEROIDENTIDAD')
        if city_name == 'Baguanos':
            return Holguin.objects.raw(
                'select distinct * from CORE_HOLGUIN h INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON h.NUMEROIDENTIDAD =  info.NIT and DPA = 3205 WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT order by NUMEROIDENTIDAD')
        if city_name == 'Holguin':
            return Holguin.objects.raw(
                'select distinct * from CORE_HOLGUIN h INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON h.NUMEROIDENTIDAD =  info.NIT and DPA = 3206 WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT order by NUMEROIDENTIDAD')
        if city_name == 'Calixto Garcia':
            return Holguin.objects.raw(
                'select distinct * from CORE_HOLGUIN h INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON h.NUMEROIDENTIDAD =  info.NIT and DPA = 3207 WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT order by NUMEROIDENTIDAD')
        if city_name == 'Cacocum':
            return Holguin.objects.raw(
                'select distinct * from CORE_HOLGUIN h INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON h.NUMEROIDENTIDAD =  info.NIT and DPA = 3208 WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT order by NUMEROIDENTIDAD')
        if city_name == 'Urbano Noris':
            return Holguin.objects.raw(
                'select distinct * from CORE_HOLGUIN h INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON h.NUMEROIDENTIDAD =  info.NIT and DPA = 3209 WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT order by NUMEROIDENTIDAD')
        if city_name == 'Cueto':
            return Holguin.objects.raw(
                'select distinct * from CORE_HOLGUIN h INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON h.NUMEROIDENTIDAD =  info.NIT and DPA = 3210 WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT order by NUMEROIDENTIDAD')
        if city_name == 'Mayari':
            return Holguin.objects.raw(
                'select distinct * from CORE_HOLGUIN h INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON h.NUMEROIDENTIDAD =  info.NIT and DPA = 3211 WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT order by NUMEROIDENTIDAD')
        if city_name == 'Frank Pais':
            return Holguin.objects.raw(
                'select distinct * from CORE_HOLGUIN h INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON h.NUMEROIDENTIDAD =  info.NIT and DPA = 3212 WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT order by NUMEROIDENTIDAD')
        if city_name == 'Sagua de Tanamo':
            return Holguin.objects.raw(
                'select distinct * from CORE_HOLGUIN h INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON h.NUMEROIDENTIDAD =  info.NIT and DPA = 3213 WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT order by NUMEROIDENTIDAD')
        if city_name == 'Moa':
            return Holguin.objects.raw(
                'select distinct * from CORE_HOLGUIN h INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON h.NUMEROIDENTIDAD =  info.NIT and DPA = 3214 WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT order by NUMEROIDENTIDAD')

    def resolve_holguin(self, info):
        return Holguin.objects.all()


schema = graphene.Schema(query=ContributorsFromHolguinQuery, auto_camelcase=False)
