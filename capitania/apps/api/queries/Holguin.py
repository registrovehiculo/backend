import graphene
from capitania.apps.api.types.provincias import HolguinType, InfogestiContributorsType
from capitania.apps.core.models import Holguin, InfogestiContributors


class ContributorsFromHolguinQuery(graphene.ObjectType):
    contributors_missing_in_onat_holguin = graphene.List(HolguinType, city_name=graphene.String())
    contributors_with_different_information_holguin = graphene.List(HolguinType, city_name=graphene.String())
    contributors_with_different_information_holguin_infogesti = graphene.List(InfogestiContributorsType, city_name=graphene.String())
    contributors_with_equals_information_holguin = graphene.List(HolguinType, city_name=graphene.String())
    holguin = graphene.List(HolguinType)

    # 1 Contribuyentes que estan en capitania vehiculo que no estan en la onat
    def resolve_contributors_missing_in_onat_holguin(self, info, city_name=graphene.String()):

        if city_name == 'Gibara':
            return Holguin.objects.raw(
                'select distinct * from RECA.CORE_HOLGUIN h LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON h.NUMEROIDENTIDAD =  info.NIT WHERE INFOGESTI.IG_CONTRIBUYENTE_PN.NIT IS NULL and DPA = 3201')
        if city_name == 'Rafael Freyre':
            return Holguin.objects.raw(
                'select distinct * from RECA.CORE_HOLGUIN h LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON h.NUMEROIDENTIDAD =  info.NIT WHERE INFOGESTI.IG_CONTRIBUYENTE_PN.NIT IS NULL and DPA = 3202')
        if city_name == 'Banes':
            return Holguin.objects.raw(
                'select distinct * from RECA.CORE_HOLGUIN h LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON h.NUMEROIDENTIDAD =  info.NIT WHERE INFOGESTI.IG_CONTRIBUYENTE_PN.NIT IS NULL and DPA = 3203')
        if city_name == 'Antilla':
            return Holguin.objects.raw(
                'select distinct * from RECA.CORE_HOLGUIN h LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON h.NUMEROIDENTIDAD =  info.NIT WHERE INFOGESTI.IG_CONTRIBUYENTE_PN.NIT IS NULL and DPA = 3204')
        if city_name == 'Baguanos':
            return Holguin.objects.raw(
                'select distinct * from RECA.CORE_HOLGUIN h LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON h.NUMEROIDENTIDAD =  info.NIT WHERE INFOGESTI.IG_CONTRIBUYENTE_PN.NIT IS NULL and DPA = 3205')
        if city_name == 'Holguin':
            return Holguin.objects.raw(
                'select distinct * from RECA.CORE_HOLGUIN h LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON h.NUMEROIDENTIDAD =  info.NIT WHERE INFOGESTI.IG_CONTRIBUYENTE_PN.NIT IS NULL and DPA = 3206')
        if city_name == 'Calixto Garcia':
            return Holguin.objects.raw(
                'select distinct * from RECA.CORE_HOLGUIN h LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON h.NUMEROIDENTIDAD =  info.NIT WHERE INFOGESTI.IG_CONTRIBUYENTE_PN.NIT IS NULL and DPA = 3207')
        if city_name == 'Cacocum':
            return Holguin.objects.raw(
                'select distinct * from RECA.CORE_HOLGUIN h LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON h.NUMEROIDENTIDAD =  info.NIT WHERE INFOGESTI.IG_CONTRIBUYENTE_PN.NIT IS NULL and DPA = 3208')
        if city_name == 'Urbano Noris':
            return Holguin.objects.raw(
                'select distinct * from RECA.CORE_HOLGUIN h LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON h.NUMEROIDENTIDAD =  info.NIT WHERE INFOGESTI.IG_CONTRIBUYENTE_PN.NIT IS NULL and DPA = 3209')
        if city_name == 'Cueto':
            return Holguin.objects.raw(
                'select distinct * from RECA.CORE_HOLGUIN h LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON h.NUMEROIDENTIDAD =  info.NIT WHERE INFOGESTI.IG_CONTRIBUYENTE_PN.NIT IS NULL and DPA = 3210')
        if city_name == 'Mayari':
            return Holguin.objects.raw(
                'select distinct * from RECA.CORE_HOLGUIN h LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON h.NUMEROIDENTIDAD =  info.NIT WHERE INFOGESTI.IG_CONTRIBUYENTE_PN.NIT IS NULL and DPA = 3211')
        if city_name == 'Frank Pais':
            return Holguin.objects.raw(
                'select distinct * from RECA.CORE_HOLGUIN h LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON h.NUMEROIDENTIDAD =  info.NIT WHERE INFOGESTI.IG_CONTRIBUYENTE_PN.NIT IS NULL and DPA = 3212')
        if city_name == 'Sagua de Tanamo':
            return Holguin.objects.raw(
                'select distinct * from RECA.CORE_HOLGUIN h LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON h.NUMEROIDENTIDAD =  info.NIT WHERE INFOGESTI.IG_CONTRIBUYENTE_PN.NIT IS NULL and DPA = 3213')
        if city_name == 'Moa':
            return Holguin.objects.raw(
                'select distinct * from RECA.CORE_HOLGUIN h LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON h.NUMEROIDENTIDAD =  info.NIT WHERE INFOGESTI.IG_CONTRIBUYENTE_PN.NIT IS NULL and DPA = 3214')


    # 2 Contribuyentes que estan en ambos capitania con informaciones diferentes
    def resolve_contributors_with_different_information_holguin(self, info, city_name=graphene.String()):

        if city_name == 'Gibara':
            return Holguin.objects.raw(
                "select distinct * from RECA.CORE_HOLGUIN h INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON h.NUMEROIDENTIDAD =  info.NIT and DPA = 3201 and UNIDAD = 3201 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NUMEROIDENTIDAD")
        if city_name == 'Rafael Freyre':
            return Holguin.objects.raw(
                "select distinct * from RECA.CORE_HOLGUIN h INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON h.NUMEROIDENTIDAD =  info.NIT and DPA = 3202 and UNIDAD = 3202 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NUMEROIDENTIDAD")
        if city_name == 'Banes':
            return Holguin.objects.raw(
                "select distinct * from RECA.CORE_HOLGUIN h INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON h.NUMEROIDENTIDAD =  info.NIT and DPA = 3203 and UNIDAD = 3203 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NUMEROIDENTIDAD")
        if city_name == 'Antilla':
            return Holguin.objects.raw(
                "select distinct * from RECA.CORE_HOLGUIN h INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON h.NUMEROIDENTIDAD =  info.NIT and DPA = 3204 and UNIDAD = 3204 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NUMEROIDENTIDAD")
        if city_name == 'Baguanos':
            return Holguin.objects.raw(
                "select distinct * from RECA.CORE_HOLGUIN h INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON h.NUMEROIDENTIDAD =  info.NIT and DPA = 3205 and UNIDAD = 3205 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NUMEROIDENTIDAD")
        if city_name == 'Holguin':
            return Holguin.objects.raw(
                "select distinct * from RECA.CORE_HOLGUIN h INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON h.NUMEROIDENTIDAD =  info.NIT and DPA = 3206 and UNIDAD = 3206 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NUMEROIDENTIDAD")
        if city_name == 'Calixto Garcia':
            return Holguin.objects.raw(
                "select distinct * from RECA.CORE_HOLGUIN h INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON h.NUMEROIDENTIDAD =  info.NIT and DPA = 3207 and UNIDAD = 3207 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NUMEROIDENTIDAD")
        if city_name == 'Cacocum':
            return Holguin.objects.raw(
                "select distinct * from RECA.CORE_HOLGUIN h INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON h.NUMEROIDENTIDAD =  info.NIT and DPA = 3208 and UNIDAD = 3208 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NUMEROIDENTIDAD")
        if city_name == 'Urbano Noris':
            return Holguin.objects.raw(
                "select distinct * from RECA.CORE_HOLGUIN h INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON h.NUMEROIDENTIDAD =  info.NIT and DPA = 3209 and UNIDAD = 3209 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NUMEROIDENTIDAD")
        if city_name == 'Cueto':
            return Holguin.objects.raw(
                "select distinct * from RECA.CORE_HOLGUIN h INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON h.NUMEROIDENTIDAD =  info.NIT and DPA = 3210 and UNIDAD = 3210 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NUMEROIDENTIDAD")
        if city_name == 'Mayari':
            return Holguin.objects.raw(
                "select distinct * from RECA.CORE_HOLGUIN h INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON h.NUMEROIDENTIDAD =  info.NIT and DPA = 3211 and UNIDAD = 3211 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NUMEROIDENTIDAD")
        if city_name == 'Frank Pais':
            return Holguin.objects.raw(
                "select distinct * from RECA.CORE_HOLGUIN h INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON h.NUMEROIDENTIDAD =  info.NIT and DPA = 3212 and UNIDAD = 3212 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NUMEROIDENTIDAD")
        if city_name == 'Sagua de Tanamo':
            return Holguin.objects.raw(
                "select distinct * from RECA.CORE_HOLGUIN h INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON h.NUMEROIDENTIDAD =  info.NIT and DPA = 3213 and UNIDAD = 3213 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NUMEROIDENTIDAD")
        if city_name == 'Moa':
            return Holguin.objects.raw(
                "select distinct * from RECA.CORE_HOLGUIN h INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON h.NUMEROIDENTIDAD =  info.NIT and DPA = 3214 and UNIDAD = 3214  and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NITorder by NUMEROIDENTIDAD")

    def resolve_contributors_with_different_information_holguin_infogesti(self, info, city_name=graphene.String()):

        if city_name == 'Gibara':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@infogesti info INNER JOIN RECA.CORE_HOLGUIN h ON h.NUMEROIDENTIDAD =  info.NIT and UNIDAD = 3201 and DPA = 3202 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NIT")
        if city_name == 'Rafael Freyre':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@infogesti info INNER JOIN RECA.CORE_HOLGUIN h ON h.NUMEROIDENTIDAD =  info.NIT and UNIDAD = 3202 and DPA = 3203 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NIT")
        if city_name == 'Banes':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@infogesti info INNER JOIN RECA.CORE_HOLGUIN h ON h.NUMEROIDENTIDAD =  info.NIT and UNIDAD = 3203 and DPA = 3204 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NIT")
        if city_name == 'Antilla':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@infogesti info INNER JOIN RECA.CORE_HOLGUIN h ON h.NUMEROIDENTIDAD =  info.NIT and UNIDAD = 3204 and DPA = 3205 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NIT")
        if city_name == 'Baguanos':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@infogesti info INNER JOIN RECA.CORE_HOLGUIN h ON h.NUMEROIDENTIDAD =  info.NIT and UNIDAD = 3205 and DPA = 3206 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NIT")
        if city_name == 'Holguin':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@infogesti info INNER JOIN RECA.CORE_HOLGUIN h ON h.NUMEROIDENTIDAD =  info.NIT and UNIDAD = 3206 and DPA = 3207 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NIT")
        if city_name == 'Calixto Garcia':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@infogesti info INNER JOIN RECA.CORE_HOLGUIN h ON h.NUMEROIDENTIDAD =  info.NIT and UNIDAD = 3207 and DPA = 3208 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NIT")
        if city_name == 'Cacocum':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@infogesti info INNER JOIN RECA.CORE_HOLGUIN h ON h.NUMEROIDENTIDAD =  info.NIT and UNIDAD = 3208 and DPA = 3209 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NIT")
        if city_name == 'Urbano Noris':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@infogesti info INNER JOIN RECA.CORE_HOLGUIN h ON h.NUMEROIDENTIDAD =  info.NIT and UNIDAD = 3209 and DPA = 3210 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NIT")
        if city_name == 'Cueto':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@infogesti info INNER JOIN RECA.CORE_HOLGUIN h ON h.NUMEROIDENTIDAD =  info.NIT and UNIDAD = 3210 and DPA = 3211 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NIT")
        if city_name == 'Mayari':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@infogesti info INNER JOIN RECA.CORE_HOLGUIN h ON h.NUMEROIDENTIDAD =  info.NIT and UNIDAD = 3211 and DPA = 3212 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NIT")
        if city_name == 'Frank Pais':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@infogesti info INNER JOIN RECA.CORE_HOLGUIN h ON h.NUMEROIDENTIDAD =  info.NIT and UNIDAD = 3212 and DPA = 3213 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NIT")
        if city_name == 'Sagua de Tanamo':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@infogesti info INNER JOIN RECA.CORE_HOLGUIN h ON h.NUMEROIDENTIDAD =  info.NIT and UNIDAD = 3213 and DPA = 3214 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NIT")
        if city_name == 'Moa':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@infogesti info INNER JOIN RECA.CORE_HOLGUIN h ON h.NUMEROIDENTIDAD =  info.NIT and UNIDAD = 3214 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NIT")


    # 4 Contribuyentes totalmente coincidentes
    def resolve_contributors_with_equals_information_holguin(self, info, city_name=graphene.String()):

        if city_name == 'Gibara':
            return Holguin.objects.raw(
                'select distinct * from RECA.CORE_HOLGUIN h INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON h.NUMEROIDENTIDAD =  info.NIT and DPA = 3201 WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT order by NUMEROIDENTIDAD')
        if city_name == 'Rafael Freyre':
            return Holguin.objects.raw(
                'select distinct * from RECA.CORE_HOLGUIN h INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON h.NUMEROIDENTIDAD =  info.NIT and DPA = 3202 WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT order by NUMEROIDENTIDAD')
        if city_name == 'Banes':
            return Holguin.objects.raw(
                'select distinct * from RECA.CORE_HOLGUIN h INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON h.NUMEROIDENTIDAD =  info.NIT and DPA = 3203 WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT order by NUMEROIDENTIDAD')
        if city_name == 'Antilla':
            return Holguin.objects.raw(
                'select distinct * from RECA.CORE_HOLGUIN h INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON h.NUMEROIDENTIDAD =  info.NIT and DPA = 3204 WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT order by NUMEROIDENTIDAD')
        if city_name == 'Baguanos':
            return Holguin.objects.raw(
                'select distinct * from RECA.CORE_HOLGUIN h INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON h.NUMEROIDENTIDAD =  info.NIT and DPA = 3205 WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT order by NUMEROIDENTIDAD')
        if city_name == 'Holguin':
            return Holguin.objects.raw(
                'select distinct * from RECA.CORE_HOLGUIN h INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON h.NUMEROIDENTIDAD =  info.NIT and DPA = 3206 WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT order by NUMEROIDENTIDAD')
        if city_name == 'Calixto Garcia':
            return Holguin.objects.raw(
                'select distinct * from RECA.CORE_HOLGUIN h INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON h.NUMEROIDENTIDAD =  info.NIT and DPA = 3207 WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT order by NUMEROIDENTIDAD')
        if city_name == 'Cacocum':
            return Holguin.objects.raw(
                'select distinct * from RECA.CORE_HOLGUIN h INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON h.NUMEROIDENTIDAD =  info.NIT and DPA = 3208 WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT order by NUMEROIDENTIDAD')
        if city_name == 'Urbano Noris':
            return Holguin.objects.raw(
                'select distinct * from RECA.CORE_HOLGUIN h INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON h.NUMEROIDENTIDAD =  info.NIT and DPA = 3209 WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT order by NUMEROIDENTIDAD')
        if city_name == 'Cueto':
            return Holguin.objects.raw(
                'select distinct * from RECA.CORE_HOLGUIN h INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON h.NUMEROIDENTIDAD =  info.NIT and DPA = 3210 WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT order by NUMEROIDENTIDAD')
        if city_name == 'Mayari':
            return Holguin.objects.raw(
                'select distinct * from RECA.CORE_HOLGUIN h INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON h.NUMEROIDENTIDAD =  info.NIT and DPA = 3211 WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT order by NUMEROIDENTIDAD')
        if city_name == 'Frank Pais':
            return Holguin.objects.raw(
                'select distinct * from RECA.CORE_HOLGUIN h INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON h.NUMEROIDENTIDAD =  info.NIT and DPA = 3212 WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT order by NUMEROIDENTIDAD')
        if city_name == 'Sagua de Tanamo':
            return Holguin.objects.raw(
                'select distinct * from RECA.CORE_HOLGUIN h INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON h.NUMEROIDENTIDAD =  info.NIT and DPA = 3213 WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT order by NUMEROIDENTIDAD')
        if city_name == 'Moa':
            return Holguin.objects.raw(
                'select distinct * from RECA.CORE_HOLGUIN h INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON h.NUMEROIDENTIDAD =  info.NIT and DPA = 3214 WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT order by NUMEROIDENTIDAD')

    def resolve_holguin(self, info):
        return Holguin.objects.all()


schema = graphene.Schema(query=ContributorsFromHolguinQuery, auto_camelcase=False)
