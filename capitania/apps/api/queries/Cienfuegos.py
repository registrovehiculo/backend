import graphene
from capitania.apps.api.types.provincias import CienfuegosType, CienfuegosType
from capitania.apps.core.models import Cienfuegos, Cienfuegos


class ContributorsFromCienfuegosQuery(graphene.ObjectType):
    contributors_missing_in_onat_cienfuegos = graphene.List(CienfuegosType, city_name=graphene.String())
    contributors_with_different_information_cienfuegos_name = graphene.List(CienfuegosType, city_name=graphene.String())
    contributors_with_different_information_cienfuegos_plate = graphene.List(CienfuegosType, city_name=graphene.String())
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
    def resolve_contributors_with_different_information_cienfuegos_plate(self, info, city_name=graphene.String()):

        if city_name == 'Aguada de Pasajeros':
            return Cienfuegos.objects.raw(
                "select distinct * from CORE_CIENFUEGOS cf inner join CLIENTE@infogesti cl on cl.NIT = cf.NUMEROIDENTIDAD AND cl.UNIDAD = 2701 and cf.DPA = 2701 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> cf.CHAPANUEVA")
        if city_name == 'Rodas':
            return Cienfuegos.objects.raw(
                "select distinct * from CORE_CIENFUEGOS cf inner join CLIENTE@infogesti cl on cl.NIT = cf.NUMEROIDENTIDAD AND cl.UNIDAD = 2702 and cf.DPA = 2702 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> cf.CHAPANUEVA")
        if city_name == 'Palmira':
            return Cienfuegos.objects.raw(
                "select distinct * from CORE_CIENFUEGOS cf inner join CLIENTE@infogesti cl on cl.NIT = cf.NUMEROIDENTIDAD AND cl.UNIDAD = 2703 and cf.DPA = 2703 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> cf.CHAPANUEVA")
        if city_name == 'las Lajas':
            return Cienfuegos.objects.raw(
                "select distinct * from CORE_CIENFUEGOS cf inner join CLIENTE@infogesti cl on cl.NIT = cf.NUMEROIDENTIDAD AND cl.UNIDAD = 2704 and cf.DPA = 2704 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> cf.CHAPANUEVA")
        if city_name == 'Cruces':
            return Cienfuegos.objects.raw(
                "select distinct * from CORE_CIENFUEGOS cf inner join CLIENTE@infogesti cl on cl.NIT = cf.NUMEROIDENTIDAD AND cl.UNIDAD = 2705 and cf.DPA = 2705 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> cf.CHAPANUEVA")
        if city_name == 'Cumanayagua':
            return Cienfuegos.objects.raw(
                "select distinct * from CORE_CIENFUEGOS cf inner join CLIENTE@infogesti cl on cl.NIT = cf.NUMEROIDENTIDAD AND cl.UNIDAD = 2706 and cf.DPA = 2706 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> cf.CHAPANUEVA")
        if city_name == 'Cienfuegos':
            return Cienfuegos.objects.raw(
                "select distinct * from CORE_CIENFUEGOS cf inner join CLIENTE@infogesti cl on cl.NIT = cf.NUMEROIDENTIDAD AND cl.UNIDAD = 2707 and cf.DPA = 2707 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> cf.CHAPANUEVA")
        if city_name == 'Abreus':
            return Cienfuegos.objects.raw(
                "select distinct * from CORE_CIENFUEGOS cf inner join CLIENTE@infogesti cl on cl.NIT = cf.NUMEROIDENTIDAD AND cl.UNIDAD = 2708 and cf.DPA = 2708 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> cf.CHAPANUEVA")

    def resolve_contributors_with_different_information_cienfuegos_name(self, info, city_name=graphene.String()):

        if city_name == 'Aguada de Pasajeros':
            return Cienfuegos.objects.raw(
                "select distinct * from CORE_CIENFUEGOS cf inner join CLIENTE@infogesti cl on cl.NIT = cf.NUMEROIDENTIDAD AND cl.UNIDAD = 2701 and cf.DPA = 2701 AND upper(cl.NOMBRE_COMPLETO) <> upper(cf.DATOSPERSONA) inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'Rodas':
            return Cienfuegos.objects.raw(
                "select distinct * from CORE_CIENFUEGOS cf inner join CLIENTE@infogesti cl on cl.NIT = cf.NUMEROIDENTIDAD AND cl.UNIDAD = 2702 and cf.DPA = 2702 AND upper(cl.NOMBRE_COMPLETO) <> upper(cf.DATOSPERSONA) inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'Palmira':
            return Cienfuegos.objects.raw(
                "select distinct * from CORE_CIENFUEGOS cf inner join CLIENTE@infogesti cl on cl.NIT = cf.NUMEROIDENTIDAD AND cl.UNIDAD = 2703 and cf.DPA = 2703 AND upper(cl.NOMBRE_COMPLETO) <> upper(cf.DATOSPERSONA) inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'las Lajas':
            return Cienfuegos.objects.raw(
                "select distinct * from CORE_CIENFUEGOS cf inner join CLIENTE@infogesti cl on cl.NIT = cf.NUMEROIDENTIDAD AND cl.UNIDAD = 2704 and cf.DPA = 2704 AND upper(cl.NOMBRE_COMPLETO) <> upper(cf.DATOSPERSONA) inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'Cruces':
            return Cienfuegos.objects.raw(
                "select distinct * from CORE_CIENFUEGOS cf inner join CLIENTE@infogesti cl on cl.NIT = cf.NUMEROIDENTIDAD AND cl.UNIDAD = 2705 and cf.DPA = 2705 AND upper(cl.NOMBRE_COMPLETO) <> upper(cf.DATOSPERSONA) inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'Cumanayagua':
            return Cienfuegos.objects.raw(
                "select distinct * from CORE_CIENFUEGOS cf inner join CLIENTE@infogesti cl on cl.NIT = cf.NUMEROIDENTIDAD AND cl.UNIDAD = 2706 and cf.DPA = 2706 AND upper(cl.NOMBRE_COMPLETO) <> upper(cf.DATOSPERSONA) inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'Cienfuegos':
            return Cienfuegos.objects.raw(
                "select distinct * from CORE_CIENFUEGOS cf inner join CLIENTE@infogesti cl on cl.NIT = cf.NUMEROIDENTIDAD AND cl.UNIDAD = 2707 and cf.DPA = 2707 AND upper(cl.NOMBRE_COMPLETO) <> upper(cf.DATOSPERSONA) inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        if city_name == 'Abreus':
            return Cienfuegos.objects.raw(
                "select distinct * from CORE_CIENFUEGOS cf inner join CLIENTE@infogesti cl on cl.NIT = cf.NUMEROIDENTIDAD AND cl.UNIDAD = 2708 and cf.DPA = 2708 AND upper(cl.NOMBRE_COMPLETO) <> upper(cf.DATOSPERSONA) inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")

    # 4 Contribuyentes totalmente coincidentes
    def resolve_contributors_with_equals_information_cienfuegos(self, info, city_name=graphene.String()):
        if city_name == 'Aguada de Pasajeros':
            return Cienfuegos.objects.raw(
                'select distinct * from CORE_CIENFUEGOS h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2701 and h.DPA = 2701 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA = h.CHAPANUEVA order by  h.NUMEROIDENTIDAD')
        if city_name == 'Rodas':
            return Cienfuegos.objects.raw(
                'select distinct * from CORE_CIENFUEGOS h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2702 and h.DPA = 2702 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA = h.CHAPANUEVA order by  h.NUMEROIDENTIDAD')
        if city_name == 'Palmira':
            return Cienfuegos.objects.raw(
                'select distinct * from CORE_CIENFUEGOS h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2703 and h.DPA = 2703 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA = h.CHAPANUEVA order by  h.NUMEROIDENTIDAD')
        if city_name == 'las Lajas':
            return Cienfuegos.objects.raw(
                'select distinct * from CORE_CIENFUEGOS h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2704 and h.DPA = 2704 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA = h.CHAPANUEVA order by  h.NUMEROIDENTIDAD')
        if city_name == 'Cruces':
            return Cienfuegos.objects.raw(
                'select distinct * from CORE_CIENFUEGOS h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2705 and h.DPA = 2705 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA = h.CHAPANUEVA order by  h.NUMEROIDENTIDAD')
        if city_name == 'Cumanayagua':
            return Cienfuegos.objects.raw(
                'select distinct * from CORE_CIENFUEGOS h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2706 and h.DPA = 2706 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA = h.CHAPANUEVA order by  h.NUMEROIDENTIDAD')
        if city_name == 'Cienfuegos':
            return Cienfuegos.objects.raw(
                'select distinct * from CORE_CIENFUEGOS h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2707 and h.DPA = 2707 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA = h.CHAPANUEVA order by  h.NUMEROIDENTIDAD')
        if city_name == 'Abreus':
            return Cienfuegos.objects.raw(
                'select distinct * from CORE_CIENFUEGOS h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 2708 and h.DPA = 2708 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA = h.CHAPANUEVA order by  h.NUMEROIDENTIDAD')

    def resolve_cienfuegos(self, info):
        return Cienfuegos.objects.all()


schema = graphene.Schema(query=ContributorsFromCienfuegosQuery, auto_camelcase=False)
