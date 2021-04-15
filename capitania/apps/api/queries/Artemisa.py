import graphene

from capitania.apps.api.types.provincias import ArtemisaType, InfogestiContributorsType
from capitania.apps.core.models import Artemisa, InfogestiContributors


class ContributorsFromArtemisaQuery(graphene.ObjectType):
    contributors_missing_in_onat_artemisa = graphene.List(ArtemisaType, city_name=graphene.String())
    contributors_with_different_information_artemisa = graphene.List(ArtemisaType, city_name=graphene.String())
    contributors_with_different_information_artemisa_infogesti = graphene.List(InfogestiContributorsType,
                                                                               city_name=graphene.String())
    contributors_with_equals_information_artemisa = graphene.List(ArtemisaType, city_name=graphene.String())
    artemisa = graphene.List(ArtemisaType)

    # 1 Contribuyentes que estan en capitania vehiculo que no estan en la onat
    def resolve_contributors_missing_in_onat_artemisa(self, info, city_name=graphene.String()):
        # artemisa
        if city_name == 'Bahia Honda':
            return Artemisa.objects.raw(
                'select distinct distinct * from RECA.CORE_ARTEMISA art LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON art.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2201')
        if city_name == 'Alquizar':
            return Artemisa.objects.raw(
                'select distinct * from RECA.CORE_ARTEMISA art LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON art.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2202')
        if city_name == 'Artemisa':
            return Artemisa.objects.raw(
                'select distinct * from RECA.CORE_ARTEMISA art LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON art.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2203')
        if city_name == 'Bauta':
            return Artemisa.objects.raw(
                'select distinct * from RECA.CORE_ARTEMISA art LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON art.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2204')
        if city_name == 'Caimito':
            return Artemisa.objects.raw(
                'select distinct * from RECA.CORE_ARTEMISA art LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON art.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2205')
        if city_name == 'Candelaria':
            return Artemisa.objects.raw(
                'select distinct * from RECA.CORE_ARTEMISA art LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON art.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2206')
        if city_name == 'Guanajay':
            return Artemisa.objects.raw(
                'select distinct * from RECA.CORE_ARTEMISA art LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON art.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2207')
        if city_name == 'Gueira de Melena':
            return Artemisa.objects.raw(
                'select distinct * from RECA.CORE_ARTEMISA art LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON art.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2208')
        if city_name == 'Mariel':
            return Artemisa.objects.raw(
                'select distinct * from RECA.CORE_ARTEMISA art LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON art.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2209')
        if city_name == 'San Antonio de los Banos':
            return Artemisa.objects.raw(
                'select distinct * from RECA.CORE_ARTEMISA art LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON art.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2210')
        if city_name == 'San Cristobal':
            return Artemisa.objects.raw(
                'select distinct * from RECA.CORE_ARTEMISA art LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON art.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2211')

    # 2 Contribuyentes que estan en ambos capitania con informaciones diferentes
    def resolve_contributors_with_different_information_artemisa(self, info, city_name=graphene.String()):

        if city_name == 'Bahia Honda':
            return Artemisa.objects.raw(
                "select distinct * from RECA.CORE_ARTEMISA art LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON art.NUMEROIDENTIDAD =  info.NIT and DPA = 2201 and info.UNIDAD = 2201 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA  order by NUMEROIDENTIDAD")
        if city_name == 'Alquizar':
            return Artemisa.objects.raw(
                "select distinct * from RECA.CORE_ARTEMISA art LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON art.NUMEROIDENTIDAD =  info.NIT and DPA = 2202 and info.UNIDAD = 2202 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA  order by NUMEROIDENTIDAD")
        if city_name == 'Artemisa':
            return Artemisa.objects.raw(
                "select distinct * from RECA.CORE_ARTEMISA art LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON art.NUMEROIDENTIDAD =  info.NIT and DPA = 2203 and info.UNIDAD = 2203 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA  order by NUMEROIDENTIDAD")
        if city_name == 'Bauta':
            return Artemisa.objects.raw(
                "select distinct * from RECA.CORE_ARTEMISA art LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON art.NUMEROIDENTIDAD =  info.NIT and DPA = 2204 and info.UNIDAD = 2204 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA  order by NUMEROIDENTIDAD")
        if city_name == 'Caimito':
            return Artemisa.objects.raw(
                "select distinct * from RECA.CORE_ARTEMISA art LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON art.NUMEROIDENTIDAD =  info.NIT and DPA = 2205 and info.UNIDAD = 2205 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA  order by NUMEROIDENTIDAD")
        if city_name == 'Candelaria':
            return Artemisa.objects.raw(
                "select distinct * from RECA.CORE_ARTEMISA art LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON art.NUMEROIDENTIDAD =  info.NIT and DPA = 2206 and info.UNIDAD = 2206 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA  order by NUMEROIDENTIDAD")
        if city_name == 'Guanajay':
            return Artemisa.objects.raw(
                "select distinct * from RECA.CORE_ARTEMISA art LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON art.NUMEROIDENTIDAD =  info.NIT and DPA = 2207 and info.UNIDAD = 2207 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA  order by NUMEROIDENTIDAD")
        if city_name == 'Gueira de Melena':
            return Artemisa.objects.raw(
                "select distinct * from RECA.CORE_ARTEMISA art LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON art.NUMEROIDENTIDAD =  info.NIT and DPA = 2208 and info.UNIDAD = 2208 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA  order by NUMEROIDENTIDAD")
        if city_name == 'Mariel':
            return Artemisa.objects.raw(
                "select distinct * from RECA.CORE_ARTEMISA art LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON art.NUMEROIDENTIDAD =  info.NIT and DPA = 2209 and info.UNIDAD = 2209 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA  order by NUMEROIDENTIDAD")
        if city_name == 'San Antonio de los Banos':
            return Artemisa.objects.raw(
                "select distinct * from RECA.CORE_ARTEMISA art LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON art.NUMEROIDENTIDAD =  info.NIT and DPA = 2210 and info.UNIDAD = 2210 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA  order by NUMEROIDENTIDAD")
        if city_name == 'San Cristobal':
            return Artemisa.objects.raw(
                "select distinct * from RECA.CORE_ARTEMISA art LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON art.NUMEROIDENTIDAD =  info.NIT and DPA = 2211 and info.UNIDAD = 2211 and info.ES_PROPIETARIO_TT = '1' WHERE NOMBRE_COMPLETO <> DATOSPERSONA  order by NUMEROIDENTIDAD")


    def resolve_contributors_with_different_information_artemisa_infogesti(self, info, city_name=graphene.String()):
        if city_name == 'Bahia Honda':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN RECA.CORE_ARTEMISA art ON art.NUMEROIDENTIDAD =  info.NIT and info.UNIDAD = 2201 and DPA = 2201 and info.ES_PROPIETARIO_TT = '1'  WHERE NOMBRE_COMPLETO <> DATOSPERSONA order by NIT")
        if city_name == 'Alquizar':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN RECA.CORE_ARTEMISA art ON art.NUMEROIDENTIDAD =  info.NIT and info.UNIDAD = 2202  and DPA = 2202 and info.ES_PROPIETARIO_TT = '1'  WHERE NOMBRE_COMPLETO <> DATOSPERSONA  order by NIT")
        if city_name == 'Artemisa':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN RECA.CORE_ARTEMISA art ON art.NUMEROIDENTIDAD =  info.NIT and info.UNIDAD = 2203  and DPA = 2203 and info.ES_PROPIETARIO_TT = '1'  WHERE NOMBRE_COMPLETO <> DATOSPERSONA  order by NIT")
        if city_name == 'Bauta':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN RECA.CORE_ARTEMISA art ON art.NUMEROIDENTIDAD =  info.NIT and info.UNIDAD = 2204  and DPA = 2204 and info.ES_PROPIETARIO_TT = '1'  WHERE NOMBRE_COMPLETO <> DATOSPERSONA  order by NIT")
        if city_name == 'Caimito':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN RECA.CORE_ARTEMISA art ON art.NUMEROIDENTIDAD =  info.NIT and info.UNIDAD = 2205  and DPA = 2205 and info.ES_PROPIETARIO_TT = '1'  WHERE NOMBRE_COMPLETO <> DATOSPERSONA  order by NIT")
        if city_name == 'Candelaria':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN RECA.CORE_ARTEMISA art ON art.NUMEROIDENTIDAD =  info.NIT and info.UNIDAD = 2206  and DPA = 2206 and info.ES_PROPIETARIO_TT = '1'  WHERE NOMBRE_COMPLETO <> DATOSPERSONA  order by NIT")
        if city_name == 'Guanajay':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN RECA.CORE_ARTEMISA art ON art.NUMEROIDENTIDAD =  info.NIT and info.UNIDAD = 2207  and DPA = 2207 and info.ES_PROPIETARIO_TT = '1'  WHERE NOMBRE_COMPLETO <> DATOSPERSONA  order by NIT")
        if city_name == 'Gueira de Melena':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN RECA.CORE_ARTEMISA art ON art.NUMEROIDENTIDAD =  info.NIT and info.UNIDAD = 2208  and DPA = 2208 and info.ES_PROPIETARIO_TT = '1'  WHERE NOMBRE_COMPLETO <> DATOSPERSONA  order by NIT")
        if city_name == 'Mariel':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN RECA.CORE_ARTEMISA art ON art.NUMEROIDENTIDAD =  info.NIT and info.UNIDAD = 2209  and DPA = 2209 and info.ES_PROPIETARIO_TT = '1'  WHERE NOMBRE_COMPLETO <> DATOSPERSONA  order by NIT")
        if city_name == 'San Antonio de los Banos':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN RECA.CORE_ARTEMISA art ON art.NUMEROIDENTIDAD =  info.NIT and info.UNIDAD = 2210  and DPA = 2210 and info.ES_PROPIETARIO_TT = '1'  WHERE NOMBRE_COMPLETO <> DATOSPERSONA  order by NIT")
        if city_name == 'San Cristobal':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN RECA.CORE_ARTEMISA art ON art.NUMEROIDENTIDAD =  info.NIT and info.UNIDAD = 2211  and DPA = 2211 and info.ES_PROPIETARIO_TT = '1'  WHERE NOMBRE_COMPLETO <> DATOSPERSONA  order by NIT")

    # 4 Contribuyentes totalmente coincidentes
    def resolve_contributors_with_equals_information_artemisa(self, info, city_name=graphene.String()):
        if city_name == 'Bahia Honda':
            return Artemisa.objects.raw(
                'select distinct * from RECA.CORE_ARTEMISA art INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON art.NUMEROIDENTIDAD =  info.NIT and DPA = 2201 WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT order  by NIT')
        if city_name == 'Alquizar':
            return Artemisa.objects.raw(
                'select distinct * from RECA.CORE_ARTEMISA art INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON art.NUMEROIDENTIDAD =  info.NIT and DPA = 2202 WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT order  by NIT')
        if city_name == 'Artemisa':
            return Artemisa.objects.raw(
                'select distinct * from RECA.CORE_ARTEMISA art INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON art.NUMEROIDENTIDAD =  info.NIT and DPA = 2203 WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT order  by NIT')
        if city_name == 'Bauta':
            return Artemisa.objects.raw(
                'select distinct * from RECA.CORE_ARTEMISA art INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON art.NUMEROIDENTIDAD =  info.NIT and DPA = 2204 WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT order  by NIT')
        if city_name == 'Caimito':
            return Artemisa.objects.raw(
                'select distinct * from RECA.CORE_ARTEMISA art INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON art.NUMEROIDENTIDAD =  info.NIT and DPA = 2205 WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT order  by NIT')
        if city_name == 'Candelaria':
            return Artemisa.objects.raw(
                'select distinct * from RECA.CORE_ARTEMISA art INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON art.NUMEROIDENTIDAD =  info.NIT and DPA = 2206 WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT order  by NIT')
        if city_name == 'Guanajay':
            return Artemisa.objects.raw(
                'select distinct * from RECA.CORE_ARTEMISA art INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON art.NUMEROIDENTIDAD =  info.NIT and DPA = 2207 WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT order  by NIT')
        if city_name == 'Gueira de Melena':
            return Artemisa.objects.raw(
                'select distinct * from RECA.CORE_ARTEMISA art INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON art.NUMEROIDENTIDAD =  info.NIT and DPA = 2208 WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT order  by NIT')
        if city_name == 'Mariel':
            return Artemisa.objects.raw(
                'select distinct * from RECA.CORE_ARTEMISA art INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON art.NUMEROIDENTIDAD =  info.NIT and DPA = 2209 WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT order  by NIT')
        if city_name == 'San Antonio de los Banos':
            return Artemisa.objects.raw(
                'select distinct * from RECA.CORE_ARTEMISA art INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON art.NUMEROIDENTIDAD =  info.NIT and DPA = 2210 WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT order  by NIT')
        if city_name == 'San Cristobal':
            return Artemisa.objects.raw(
                'select distinct * from RECA.CORE_ARTEMISA art INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON art.NUMEROIDENTIDAD =  info.NIT and DPA = 2211 WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT order  by NIT')


    def resolve_artemisa(self, info):
        return Artemisa.objects.all()


schema = graphene.Schema(query=ContributorsFromArtemisaQuery, auto_camelcase=False)
