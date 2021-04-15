import graphene
from capitania.apps.api.types.provincias import PinarDelRioType, InfogestiContributorsType
from capitania.apps.core.models import PinarDelRio, InfogestiContributors


class ContributorsFromPinarQuery(graphene.ObjectType):
    contributors_missing_in_onat_pinar = graphene.List(PinarDelRioType, city_name=graphene.String())
    contributors_with_different_information_pinar = graphene.List(PinarDelRioType, city_name=graphene.String())
    contributors_with_different_information_pinar_infogesti = graphene.List(InfogestiContributorsType, city_name=graphene.String())
    contributors_with_equals_information_pinar = graphene.List(PinarDelRioType, city_name=graphene.String())
    pinar_del_rio = graphene.List(PinarDelRioType)

    # 1 Contribuyentes que estan en capitania vehiculo que no estan en la onat
    def resolve_contributors_missing_in_onat_pinar(self, info, city_name=graphene.String()):

        if city_name == 'Sandino':
            return PinarDelRio.objects.raw(
                'select distinct * from RECA.CORE_PINARDELRIO p LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON p.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2101')
        if city_name == 'Mantua':
            return PinarDelRio.objects.raw(
                'select distinct * from RECA.CORE_PINARDELRIO p LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON p.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2102')
        if city_name == 'Minas De Matahambre':
            return PinarDelRio.objects.raw(
                'select distinct * from RECA.CORE_PINARDELRIO p LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON p.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2103')
        if city_name == 'Viñales':
            return PinarDelRio.objects.raw(
                'select distinct * from RECA.CORE_PINARDELRIO p LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON p.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2104')
        if city_name == 'La Palma':
            return PinarDelRio.objects.raw(
                'select distinct * from RECA.CORE_PINARDELRIO p LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON p.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2105')
        if city_name == 'Los Palacios':
            return PinarDelRio.objects.raw(
                'select distinct * from RECA.CORE_PINARDELRIO p LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON p.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2106')
        if city_name == 'Consolacion del Sur':
            return PinarDelRio.objects.raw(
                'select distinct * from RECA.CORE_PINARDELRIO p LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON p.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2107')
        if city_name == 'Pinar del Rio':
            return PinarDelRio.objects.raw(
                'select distinct * from RECA.CORE_PINARDELRIO p LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON p.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2108')
        if city_name == 'San Luis':
            return PinarDelRio.objects.raw(
                'select distinct * from RECA.CORE_PINARDELRIO p LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON p.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2109')
        if city_name == 'San Juan y Martinez':
            return PinarDelRio.objects.raw(
                'select distinct * from RECA.CORE_PINARDELRIO p LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON p.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2110')
        if city_name == 'Guane':
            return PinarDelRio.objects.raw(
                'select distinct * from RECA.CORE_PINARDELRIO p LEFT OUTER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON p.NUMEROIDENTIDAD =  info.NIT WHERE info.NIT IS NULL and DPA = 2111')


    # 2 Contribuyentes que estan en ambos capitania con informaciones diferentes
    def resolve_contributors_with_different_information_pinar(self, info, city_name=graphene.String()):

        if city_name == 'Sandino':
            return PinarDelRio.objects.raw(
                "select distinct * from RECA.CORE_PINARDELRIO p INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON p.NUMEROIDENTIDAD =  info.NIT  and info.ES_PROPIETARIO_TT = '1' and UNIDAD = 2101 and DPA = 2101 WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NUMEROIDENTIDAD")
        if city_name == 'Mantua':
            return PinarDelRio.objects.raw(
                "select distinct * from RECA.CORE_PINARDELRIO p INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON p.NUMEROIDENTIDAD =  info.NIT  and info.ES_PROPIETARIO_TT = '1' and UNIDAD = 2102 and DPA = 2102 WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NUMEROIDENTIDAD")
        if city_name == 'Minas De Matahambre':
            return PinarDelRio.objects.raw(
                "select distinct * from RECA.CORE_PINARDELRIO p INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON p.NUMEROIDENTIDAD =  info.NIT  and info.ES_PROPIETARIO_TT = '1' and UNIDAD = 2103 and DPA = 2103 WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NUMEROIDENTIDAD")
        if city_name == 'Viñales':
            return PinarDelRio.objects.raw(
                "select distinct * from RECA.CORE_PINARDELRIO p INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON p.NUMEROIDENTIDAD =  info.NIT  and info.ES_PROPIETARIO_TT = '1' and UNIDAD = 2104 and DPA = 2104 WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NUMEROIDENTIDAD")
        if city_name == 'La Palma':
            return PinarDelRio.objects.raw(
                "select distinct * from RECA.CORE_PINARDELRIO p INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON p.NUMEROIDENTIDAD =  info.NIT  and info.ES_PROPIETARIO_TT = '1' and UNIDAD = 2105 and DPA = 2105 WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NUMEROIDENTIDAD")
        if city_name == 'Los Palacios':
            return PinarDelRio.objects.raw(
                "select distinct * from RECA.CORE_PINARDELRIO p INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON p.NUMEROIDENTIDAD =  info.NIT  and info.ES_PROPIETARIO_TT = '1' and UNIDAD = 2106 and DPA = 2106 WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NUMEROIDENTIDAD")
        if city_name == 'Consolacion del Sur':
            return PinarDelRio.objects.raw(
                "select distinct * from RECA.CORE_PINARDELRIO p INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON p.NUMEROIDENTIDAD =  info.NIT  and info.ES_PROPIETARIO_TT = '1' and UNIDAD = 2107 and DPA = 2107 WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NUMEROIDENTIDAD")
        if city_name == 'Pinar del Rio':
            return PinarDelRio.objects.raw(
                "select distinct * from RECA.CORE_PINARDELRIO p INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON p.NUMEROIDENTIDAD =  info.NIT  and info.ES_PROPIETARIO_TT = '1' and UNIDAD = 2108 and DPA = 2108 WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NUMEROIDENTIDAD")
        if city_name == 'San Luis':
            return PinarDelRio.objects.raw(
                "select distinct * from RECA.CORE_PINARDELRIO p INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON p.NUMEROIDENTIDAD =  info.NIT  and info.ES_PROPIETARIO_TT = '1' and UNIDAD = 2109 and DPA = 2109 WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NUMEROIDENTIDAD")
        if city_name == 'San Juan y Martinez':
            return PinarDelRio.objects.raw(
                "select distinct * from RECA.CORE_PINARDELRIO p INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON p.NUMEROIDENTIDAD =  info.NIT  and info.ES_PROPIETARIO_TT = '1' and UNIDAD = 2110 and DPA = 2110 WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NUMEROIDENTIDAD")
        if city_name == 'Guane':
            return PinarDelRio.objects.raw(
                "select distinct * from RECA.CORE_PINARDELRIO p INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON p.NUMEROIDENTIDAD =  info.NIT  and info.ES_PROPIETARIO_TT = '1' and UNIDAD = 2111 and DPA = 2111 WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NUMEROIDENTIDAD")


    def resolve_contributors_with_different_information_pinar_infogesti(self, info, city_name=graphene.String()):

        if city_name == 'Sandino':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@infogesti info INNER JOIN RECA.CORE_PINARDELRIO p ON p.NUMEROIDENTIDAD =  info.NIT   and info.ES_PROPIETARIO_TT = '1' and UNIDAD = 2101 and DPA = 2101  WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NIT")
        if city_name == 'Mantua':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@infogesti info INNER JOIN RECA.CORE_PINARDELRIO p ON p.NUMEROIDENTIDAD =  info.NIT   and info.ES_PROPIETARIO_TT = '1' and UNIDAD = 2102 and DPA = 2102  WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NIT")
        if city_name == 'Minas De Matahambre':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@infogesti info INNER JOIN RECA.CORE_PINARDELRIO p ON p.NUMEROIDENTIDAD =  info.NIT   and info.ES_PROPIETARIO_TT = '1' and UNIDAD = 2103 and DPA = 2103  WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NIT")
        if city_name == 'Viñales':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@infogesti info INNER JOIN RECA.CORE_PINARDELRIO p ON p.NUMEROIDENTIDAD =  info.NIT   and info.ES_PROPIETARIO_TT = '1' and UNIDAD = 2104 and DPA = 2104  WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NIT")
        if city_name == 'La Palma':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@infogesti info INNER JOIN RECA.CORE_PINARDELRIO p ON p.NUMEROIDENTIDAD =  info.NIT   and info.ES_PROPIETARIO_TT = '1' and UNIDAD = 2105 and DPA = 2105  WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NIT")
        if city_name == 'Los Palacios':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@infogesti info INNER JOIN RECA.CORE_PINARDELRIO p ON p.NUMEROIDENTIDAD =  info.NIT   and info.ES_PROPIETARIO_TT = '1' and UNIDAD = 2106 and DPA = 2106  WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NIT")
        if city_name == 'Consolacion del Sur':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@infogesti info INNER JOIN RECA.CORE_PINARDELRIO p ON p.NUMEROIDENTIDAD =  info.NIT   and info.ES_PROPIETARIO_TT = '1' and UNIDAD = 2107 and DPA = 2107  WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NIT")
        if city_name == 'Pinar del Rio':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@infogesti info INNER JOIN RECA.CORE_PINARDELRIO p ON p.NUMEROIDENTIDAD =  info.NIT   and info.ES_PROPIETARIO_TT = '1' and UNIDAD = 2108 and DPA = 2108  WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NIT")
        if city_name == 'San Luis':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@infogesti info INNER JOIN RECA.CORE_PINARDELRIO p ON p.NUMEROIDENTIDAD =  info.NIT   and info.ES_PROPIETARIO_TT = '1' and UNIDAD = 2109 and DPA = 2109  WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NIT")
        if city_name == 'San Juan y Martinez':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@infogesti info INNER JOIN RECA.CORE_PINARDELRIO p ON p.NUMEROIDENTIDAD =  info.NIT   and info.ES_PROPIETARIO_TT = '1' and UNIDAD = 2110 and DPA = 2110  WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NIT")
        if city_name == 'Guane':
            return InfogestiContributors.objects.raw(
                "select distinct * from IG_CONTRIBUYENTE_PN@infogesti info INNER JOIN RECA.CORE_PINARDELRIO p ON p.NUMEROIDENTIDAD =  info.NIT   and info.ES_PROPIETARIO_TT = '1' and UNIDAD = 2111 and DPA = 2111  WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NIT")

    # 4 Contribuyentes totalmente coincidentes
    def resolve_contributors_with_equals_information_pinar(self, info, city_name=graphene.String()):

        if city_name == 'Sandino':
            return PinarDelRio.objects.raw(
                'select distinct * from RECA.CORE_PINARDELRIO p INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON p.NUMEROIDENTIDAD =  info.NIT WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT  and DPA = 2101 order by NUMEROIDENTIDAD')
        if city_name == 'Mantua':
            return PinarDelRio.objects.raw(
                'select distinct * from RECA.CORE_PINARDELRIO p INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON p.NUMEROIDENTIDAD =  info.NIT WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT  and DPA = 2102 order by NUMEROIDENTIDAD')
        if city_name == 'Minas De Matahambre':
            return PinarDelRio.objects.raw(
                'select distinct * from RECA.CORE_PINARDELRIO p INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON p.NUMEROIDENTIDAD =  info.NIT WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT  and DPA = 2103 order by NUMEROIDENTIDAD')
        if city_name == 'Viñales':
            return PinarDelRio.objects.raw(
                'select distinct * from RECA.CORE_PINARDELRIO p INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON p.NUMEROIDENTIDAD =  info.NIT WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT  and DPA = 2104 order by NUMEROIDENTIDAD')
        if city_name == 'La Palma':
            return PinarDelRio.objects.raw(
                'select distinct * from RECA.CORE_PINARDELRIO p INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON p.NUMEROIDENTIDAD =  info.NIT WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT  and DPA = 2105 order by NUMEROIDENTIDAD')
        if city_name == 'Los Palacios':
            return PinarDelRio.objects.raw(
                'select distinct * from RECA.CORE_PINARDELRIO p INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON p.NUMEROIDENTIDAD =  info.NIT WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT  and DPA = 2106 order by NUMEROIDENTIDAD')
        if city_name == 'Consolacion del Sur':
            return PinarDelRio.objects.raw(
                'select distinct * from RECA.CORE_PINARDELRIO p INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON p.NUMEROIDENTIDAD =  info.NIT WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT  and DPA = 2107 order by NUMEROIDENTIDAD')
        if city_name == 'Pinar del Rio':
            return PinarDelRio.objects.raw(
                'select distinct * from RECA.CORE_PINARDELRIO p INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON p.NUMEROIDENTIDAD =  info.NIT WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT  and DPA = 2108 order by NUMEROIDENTIDAD')
        if city_name == 'San Luis':
            return PinarDelRio.objects.raw(
                'select distinct * from RECA.CORE_PINARDELRIO p INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON p.NUMEROIDENTIDAD =  info.NIT WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT  and DPA = 2109 order by NUMEROIDENTIDAD')
        if city_name == 'San Juan y Martinez':
            return PinarDelRio.objects.raw(
                'select distinct * from RECA.CORE_PINARDELRIO p INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON p.NUMEROIDENTIDAD =  info.NIT WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT  and DPA = 2110 order by NUMEROIDENTIDAD')
        if city_name == 'Guane':
            return PinarDelRio.objects.raw(
                'select distinct * from RECA.CORE_PINARDELRIO p INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON p.NUMEROIDENTIDAD =  info.NIT WHERE NOMBRE_COMPLETO = DATOSPERSONA  and NUMEROIDENTIDAD = NIT  and DPA = 2111 order by NUMEROIDENTIDAD')


    def resolve_pinar_del_rio(self, info):
        return PinarDelRio.objects.all()


schema = graphene.Schema(query=ContributorsFromPinarQuery, auto_camelcase=False)
