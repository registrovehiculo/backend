import graphene
from capitania.apps.api.types.provincias import InfogestiContributorsType
from capitania.apps.core.models import InfogestiContributors


class ContributorsFromInfogestiQuery(graphene.ObjectType):
    infogesti_artemisa = graphene.List(InfogestiContributorsType, city_name=graphene.String())
    infogesti_camaguey = graphene.List(InfogestiContributorsType, city_name=graphene.String())
    infogesti_ciego = graphene.List(InfogestiContributorsType, city_name=graphene.String())
    infogesti_cienfuegos = graphene.List(InfogestiContributorsType, city_name=graphene.String())
    infogesti_granma = graphene.List(InfogestiContributorsType, city_name=graphene.String())
    infogesti_guantanamo = graphene.List(InfogestiContributorsType, city_name=graphene.String())
    infogesti_holguin = graphene.List(InfogestiContributorsType, city_name=graphene.String())
    infogesti_isla = graphene.List(InfogestiContributorsType, city_name=graphene.String())
    infogesti_tunas = graphene.List(InfogestiContributorsType, city_name=graphene.String())
    infogesti_matanzas = graphene.List(InfogestiContributorsType, city_name=graphene.String())
    infogesti_mayabeque = graphene.List(InfogestiContributorsType, city_name=graphene.String())
    infogesti_pinar = graphene.List(InfogestiContributorsType, city_name=graphene.String())
    infogesti_santiago = graphene.List(InfogestiContributorsType, city_name=graphene.String())
    infogesti_espiritud = graphene.List(InfogestiContributorsType, city_name=graphene.String())
    infogesti_villa = graphene.List(InfogestiContributorsType, city_name=graphene.String())
    infogesti_habana = graphene.List(InfogestiContributorsType, city_name=graphene.String())

    def resolve_infogesti_artemisa(self, info, city_name=graphene.String()):
        if city_name == 'Bahia Honda':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_ARTEMISA art ON art.NUMEROIDENTIDAD =  info.NIT WHERE art.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=2201 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'Alquizar':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_ARTEMISA art ON art.NUMEROIDENTIDAD =  info.NIT WHERE art.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=2202 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'Artemisa':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_ARTEMISA art ON art.NUMEROIDENTIDAD =  info.NIT WHERE art.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=2203 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'Bauta':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_ARTEMISA art ON art.NUMEROIDENTIDAD =  info.NIT WHERE art.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=2204 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'Caimito':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_ARTEMISA art ON art.NUMEROIDENTIDAD =  info.NIT WHERE art.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=2205 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'Candelaria':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_ARTEMISA art ON art.NUMEROIDENTIDAD =  info.NIT WHERE art.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=2206 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'Guanajay':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_ARTEMISA art ON art.NUMEROIDENTIDAD =  info.NIT WHERE art.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=2207 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'Gueira de Melena':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_ARTEMISA art ON art.NUMEROIDENTIDAD =  info.NIT WHERE art.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=2208 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'Mariel':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_ARTEMISA art ON art.NUMEROIDENTIDAD =  info.NIT WHERE art.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=2209 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'San Antonio de los Banos':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_ARTEMISA art ON art.NUMEROIDENTIDAD =  info.NIT WHERE art.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=2210 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'San Cristobal':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_ARTEMISA art ON art.NUMEROIDENTIDAD =  info.NIT WHERE art.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=2211 and info.ES_PROPIETARIO_TT = '1'")


    def resolve_infogesti_habana(self, info, city_name=graphene.String()):
        if city_name == 'Playa':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_LAHABANA hab ON hab.NUMEROIDENTIDAD =  info.NIT WHERE hab.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=2301 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'Plaza De La Revolucion':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_LAHABANA hab ON hab.NUMEROIDENTIDAD =  info.NIT WHERE hab.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=2302 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'Centro Habana':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_LAHABANA hab ON hab.NUMEROIDENTIDAD =  info.NIT WHERE hab.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=2303 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'La Habana Vieja':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_LAHABANA hab ON hab.NUMEROIDENTIDAD =  info.NIT WHERE hab.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=2304 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'Regla':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_LAHABANA hab ON hab.NUMEROIDENTIDAD =  info.NIT WHERE hab.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=2305 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'La Habana Del Este':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_LAHABANA hab ON hab.NUMEROIDENTIDAD =  info.NIT WHERE hab.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=2306 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'Guanabacoa':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_LAHABANA hab ON hab.NUMEROIDENTIDAD =  info.NIT WHERE hab.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=2307 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'San Miguel Del Padron':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_LAHABANA hab ON hab.NUMEROIDENTIDAD =  info.NIT WHERE hab.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=2308 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'Diez De Octubre':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_LAHABANA hab ON hab.NUMEROIDENTIDAD =  info.NIT WHERE hab.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=2309 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'Cerro':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_LAHABANA hab ON hab.NUMEROIDENTIDAD =  info.NIT WHERE hab.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=2310 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'Marianao':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_LAHABANA hab ON hab.NUMEROIDENTIDAD =  info.NIT WHERE hab.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=2311 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'La Lisa':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_LAHABANA hab ON hab.NUMEROIDENTIDAD =  info.NIT WHERE hab.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=2312 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'Boyeros':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_LAHABANA hab ON hab.NUMEROIDENTIDAD =  info.NIT WHERE hab.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=2313 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'Arroyo Naranjo':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_LAHABANA hab ON hab.NUMEROIDENTIDAD =  info.NIT WHERE hab.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=2314 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'Cotorro':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_LAHABANA hab ON hab.NUMEROIDENTIDAD =  info.NIT WHERE hab.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=2315 and info.ES_PROPIETARIO_TT = '1'")

    def resolve_infogesti_camaguey(self, info, city_name=graphene.String()):
        if city_name == 'Carlos Manuel De Cespedes':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_CAMAGUEY cmg ON cmg.NUMEROIDENTIDAD =  info.NIT WHERE cmg.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=3001 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'Esmeralda':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_CAMAGUEY cmg ON cmg.NUMEROIDENTIDAD =  info.NIT WHERE cmg.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=3002 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'Sierra De Cubitas':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_CAMAGUEY cmg ON cmg.NUMEROIDENTIDAD =  info.NIT WHERE cmg.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=3003 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'Minas':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_CAMAGUEY cmg ON cmg.NUMEROIDENTIDAD =  info.NIT WHERE cmg.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=3004 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'Nuevitas':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_CAMAGUEY cmg ON cmg.NUMEROIDENTIDAD =  info.NIT WHERE cmg.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=3005 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'Guaimaro':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_CAMAGUEY cmg ON cmg.NUMEROIDENTIDAD =  info.NIT WHERE cmg.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=3006 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'Sibanicu':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_CAMAGUEY cmg ON cmg.NUMEROIDENTIDAD =  info.NIT WHERE cmg.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=3007 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'Camagüey':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_CAMAGUEY cmg ON cmg.NUMEROIDENTIDAD =  info.NIT WHERE cmg.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=3008 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'Florida':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_CAMAGUEY cmg ON cmg.NUMEROIDENTIDAD =  info.NIT WHERE cmg.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=3009 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'Vertientes':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_CAMAGUEY cmg ON cmg.NUMEROIDENTIDAD =  info.NIT WHERE cmg.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=3010 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'Jimaguayu':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_CAMAGUEY cmg ON cmg.NUMEROIDENTIDAD =  info.NIT WHERE cmg.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=3011 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'Najasa':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_CAMAGUEY cmg ON cmg.NUMEROIDENTIDAD =  info.NIT WHERE cmg.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=3012 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'Santa Cruz del Sur':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_CAMAGUEY cmg ON cmg.NUMEROIDENTIDAD =  info.NIT WHERE cmg.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=3013 and info.ES_PROPIETARIO_TT = '1'")

    def resolve_infogesti_ciego(self, info, city_name=graphene.String()):
        if city_name == 'Chambas':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_CIEGODEAVILA cv ON cv.NUMEROIDENTIDAD =  info.NIT WHERE cv.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=2901 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'Moron':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_CIEGODEAVILA cv ON cv.NUMEROIDENTIDAD =  info.NIT WHERE cv.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=2902 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'Bolivia':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_CIEGODEAVILA cv ON cv.NUMEROIDENTIDAD =  info.NIT WHERE cv.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=2903 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'Primero De Enero':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_CIEGODEAVILA cv ON cv.NUMEROIDENTIDAD =  info.NIT WHERE cv.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=2904 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'Ciro Redondo':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_CIEGODEAVILA cv ON cv.NUMEROIDENTIDAD =  info.NIT WHERE cv.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=2905 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'Florencia':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_CIEGODEAVILA cv ON cv.NUMEROIDENTIDAD =  info.NIT WHERE cv.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=2906 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'Majagua':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_CIEGODEAVILA cv ON cv.NUMEROIDENTIDAD =  info.NIT WHERE cv.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=2907 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'Ciego de Avila':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_CIEGODEAVILA cv ON cv.NUMEROIDENTIDAD =  info.NIT WHERE cv.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=2908 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'Venezuela':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_CIEGODEAVILA cv ON cv.NUMEROIDENTIDAD =  info.NIT WHERE cv.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=2909 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'Baragua':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_CIEGODEAVILA cv ON cv.NUMEROIDENTIDAD =  info.NIT WHERE cv.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=2910 and info.ES_PROPIETARIO_TT = '1'")

    def resolve_infogesti_cienfuegos(self, info, city_name=graphene.String()):
        if city_name == 'Aguada de Pasajeros':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_CIENFUEGOS cf ON cf.NUMEROIDENTIDAD =  info.NIT WHERE cf.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=2701 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'Rodas':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_CIENFUEGOS cf ON cf.NUMEROIDENTIDAD =  info.NIT WHERE cf.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=2702 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'Palmira':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_CIENFUEGOS cf ON cf.NUMEROIDENTIDAD =  info.NIT WHERE cf.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=2703 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'las Lajas':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_CIENFUEGOS cf ON cf.NUMEROIDENTIDAD =  info.NIT WHERE cf.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=2704 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'Cruces':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_CIENFUEGOS cf ON cf.NUMEROIDENTIDAD =  info.NIT WHERE cf.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=2705 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'Cumanayagua':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_CIENFUEGOS cf ON cf.NUMEROIDENTIDAD =  info.NIT WHERE cf.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=2706 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'Cienfuegos':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_CIENFUEGOS cf ON cf.NUMEROIDENTIDAD =  info.NIT WHERE cf.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=2707 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'Abreus':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_CIENFUEGOS cf ON cf.NUMEROIDENTIDAD =  info.NIT WHERE cf.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=2708 and info.ES_PROPIETARIO_TT = '1'")

    def resolve_infogesti_granma(self, info, city_name=graphene.String()):
        if city_name == 'Rio Cauto':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_GRANMA g ON g.NUMEROIDENTIDAD =  info.NIT WHERE g.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=3301 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'Cauto Cristo':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_GRANMA g ON g.NUMEROIDENTIDAD =  info.NIT WHERE g.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=3302 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'Jiguani':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_GRANMA g ON g.NUMEROIDENTIDAD =  info.NIT WHERE g.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=3303 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'Bayamo':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_GRANMA g ON g.NUMEROIDENTIDAD =  info.NIT WHERE g.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=3304 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'Yara':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_GRANMA g ON g.NUMEROIDENTIDAD =  info.NIT WHERE g.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=3305 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'Manzanillo':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_GRANMA g ON g.NUMEROIDENTIDAD =  info.NIT WHERE g.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=3306 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'Campechuela':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_GRANMA g ON g.NUMEROIDENTIDAD =  info.NIT WHERE g.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=3307 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'Media Luna':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_GRANMA g ON g.NUMEROIDENTIDAD =  info.NIT WHERE g.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=3308 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'Niquero':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_GRANMA g ON g.NUMEROIDENTIDAD =  info.NIT WHERE g.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=3309 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'Pilon':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_GRANMA g ON g.NUMEROIDENTIDAD =  info.NIT WHERE g.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=3310 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'Bartolome Maso':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_GRANMA g ON g.NUMEROIDENTIDAD =  info.NIT WHERE g.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=3311 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'Buey Arriba':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_GRANMA g ON g.NUMEROIDENTIDAD =  info.NIT WHERE g.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=3312 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'Guisa':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_GRANMA g ON g.NUMEROIDENTIDAD =  info.NIT WHERE g.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=3313 and info.ES_PROPIETARIO_TT = '1'")

    def resolve_infogesti_isla(self, info, city_name=graphene.String()):
        return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_ISLADELAJUVENTUD i ON i.NUMEROIDENTIDAD =  info.NIT WHERE i.NUMEROIDENTIDAD IS NULL AND info.UNIDAD = 4001 and info.ES_PROPIETARIO_TT = '1'")

    def resolve_infogesti_tunas(self, info, city_name=graphene.String()):
        if city_name == 'Manati':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_LASTUNAS t ON t.NUMEROIDENTIDAD =  info.NIT WHERE t.NUMEROIDENTIDAD IS NULL AND info.UNIDAD = 3101 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'Puerto Padre':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_LASTUNAS t ON t.NUMEROIDENTIDAD =  info.NIT WHERE t.NUMEROIDENTIDAD IS NULL AND info.UNIDAD = 3102 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'Jesus Menendez':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_LASTUNAS t ON t.NUMEROIDENTIDAD =  info.NIT WHERE t.NUMEROIDENTIDAD IS NULL AND info.UNIDAD = 3103 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'Majibacoa':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_LASTUNAS t ON t.NUMEROIDENTIDAD =  info.NIT WHERE t.NUMEROIDENTIDAD IS NULL AND info.UNIDAD = 3104 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'Las Tunas':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_LASTUNAS t ON t.NUMEROIDENTIDAD =  info.NIT WHERE t.NUMEROIDENTIDAD IS NULL AND info.UNIDAD = 3105 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'Jobabo':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_LASTUNAS t ON t.NUMEROIDENTIDAD =  info.NIT WHERE t.NUMEROIDENTIDAD IS NULL AND info.UNIDAD = 3106 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'Colombia':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_LASTUNAS t ON t.NUMEROIDENTIDAD =  info.NIT WHERE t.NUMEROIDENTIDAD IS NULL AND info.UNIDAD = 3107 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'Amancio':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_LASTUNAS t ON t.NUMEROIDENTIDAD =  info.NIT WHERE t.NUMEROIDENTIDAD IS NULL AND info.UNIDAD = 3108 and info.ES_PROPIETARIO_TT = '1'")

    def resolve_infogesti_matanzas(self, info, city_name=graphene.String()):
        if city_name == 'Matanzas':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_MATANZAS m ON m.NUMEROIDENTIDAD =  info.NIT WHERE m.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=2501 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'Cardenas':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_MATANZAS m ON m.NUMEROIDENTIDAD =  info.NIT WHERE m.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=2502 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'Marti':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_MATANZAS m ON m.NUMEROIDENTIDAD =  info.NIT WHERE m.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=2503 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'Colon':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_MATANZAS m ON m.NUMEROIDENTIDAD =  info.NIT WHERE m.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=2504 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'Perico':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_MATANZAS m ON m.NUMEROIDENTIDAD =  info.NIT WHERE m.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=2505 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'Jovellanos':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_MATANZAS m ON m.NUMEROIDENTIDAD =  info.NIT WHERE m.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=2506 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'Pedro Betancourt':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_MATANZAS m ON m.NUMEROIDENTIDAD =  info.NIT WHERE m.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=2507 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'Limonar':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_MATANZAS m ON m.NUMEROIDENTIDAD =  info.NIT WHERE m.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=2508 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'Union de Reyes':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_MATANZAS m ON m.NUMEROIDENTIDAD =  info.NIT WHERE m.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=2509 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'Cienaga De Zapata':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_MATANZAS m ON m.NUMEROIDENTIDAD =  info.NIT WHERE m.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=2510 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'Jagüey Grande':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_MATANZAS m ON m.NUMEROIDENTIDAD =  info.NIT WHERE m.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=2511 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'Calimete':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_MATANZAS m ON m.NUMEROIDENTIDAD =  info.NIT WHERE m.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=2512 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'Los Arabos':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_MATANZAS m ON m.NUMEROIDENTIDAD =  info.NIT WHERE m.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=2513 and info.ES_PROPIETARIO_TT = '1'")


    def resolve_infogesti_mayabeque(self, info, city_name=graphene.String()):
        if city_name == 'Bejucal':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_MAYABEQUE m ON m.NUMEROIDENTIDAD =  info.NIT WHERE m.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=2401 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'San Jose de las Lajas':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_MAYABEQUE m ON m.NUMEROIDENTIDAD =  info.NIT WHERE m.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=2402 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'Jaruco':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_MAYABEQUE m ON m.NUMEROIDENTIDAD =  info.NIT WHERE m.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=2403 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'Santa Cruz del Norte':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_MAYABEQUE m ON m.NUMEROIDENTIDAD =  info.NIT WHERE m.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=2404 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'Madruga':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_MAYABEQUE m ON m.NUMEROIDENTIDAD =  info.NIT WHERE m.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=2405 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'Nueva Paz':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_MAYABEQUE m ON m.NUMEROIDENTIDAD =  info.NIT WHERE m.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=2406 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'San Nicolás':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_MAYABEQUE m ON m.NUMEROIDENTIDAD =  info.NIT WHERE m.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=2407 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'Güines':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_MAYABEQUE m ON m.NUMEROIDENTIDAD =  info.NIT WHERE m.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=2408 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'Melena del Sur':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_MAYABEQUE m ON m.NUMEROIDENTIDAD =  info.NIT WHERE m.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=2409 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'Batabano':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_MAYABEQUE m ON m.NUMEROIDENTIDAD =  info.NIT WHERE m.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=2410 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'Quivican':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_MAYABEQUE m ON m.NUMEROIDENTIDAD =  info.NIT WHERE m.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=2411 and info.ES_PROPIETARIO_TT = '1'")

    def resolve_infogesti_pinar(self, info, city_name=graphene.String()):
        if city_name == 'Sandino':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_PINARDELRIO p ON p.NUMEROIDENTIDAD =  info.NIT WHERE p.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=2101 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'Mantua':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_PINARDELRIO p ON p.NUMEROIDENTIDAD =  info.NIT WHERE p.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=2102 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'Minas De Matahambre':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_PINARDELRIO p ON p.NUMEROIDENTIDAD =  info.NIT WHERE p.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=2103 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'Viñales':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_PINARDELRIO p ON p.NUMEROIDENTIDAD =  info.NIT WHERE p.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=2104 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'La Palma':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_PINARDELRIO p ON p.NUMEROIDENTIDAD =  info.NIT WHERE p.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=2105 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'Los Palacios':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_PINARDELRIO p ON p.NUMEROIDENTIDAD =  info.NIT WHERE p.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=2106 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'Consolacion del Sur':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_PINARDELRIO p ON p.NUMEROIDENTIDAD =  info.NIT WHERE p.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=2107 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'Pinar del Rio':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_PINARDELRIO p ON p.NUMEROIDENTIDAD =  info.NIT WHERE p.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=2108 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'San Luis':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_PINARDELRIO p ON p.NUMEROIDENTIDAD =  info.NIT WHERE p.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=2109 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'San Juan y Martinez':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_PINARDELRIO p ON p.NUMEROIDENTIDAD =  info.NIT WHERE p.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=2110 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'Guane':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_PINARDELRIO p ON p.NUMEROIDENTIDAD =  info.NIT WHERE p.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=2111 and info.ES_PROPIETARIO_TT = '1'")

    def resolve_infogesti_santiago(self, info, city_name=graphene.String()):
        if city_name == 'Contramaestre':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_SANTIAGODECUBA s ON s.NUMEROIDENTIDAD =  info.NIT WHERE s.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=3401 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'Mella':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_SANTIAGODECUBA s ON s.NUMEROIDENTIDAD =  info.NIT WHERE s.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=3402 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'San Luis':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_SANTIAGODECUBA s ON s.NUMEROIDENTIDAD =  info.NIT WHERE s.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=3403 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'Segundo Frente':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_SANTIAGODECUBA s ON s.NUMEROIDENTIDAD =  info.NIT WHERE s.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=3404 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'Songo - La Maya':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_SANTIAGODECUBA s ON s.NUMEROIDENTIDAD =  info.NIT WHERE s.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=3405 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'Santiago de Cuba':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_SANTIAGODECUBA s ON s.NUMEROIDENTIDAD =  info.NIT WHERE s.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=3406 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'Palma Soriano':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_SANTIAGODECUBA s ON s.NUMEROIDENTIDAD =  info.NIT WHERE s.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=3407 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'Tercer Frente':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_SANTIAGODECUBA s ON s.NUMEROIDENTIDAD =  info.NIT WHERE s.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=3408 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'Guamá':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_SANTIAGODECUBA s ON s.NUMEROIDENTIDAD =  info.NIT WHERE s.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=3408 and info.ES_PROPIETARIO_TT = '1'")


    def resolve_infogesti_spirirtud(self, info, city_name=graphene.String()):
        if city_name == 'Yaguajay':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_SANTICESPIRITUD s ON s.NUMEROIDENTIDAD =  info.NIT WHERE s.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=2801 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'Jatibonico':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_SANTICESPIRITUD s ON s.NUMEROIDENTIDAD =  info.NIT WHERE s.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=2802 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'Taguasco':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_SANTICESPIRITUD s ON s.NUMEROIDENTIDAD =  info.NIT WHERE s.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=2803 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'Cabaiguán':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_SANTICESPIRITUD s ON s.NUMEROIDENTIDAD =  info.NIT WHERE s.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=2804 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'Fomento':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_SANTICESPIRITUD s ON s.NUMEROIDENTIDAD =  info.NIT WHERE s.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=2805 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'Trinidad':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_SANTICESPIRITUD s ON s.NUMEROIDENTIDAD =  info.NIT WHERE s.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=2806 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'Sancti Spiritus':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_SANTICESPIRITUD s ON s.NUMEROIDENTIDAD =  info.NIT WHERE s.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=2807 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'La Sierpe':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_SANTICESPIRITUD s ON s.NUMEROIDENTIDAD =  info.NIT WHERE s.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=2808 and info.ES_PROPIETARIO_TT = '1'")

    def resolve_infogesti_villa(self, info, city_name=graphene.String()):
        if city_name == 'Corralillo':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_VILLACLARA v ON v.NUMEROIDENTIDAD =  info.NIT WHERE v.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=2601 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'Quemado de Güines':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_VILLACLARA v ON v.NUMEROIDENTIDAD =  info.NIT WHERE v.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=2602 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'Sagua la Grande':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_VILLACLARA v ON v.NUMEROIDENTIDAD =  info.NIT WHERE v.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=2603 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'Encrucijada':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_VILLACLARA v ON v.NUMEROIDENTIDAD =  info.NIT WHERE v.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=2604 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'Camajuaní':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_VILLACLARA v ON v.NUMEROIDENTIDAD =  info.NIT WHERE v.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=2605 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'Caibarién':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_VILLACLARA v ON v.NUMEROIDENTIDAD =  info.NIT WHERE v.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=2606 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'San Juan de los Remedios':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_VILLACLARA v ON v.NUMEROIDENTIDAD =  info.NIT WHERE v.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=2607 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'Placetas':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_VILLACLARA v ON v.NUMEROIDENTIDAD =  info.NIT WHERE v.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=2608 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'Santa Clara':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_VILLACLARA v ON v.NUMEROIDENTIDAD =  info.NIT WHERE v.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=2609 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'Cifuentes':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_VILLACLARA v ON v.NUMEROIDENTIDAD =  info.NIT WHERE v.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=2610 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'Santo Domingo':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_VILLACLARA v ON v.NUMEROIDENTIDAD =  info.NIT WHERE v.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=2611 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'Ranchuelo':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_VILLACLARA v ON v.NUMEROIDENTIDAD =  info.NIT WHERE v.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=2612 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'Manicaragua':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_VILLACLARA v ON v.NUMEROIDENTIDAD =  info.NIT WHERE v.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=2613 and info.ES_PROPIETARIO_TT = '1'")


    def resolve_infogesti_holguin(self, info, city_name=graphene.String()):
        if city_name == 'Gibara':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_HOLGUIN h ON h.NUMEROIDENTIDAD =  info.NIT WHERE h.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=3201 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'Rafael Freyre':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_HOLGUIN h ON h.NUMEROIDENTIDAD =  info.NIT WHERE h.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=3202 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'Banes':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_HOLGUIN h ON h.NUMEROIDENTIDAD =  info.NIT WHERE h.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=3203 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'Antilla':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_HOLGUIN h ON h.NUMEROIDENTIDAD =  info.NIT WHERE h.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=3204 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'Baguanos':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_HOLGUIN h ON h.NUMEROIDENTIDAD =  info.NIT WHERE h.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=3205 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'Holguin':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_HOLGUIN h ON h.NUMEROIDENTIDAD =  info.NIT WHERE h.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=3206 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'Calixto Garcia':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_HOLGUIN h ON h.NUMEROIDENTIDAD =  info.NIT WHERE h.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=3207 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'Cacocum':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_HOLGUIN h ON h.NUMEROIDENTIDAD =  info.NIT WHERE h.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=3208 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'Urbano Noris':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_HOLGUIN h ON h.NUMEROIDENTIDAD =  info.NIT WHERE h.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=3209 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'Cueto':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_HOLGUIN h ON h.NUMEROIDENTIDAD =  info.NIT WHERE h.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=3210 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'Mayari':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_HOLGUIN h ON h.NUMEROIDENTIDAD =  info.NIT WHERE h.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=3211 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'Frank Pais':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_HOLGUIN h ON h.NUMEROIDENTIDAD =  info.NIT WHERE h.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=3212 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'Sagua de Tanamo':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_HOLGUIN h ON h.NUMEROIDENTIDAD =  info.NIT WHERE h.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=3213 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'Moa':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_HOLGUIN h ON h.NUMEROIDENTIDAD =  info.NIT WHERE h.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=3214 and info.ES_PROPIETARIO_TT = '1'")


    def resolve_infogesti_guantanamo(self, info, city_name=graphene.String()):
        if city_name == 'El Salvador':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_GUANTANAMO g ON g.NUMEROIDENTIDAD =  info.NIT WHERE g.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=3501 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'Manuel Tames':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_GUANTANAMO g ON g.NUMEROIDENTIDAD =  info.NIT WHERE g.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=3502 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'Yateras':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_GUANTANAMO g ON g.NUMEROIDENTIDAD =  info.NIT WHERE g.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=3503 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'Baracoa':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_GUANTANAMO g ON g.NUMEROIDENTIDAD =  info.NIT WHERE g.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=3504 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'Maisi':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_GUANTANAMO g ON g.NUMEROIDENTIDAD =  info.NIT WHERE g.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=3505 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'Imias':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_GUANTANAMO g ON g.NUMEROIDENTIDAD =  info.NIT WHERE g.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=3506 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'San Antonio Del Sur':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_GUANTANAMO g ON g.NUMEROIDENTIDAD =  info.NIT WHERE g.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=3507 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'Caimanera':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_GUANTANAMO g ON g.NUMEROIDENTIDAD =  info.NIT WHERE g.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=3508 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'Guantanamo':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_GUANTANAMO g ON g.NUMEROIDENTIDAD =  info.NIT WHERE g.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=3509 and info.ES_PROPIETARIO_TT = '1'")
        if city_name == 'Niceto Perez':
            return InfogestiContributors.objects.raw("select distinct * from IG_CONTRIBUYENTE_PN@infogesti info LEFT OUTER JOIN CORE_GUANTANAMO g ON g.NUMEROIDENTIDAD =  info.NIT WHERE g.NUMEROIDENTIDAD IS NULL AND info.UNIDAD=3510 and info.ES_PROPIETARIO_TT = '1'")


schema = graphene.Schema(query=ContributorsFromInfogestiQuery, auto_camelcase=False)
