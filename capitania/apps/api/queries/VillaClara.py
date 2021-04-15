import graphene
from capitania.apps.api.types.provincias import VillaClaraType, InfogestiContributorsType
from capitania.apps.core.models import VillaClara, InfogestiContributors


class ContributorsFromVillaClaraQuery(graphene.ObjectType):
    contributors_missing_in_onat_villa_clara = graphene.List(VillaClaraType, city_name=graphene.String())
    contributors_with_different_information_villa_clara = graphene.List(VillaClaraType, city_name=graphene.String())
    contributors_with_different_information_villa_clara_infogesti = graphene.List(InfogestiContributorsType, city_name=graphene.String())
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
    def resolve_contributors_with_different_information_villa_clara(self, info, city_name=graphene.String()):

        if city_name == 'Corralillo':
            return VillaClara.objects.raw(
                "select * from RECA.CORE_VILLACLARA v INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON v.NUMEROIDENTIDAD =  info.NIT  and info.ES_PROPIETARIO_TT = '1' and DPA = 2601 WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NUMEROIDENTIDAD")
        if city_name == 'Quemado de Güines':
            return VillaClara.objects.raw(
                "select * from RECA.CORE_VILLACLARA v INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON v.NUMEROIDENTIDAD =  info.NIT  and info.ES_PROPIETARIO_TT = '1' and DPA = 2602 WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NUMEROIDENTIDAD")
        if city_name == 'Sagua la Grande':
            return VillaClara.objects.raw(
                "select * from RECA.CORE_VILLACLARA v INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON v.NUMEROIDENTIDAD =  info.NIT  and info.ES_PROPIETARIO_TT = '1' and DPA = 2603 WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NUMEROIDENTIDAD")
        if city_name == 'Encrucijada':
            return VillaClara.objects.raw(
                "select * from RECA.CORE_VILLACLARA v INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON v.NUMEROIDENTIDAD =  info.NIT  and info.ES_PROPIETARIO_TT = '1' and DPA = 2604 WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NUMEROIDENTIDAD")
        if city_name == 'Camajuaní':
            return VillaClara.objects.raw(
                "select * from RECA.CORE_VILLACLARA v INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON v.NUMEROIDENTIDAD =  info.NIT  and info.ES_PROPIETARIO_TT = '1' and DPA = 2605 WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NUMEROIDENTIDAD")
        if city_name == 'Caibarién':
            return VillaClara.objects.raw(
                "select * from RECA.CORE_VILLACLARA v INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON v.NUMEROIDENTIDAD =  info.NIT  and info.ES_PROPIETARIO_TT = '1' and DPA = 2606 WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NUMEROIDENTIDAD")
        if city_name == 'San Juan de los Remedios':
            return VillaClara.objects.raw(
                "select * from RECA.CORE_VILLACLARA v INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON v.NUMEROIDENTIDAD =  info.NIT  and info.ES_PROPIETARIO_TT = '1' and DPA = 2607 WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NUMEROIDENTIDAD")
        if city_name == 'Placetas':
            return VillaClara.objects.raw(
                "select * from RECA.CORE_VILLACLARA v INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON v.NUMEROIDENTIDAD =  info.NIT  and info.ES_PROPIETARIO_TT = '1' and DPA = 2608 WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NUMEROIDENTIDAD")
        if city_name == 'Santa Clara':
            return VillaClara.objects.raw(
                "select * from RECA.CORE_VILLACLARA v INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON v.NUMEROIDENTIDAD =  info.NIT  and info.ES_PROPIETARIO_TT = '1' and DPA = 2609 WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NUMEROIDENTIDAD")
        if city_name == 'Cifuentes':
            return VillaClara.objects.raw(
                "select * from RECA.CORE_VILLACLARA v INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON v.NUMEROIDENTIDAD =  info.NIT  and info.ES_PROPIETARIO_TT = '1' and DPA = 2610 WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NUMEROIDENTIDAD")
        if city_name == 'Santo Domingo':
            return VillaClara.objects.raw(
                "select * from RECA.CORE_VILLACLARA v INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON v.NUMEROIDENTIDAD =  info.NIT  and info.ES_PROPIETARIO_TT = '1' and DPA = 2611 WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NUMEROIDENTIDAD")
        if city_name == 'Ranchuelo':
            return VillaClara.objects.raw(
                "select * from RECA.CORE_VILLACLARA v INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON v.NUMEROIDENTIDAD =  info.NIT  and info.ES_PROPIETARIO_TT = '1' and DPA = 2612 WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NUMEROIDENTIDAD")
        if city_name == 'Manicaragua':
            return VillaClara.objects.raw(
                "select * from RECA.CORE_VILLACLARA v INNER JOIN IG_CONTRIBUYENTE_PN@infogesti info ON v.NUMEROIDENTIDAD =  info.NIT  and info.ES_PROPIETARIO_TT = '1' and DPA = 2613 WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NUMEROIDENTIDAD")

    def resolve_contributors_with_different_information_villa_clara_infogesti(self, info, city_name=graphene.String()):

        if city_name == 'Corralillo':
            return InfogestiContributors.objects.raw(
                "select * from IG_CONTRIBUYENTE_PN@infogesti info INNER JOIN CORE_VILLACLARA v ON v.NUMEROIDENTIDAD =  info.NIT  and info.ES_PROPIETARIO_TT = '1' and UNIDAD = 2601 WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NIT")
        if city_name == 'Quemado de Güines':
            return InfogestiContributors.objects.raw(
                "select * from IG_CONTRIBUYENTE_PN@infogesti info INNER JOIN CORE_VILLACLARA v ON v.NUMEROIDENTIDAD =  info.NIT  and info.ES_PROPIETARIO_TT = '1' and UNIDAD = 2602 WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NIT")
        if city_name == 'Sagua la Grande':
            return InfogestiContributors.objects.raw(
                "select * from IG_CONTRIBUYENTE_PN@infogesti info INNER JOIN CORE_VILLACLARA v ON v.NUMEROIDENTIDAD =  info.NIT  and info.ES_PROPIETARIO_TT = '1' and UNIDAD = 2603 WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NIT")
        if city_name == 'Encrucijada':
            return InfogestiContributors.objects.raw(
                "select * from IG_CONTRIBUYENTE_PN@infogesti info INNER JOIN CORE_VILLACLARA v ON v.NUMEROIDENTIDAD =  info.NIT  and info.ES_PROPIETARIO_TT = '1' and UNIDAD = 2604 WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NIT")
        if city_name == 'Camajuaní':
            return InfogestiContributors.objects.raw(
                "select * from IG_CONTRIBUYENTE_PN@infogesti info INNER JOIN CORE_VILLACLARA v ON v.NUMEROIDENTIDAD =  info.NIT  and info.ES_PROPIETARIO_TT = '1' and UNIDAD = 2605 WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NIT")
        if city_name == 'Caibarién':
            return InfogestiContributors.objects.raw(
                "select * from IG_CONTRIBUYENTE_PN@infogesti info INNER JOIN CORE_VILLACLARA v ON v.NUMEROIDENTIDAD =  info.NIT  and info.ES_PROPIETARIO_TT = '1' and UNIDAD = 2606 WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NIT")
        if city_name == 'San Juan de los Remedios':
            return InfogestiContributors.objects.raw(
                "select * from IG_CONTRIBUYENTE_PN@infogesti info INNER JOIN CORE_VILLACLARA v ON v.NUMEROIDENTIDAD =  info.NIT  and info.ES_PROPIETARIO_TT = '1' and UNIDAD = 2607 WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NIT")
        if city_name == 'Placetas':
            return InfogestiContributors.objects.raw(
                "select * from IG_CONTRIBUYENTE_PN@infogesti info INNER JOIN CORE_VILLACLARA v ON v.NUMEROIDENTIDAD =  info.NIT  and info.ES_PROPIETARIO_TT = '1' and UNIDAD = 2608 WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NIT")
        if city_name == 'Santa Clara':
            return InfogestiContributors.objects.raw(
                "select * from IG_CONTRIBUYENTE_PN@infogesti info INNER JOIN CORE_VILLACLARA v ON v.NUMEROIDENTIDAD =  info.NIT  and info.ES_PROPIETARIO_TT = '1' and UNIDAD = 2609 WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NIT")
        if city_name == 'Cifuentes':
            return InfogestiContributors.objects.raw(
                "select * from IG_CONTRIBUYENTE_PN@infogesti info INNER JOIN CORE_VILLACLARA v ON v.NUMEROIDENTIDAD =  info.NIT  and info.ES_PROPIETARIO_TT = '1' and UNIDAD = 2610 WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NIT")
        if city_name == 'Santo Domingo':
            return InfogestiContributors.objects.raw(
                "select * from IG_CONTRIBUYENTE_PN@infogesti info INNER JOIN CORE_VILLACLARA v ON v.NUMEROIDENTIDAD =  info.NIT  and info.ES_PROPIETARIO_TT = '1' and UNIDAD = 2611 WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NIT")
        if city_name == 'Ranchuelo':
            return InfogestiContributors.objects.raw(
                "select * from IG_CONTRIBUYENTE_PN@infogesti info INNER JOIN CORE_VILLACLARA v ON v.NUMEROIDENTIDAD =  info.NIT  and info.ES_PROPIETARIO_TT = '1' and UNIDAD = 2612 WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NIT")
        if city_name == 'Manicaragua':
            return InfogestiContributors.objects.raw(
                "select * from IG_CONTRIBUYENTE_PN@infogesti info INNER JOIN CORE_VILLACLARA v ON v.NUMEROIDENTIDAD =  info.NIT  and info.ES_PROPIETARIO_TT = '1' and UNIDAD = 2613 WHERE NOMBRE_COMPLETO <> DATOSPERSONA OR NUMEROIDENTIDAD <> NIT order by NIT")

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
