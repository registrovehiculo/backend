import operator
from functools import reduce
from itertools import chain
import graphene
from django.db import connection
from django.db.models.query_utils import Q
from capitania.apps.api.types.provincias import IslaDeLaJuventudType, IslaDeLaJuventudType
from capitania.apps.core.models import IslaDeLaJuventud, IslaDeLaJuventud


class ContributorsFromIslaDeLaJuventudQuery(graphene.ObjectType):
    contributors_missing_in_onat_isla_de_la_juventud = graphene.List(IslaDeLaJuventudType, city_name=graphene.String())
    contributors_with_different_information_isla_de_la_juventud_plate = graphene.List(IslaDeLaJuventudType, city_name=graphene.String())
    contributors_with_different_information_isla_de_la_juventud_name = graphene.List(IslaDeLaJuventudType, city_name=graphene.String())
    contributors_with_equals_information_isla_de_la_juventud = graphene.List(IslaDeLaJuventudType, city_name=graphene.String())
    isla_de_la_juventud = graphene.List(IslaDeLaJuventudType)

    # 1 Contribuyentes que estan en capitania vehiculo que no estan en la onat
    def resolve_contributors_missing_in_onat_isla_de_la_juventud(self, info, city_name=graphene.String()):
        isla_de_la_juventud = IslaDeLaJuventud.objects.raw('select distinct * from CORE_ISLADELAJUVENTUD i LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON i.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL')
        return isla_de_la_juventud

    # 2 Contribuyentes que estan en ambos capitania con informaciones diferentes
    def resolve_contributors_with_different_information_isla_de_la_juventud_plate(self, info, city_name=graphene.String()):
        isla_de_la_juventud = IslaDeLaJuventud.objects.raw("select distinct * from CORE_ISLADELAJUVENTUD h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 4001 and h.DPA = 4001 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA <> h.CHAPANUEVA")
        return isla_de_la_juventud

    def resolve_contributors_with_different_information_isla_de_la_juventud_name(self, info, city_name=graphene.String()):
        isla_de_la_juventud = IslaDeLaJuventud.objects.raw("select distinct * from CORE_ISLADELAJUVENTUD h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 4001 and h.DPA = 4001 AND cl.NOMBRE_COMPLETO <> h.DATOSPERSONA inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE")
        return isla_de_la_juventud

    # 4 Contribuyentes totalmente coincidentes
    def resolve_contributors_with_equals_information_isla_de_la_juventud(self, info, city_name=graphene.String()):
        isla_de_la_juventud = IslaDeLaJuventud.objects.raw('select distinct * from CORE_ISLADELAJUVENTUD h inner join CLIENTE@infogesti cl on cl.NIT = h.NUMEROIDENTIDAD AND cl.UNIDAD = 4001 and h.DPA = 4001 inner join CLIENTE_TT@infogesti tt on cl.ID = tt.ID_CLIENTE where tt.MATRICULA = h.CHAPANUEVA order by  h.NUMEROIDENTIDAD')
        return isla_de_la_juventud

    def resolve_isla_de_la_juventud(self, info):
        return IslaDeLaJuventud.objects.all()


schema = graphene.Schema(query=ContributorsFromIslaDeLaJuventudQuery, auto_camelcase=False)
