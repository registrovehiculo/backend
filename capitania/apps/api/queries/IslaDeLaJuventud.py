import operator
from functools import reduce
from itertools import chain
import graphene
from django.db import connection
from django.db.models.query_utils import Q
from capitania.apps.api.types.provincias import IslaDeLaJuventudType, InfogestiContributorsType
from capitania.apps.core.models import IslaDeLaJuventud, InfogestiContributors


class ContributorsFromIslaDeLaJuventudQuery(graphene.ObjectType):
    contributors_missing_in_onat_isla_de_la_juventud = graphene.List(IslaDeLaJuventudType, city_name=graphene.String())
    contributors_with_different_information_isla_de_la_juventud = graphene.List(IslaDeLaJuventudType, city_name=graphene.String())
    contributors_with_different_information_isla_de_la_juventud_infogesti = graphene.List(InfogestiContributorsType, city_name=graphene.String())
    contributors_with_equals_information_isla_de_la_juventud = graphene.List(IslaDeLaJuventudType, city_name=graphene.String())
    isla_de_la_juventud = graphene.List(IslaDeLaJuventudType)

    # 1 Contribuyentes que estan en capitania vehiculo que no estan en la onat
    def resolve_contributors_missing_in_onat_isla_de_la_juventud(self, info, city_name=graphene.String()):
        isla_de_la_juventud = IslaDeLaJuventud.objects.raw('select distinct * from RECA.CORE_ISLADELAJUVENTUD i LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON i.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL')
        return isla_de_la_juventud

    # 2 Contribuyentes que estan en ambos capitania con informaciones diferentes
    def resolve_contributors_with_different_information_isla_de_la_juventud(self, info, city_name=graphene.String()):
        isla_de_la_juventud = IslaDeLaJuventud.objects.raw("select distinct * from RECA.CORE_ISLADELAJUVENTUD i INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON i.NUMEROIDENTIDAD =  info.NIT and info.UNIDAD = 4001 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NUMEROIDENTIDAD")
        return isla_de_la_juventud

    def resolve_contributors_with_different_information_isla_de_la_juventud_infogesti(self, info, city_name=graphene.String()):
        isla_de_la_juventud = InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info INNER JOIN RECA.CORE_ISLADELAJUVENTUD i ON i.NUMEROIDENTIDAD =  info.NIT and info.UNIDAD = 4001 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NIT")
        return isla_de_la_juventud

    # 4 Contribuyentes totalmente coincidentes
    def resolve_contributors_with_equals_information_isla_de_la_juventud(self, info, city_name=graphene.String()):
        isla_de_la_juventud = IslaDeLaJuventud.objects.raw('select distinct * from RECA.CORE_ISLADELAJUVENTUD i INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON i.NUMEROIDENTIDAD =  info.NIT WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT')
        return isla_de_la_juventud

    def resolve_isla_de_la_juventud(self, info):
        return IslaDeLaJuventud.objects.all()


schema = graphene.Schema(query=ContributorsFromIslaDeLaJuventudQuery, auto_camelcase=False)
