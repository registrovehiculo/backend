import graphene

from capitania.apps.api.types.provincias import ArtemisaType
from capitania.apps.core.models import Artemisa, PinarDelRio, Cienfuegos, LaHabana,\
    LasTunas, Camaguey, CiegoDeAvila, Granma, Guantanamo, Holguin, IslaDeLaJuventud, \
    SanticEspiritud, Matanzas, Mayabeque, VillaClara


class deleteRecords(graphene.ObjectType):
    delete = graphene.List(ArtemisaType)

    # 1 Contribuyentes que estan en capitania vehiculo que no estan en la onat
    def resolve_delete(self, info):
        # Artemisa.objects.all().delete()
        # PinarDelRio.objects.all().delete()
        # Cienfuegos.objects.all().delete()
        LaHabana.objects.all().delete()
        # Camaguey.objects.all().delete()
        # CiegoDeAvila.objects.all().delete()
        # LasTunas.objects.all().delete()
        # Granma.objects.all().delete()
        # Guantanamo.objects.all().delete()
        # Holguin.objects.all().delete()
        # IslaDeLaJuventud.objects.all().delete()
        # SanticEspiritud.objects.all().delete()
        # Matanzas.objects.all().delete()
        # Mayabeque.objects.all().delete()
        # VillaClara.objects.all().delete()


schema = graphene.Schema(query=deleteRecords, auto_camelcase=False)
