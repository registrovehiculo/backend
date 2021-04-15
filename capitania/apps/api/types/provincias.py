from graphene_django.types import DjangoObjectType
from capitania.apps.core import models

class InfogestiContributorsType(DjangoObjectType):
    class Meta:
        model = models.InfogestiContributors

class ArtemisaType(DjangoObjectType):
    class Meta:
        model = models.Artemisa

class LaHabanaType(DjangoObjectType):
    class Meta:
        model = models.LaHabana

class CamagueyType(DjangoObjectType):
    class Meta:
        model = models.Camaguey


class CiegoDeAvilaType(DjangoObjectType):
    class Meta:
        model = models.CiegoDeAvila


class CienfuegosType(DjangoObjectType):
    class Meta:
        model = models.Cienfuegos


class SanticEspiritudType(DjangoObjectType):
    class Meta:
        model = models.SanticEspiritud


class GranmaType(DjangoObjectType):
    class Meta:
        model = models.Granma


class GuantanamoType(DjangoObjectType):
    class Meta:
        model = models.Guantanamo


class HolguinType(DjangoObjectType):
    class Meta:
        model = models.Holguin


class IslaDeLaJuventudType(DjangoObjectType):
    class Meta:
        model = models.IslaDeLaJuventud


class MatanzasType(DjangoObjectType):
    class Meta:
        model = models.Matanzas


class PinarDelRioType(DjangoObjectType):
    class Meta:
        model = models.PinarDelRio


class LasTunasType(DjangoObjectType):
    class Meta:
        model = models.LasTunas


class VillaClaraType(DjangoObjectType):
    class Meta:
        model = models.VillaClara


class MayabequeType(DjangoObjectType):
    class Meta:
        model = models.Mayabeque


class SantiagoDeCubaType(DjangoObjectType):
    class Meta:
        model = models.SantiagoDeCuba
