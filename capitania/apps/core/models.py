import graphene
from cachecontrol import cache
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.timezone import now


class SingletonModel(models.Model):
    class Meta:
        abstract = True

    def set_cache(self):
        from cachecontrol import cache
        cache.set(self.__class__.__name__, self)

    def save(self, *args, **kwargs):
        self.pk = 1
        super(SingletonModel, self).save(*args, **kwargs)
        self.set_cache()

    def delete(self, *args, **kwargs):
        pass

    @classmethod
    def load(cls):
        if cache.get(cls.__name__) is None:
            obj, created = cls.objects.get_or_create(pk=1)
            if not created:
                obj.set_cache()
        return cache.get(cls.__name__)


class User(AbstractUser):
    """
    User account
    """
    genre = models.CharField(choices=(
        ('m', 'Masculino'),
        ('f', 'Femenino'),
    ), default='m', max_length=1, null=True, verbose_name='Género')

    # Related to login
    first_login = models.DateTimeField(verbose_name='primer inicio de sesión', null=True, blank=True)

    # Related to Users

    class Meta:
        db_table = 'user'
        verbose_name = 'usuario'
        verbose_name_plural = 'usuarios'

    def __str__(self):
        return str(self.username)

    def delete(self, **kwargs):
        remove = kwargs.pop('remove', None)
        if remove:
            super().delete(**kwargs)
        else:
            self.is_active = False
            self.is_staff = False
            self.is_superuser = False
            self.is_suspended = True
            self.suspended_at = now()
            self.suspended_reason = 'deleted_by_admin'

    def activate(self):
        self.is_active = True
        self.is_suspended = False
        self.suspended_at = None
        self.deactivated_at = None
        self.suspended_reason = None

    def deactivate(self):
        self.is_active = False
        self.is_staff = False
        self.is_superuser = False
        self.is_suspended = True
        self.suspended_at = now()
        self.deactivated_at = now()
        self.suspended_reason = 'auto_deleted'

    def suspend(self):
        self.is_suspended = True
        self.suspended_at = now()

    def get_name(self):
        if self.first_name not in [None, '']:
            return self.first_name
        else:
            return '@{}'.format(self.username)

    @staticmethod
    def is_username_taken(username):
        try:
            User.objects.get(username=username)
            return True
        except User.DoesNotExist:
            return False


class Vehiculo(models.Model):
    dpa = models.CharField(max_length=4, null=True, blank=True)
    municipio = models.CharField(max_length=400, null=True, blank=True)
    estadovehiculo = models.CharField(max_length=400, null=True, blank=True)
    marcavehiculo = models.CharField(max_length=400, null=True, blank=True)
    chapanueva = models.CharField(max_length=400, null=True, blank=True)
    numeromotor = models.CharField(max_length=400, null=True, blank=True)
    numerocarroseria = models.CharField(max_length=400, null=True, blank=True)
    marcamotor = models.CharField(max_length=400, null=True, blank=True)
    numeroidentidad = models.CharField(max_length=400, null=True, blank=True)
    datospersona = models.CharField(max_length=400, null=True, blank=True)
    direccion = models.CharField(max_length=400, null=True, blank=True)


class Artemisa(models.Model):
    dpa = models.CharField(max_length=4, null=True, blank=True)
    municipio = models.CharField(max_length=400, null=True, blank=True)
    estadovehiculo = models.CharField(max_length=400, null=True, blank=True)
    marcavehiculo = models.CharField(max_length=400, null=True, blank=True)
    chapanueva = models.CharField(max_length=400, null=True, blank=True)
    numeromotor = models.CharField(max_length=400, null=True, blank=True)
    numerocarroseria = models.CharField(max_length=400, null=True, blank=True)
    marcamotor = models.CharField(max_length=400, null=True, blank=True)
    numeroidentidad = models.CharField(max_length=400, null=True, blank=True)
    datospersona = models.CharField(max_length=400, null=True, blank=True)
    direccion = models.CharField(max_length=400, null=True, blank=True)


class LaHabana(models.Model):
    dpa = models.CharField(max_length=4, null=True, blank=True)
    municipio = models.CharField(max_length=400, null=True, blank=True)
    estadovehiculo = models.CharField(max_length=400, null=True, blank=True)
    marcavehiculo = models.CharField(max_length=400, null=True, blank=True)
    chapanueva = models.CharField(max_length=400, null=True, blank=True)
    numeromotor = models.CharField(max_length=400, null=True, blank=True)
    numerocarroseria = models.CharField(max_length=400, null=True, blank=True)
    marcamotor = models.CharField(max_length=400, null=True, blank=True)
    numeroidentidad = models.CharField(max_length=400, null=True, blank=True)
    datospersona = models.CharField(max_length=400, null=True, blank=True)
    direccion = models.CharField(max_length=400, null=True, blank=True)


class Camaguey(models.Model):
    dpa = models.CharField(max_length=4, null=True, blank=True)
    municipio = models.CharField(max_length=400, null=True, blank=True)
    estadovehiculo = models.CharField(max_length=400, null=True, blank=True)
    marcavehiculo = models.CharField(max_length=400, null=True, blank=True)
    chapanueva = models.CharField(max_length=400, null=True, blank=True)
    numeromotor = models.CharField(max_length=400, null=True, blank=True)
    numerocarroseria = models.CharField(max_length=400, null=True, blank=True)
    marcamotor = models.CharField(max_length=400, null=True, blank=True)
    numeroidentidad = models.CharField(max_length=400, null=True, blank=True)
    datospersona = models.CharField(max_length=400, null=True, blank=True)
    direccion = models.CharField(max_length=400, null=True, blank=True)


class CiegoDeAvila(models.Model):
    dpa = models.CharField(max_length=4, null=True, blank=True)
    municipio = models.CharField(max_length=400, null=True, blank=True)
    estadovehiculo = models.CharField(max_length=400, null=True, blank=True)
    marcavehiculo = models.CharField(max_length=400, null=True, blank=True)
    chapanueva = models.CharField(max_length=400, null=True, blank=True)
    numeromotor = models.CharField(max_length=400, null=True, blank=True)
    numerocarroseria = models.CharField(max_length=400, null=True, blank=True)
    marcamotor = models.CharField(max_length=400, null=True, blank=True)
    numeroidentidad = models.CharField(max_length=400, null=True, blank=True)
    datospersona = models.CharField(max_length=400, null=True, blank=True)
    direccion = models.CharField(max_length=400, null=True, blank=True)


class Cienfuegos(models.Model):
    dpa = models.CharField(max_length=4, null=True, blank=True)
    municipio = models.CharField(max_length=400, null=True, blank=True)
    estadovehiculo = models.CharField(max_length=400, null=True, blank=True)
    marcavehiculo = models.CharField(max_length=400, null=True, blank=True)
    chapanueva = models.CharField(max_length=400, null=True, blank=True)
    numeromotor = models.CharField(max_length=400, null=True, blank=True)
    numerocarroseria = models.CharField(max_length=400, null=True, blank=True)
    marcamotor = models.CharField(max_length=400, null=True, blank=True)
    numeroidentidad = models.CharField(max_length=400, null=True, blank=True)
    datospersona = models.CharField(max_length=400, null=True, blank=True)
    direccion = models.CharField(max_length=400, null=True, blank=True)


class Granma(models.Model):
    dpa = models.CharField(max_length=4, null=True, blank=True)
    municipio = models.CharField(max_length=400, null=True, blank=True)
    estadovehiculo = models.CharField(max_length=400, null=True, blank=True)
    marcavehiculo = models.CharField(max_length=400, null=True, blank=True)
    chapanueva = models.CharField(max_length=400, null=True, blank=True)
    numeromotor = models.CharField(max_length=400, null=True, blank=True)
    numerocarroseria = models.CharField(max_length=400, null=True, blank=True)
    marcamotor = models.CharField(max_length=400, null=True, blank=True)
    numeroidentidad = models.CharField(max_length=400, null=True, blank=True)
    datospersona = models.CharField(max_length=400, null=True, blank=True)
    direccion = models.CharField(max_length=400, null=True, blank=True)


class Guantanamo(models.Model):
    dpa = models.CharField(max_length=4, null=True, blank=True)
    municipio = models.CharField(max_length=400, null=True, blank=True)
    estadovehiculo = models.CharField(max_length=400, null=True, blank=True)
    marcavehiculo = models.CharField(max_length=400, null=True, blank=True)
    chapanueva = models.CharField(max_length=400, null=True, blank=True)
    numeromotor = models.CharField(max_length=400, null=True, blank=True)
    numerocarroseria = models.CharField(max_length=400, null=True, blank=True)
    marcamotor = models.CharField(max_length=400, null=True, blank=True)
    numeroidentidad = models.CharField(max_length=400, null=True, blank=True)
    datospersona = models.CharField(max_length=400, null=True, blank=True)
    direccion = models.CharField(max_length=400, null=True, blank=True)


class Holguin(models.Model):
    dpa = models.CharField(max_length=4, null=True, blank=True)
    municipio = models.CharField(max_length=400, null=True, blank=True)
    estadovehiculo = models.CharField(max_length=400, null=True, blank=True)
    marcavehiculo = models.CharField(max_length=400, null=True, blank=True)
    chapanueva = models.CharField(max_length=400, null=True, blank=True)
    numeromotor = models.CharField(max_length=400, null=True, blank=True)
    numerocarroseria = models.CharField(max_length=400, null=True, blank=True)
    marcamotor = models.CharField(max_length=400, null=True, blank=True)
    numeroidentidad = models.CharField(max_length=400, null=True, blank=True)
    datospersona = models.CharField(max_length=400, null=True, blank=True)
    direccion = models.CharField(max_length=400, null=True, blank=True)


class IslaDeLaJuventud(models.Model):
    dpa = models.CharField(max_length=4, null=True, blank=True)
    municipio = models.CharField(max_length=400, null=True, blank=True)
    estadovehiculo = models.CharField(max_length=400, null=True, blank=True)
    marcavehiculo = models.CharField(max_length=400, null=True, blank=True)
    chapanueva = models.CharField(max_length=400, null=True, blank=True)
    numeromotor = models.CharField(max_length=400, null=True, blank=True)
    numerocarroseria = models.CharField(max_length=400, null=True, blank=True)
    marcamotor = models.CharField(max_length=400, null=True, blank=True)
    numeroidentidad = models.CharField(max_length=400, null=True, blank=True)
    datospersona = models.CharField(max_length=400, null=True, blank=True)
    direccion = models.CharField(max_length=400, null=True, blank=True)


class LasTunas(models.Model):
    dpa = models.CharField(max_length=4, null=True, blank=True)
    municipio = models.CharField(max_length=400, null=True, blank=True)
    estadovehiculo = models.CharField(max_length=400, null=True, blank=True)
    marcavehiculo = models.CharField(max_length=400, null=True, blank=True)
    chapanueva = models.CharField(max_length=400, null=True, blank=True)
    numeromotor = models.CharField(max_length=400, null=True, blank=True)
    numerocarroseria = models.CharField(max_length=400, null=True, blank=True)
    marcamotor = models.CharField(max_length=400, null=True, blank=True)
    numeroidentidad = models.CharField(max_length=400, null=True, blank=True)
    datospersona = models.CharField(max_length=400, null=True, blank=True)
    direccion = models.CharField(max_length=400, null=True, blank=True)


class VillaClara(models.Model):
    dpa = models.CharField(max_length=4, null=True, blank=True)
    municipio = models.CharField(max_length=400, null=True, blank=True)
    estadovehiculo = models.CharField(max_length=400, null=True, blank=True)
    marcavehiculo = models.CharField(max_length=400, null=True, blank=True)
    chapanueva = models.CharField(max_length=400, null=True, blank=True)
    numeromotor = models.CharField(max_length=400, null=True, blank=True)
    numerocarroseria = models.CharField(max_length=400, null=True, blank=True)
    marcamotor = models.CharField(max_length=400, null=True, blank=True)
    numeroidentidad = models.CharField(max_length=400, null=True, blank=True)
    datospersona = models.CharField(max_length=400, null=True, blank=True)
    direccion = models.CharField(max_length=400, null=True, blank=True)


class Matanzas(models.Model):
    dpa = models.CharField(max_length=4, null=True, blank=True)
    municipio = models.CharField(max_length=400, null=True, blank=True)
    estadovehiculo = models.CharField(max_length=400, null=True, blank=True)
    marcavehiculo = models.CharField(max_length=400, null=True, blank=True)
    chapanueva = models.CharField(max_length=400, null=True, blank=True)
    numeromotor = models.CharField(max_length=400, null=True, blank=True)
    numerocarroseria = models.CharField(max_length=400, null=True, blank=True)
    marcamotor = models.CharField(max_length=400, null=True, blank=True)
    numeroidentidad = models.CharField(max_length=400, null=True, blank=True)
    datospersona = models.CharField(max_length=400, null=True, blank=True)
    direccion = models.CharField(max_length=400, null=True, blank=True)


class Mayabeque(models.Model):
    dpa = models.CharField(max_length=4, null=True, blank=True)
    municipio = models.CharField(max_length=400, null=True, blank=True)
    estadovehiculo = models.CharField(max_length=400, null=True, blank=True)
    marcavehiculo = models.CharField(max_length=400, null=True, blank=True)
    chapanueva = models.CharField(max_length=400, null=True, blank=True)
    numeromotor = models.CharField(max_length=400, null=True, blank=True)
    numerocarroseria = models.CharField(max_length=400, null=True, blank=True)
    marcamotor = models.CharField(max_length=400, null=True, blank=True)
    numeroidentidad = models.CharField(max_length=400, null=True, blank=True)
    datospersona = models.CharField(max_length=400, null=True, blank=True)
    direccion = models.CharField(max_length=400, null=True, blank=True)


class SantiagoDeCuba(models.Model):
    dpa = models.CharField(max_length=4, null=True, blank=True)
    municipio = models.CharField(max_length=400, null=True, blank=True)
    estadovehiculo = models.CharField(max_length=400, null=True, blank=True)
    marcavehiculo = models.CharField(max_length=400, null=True, blank=True)
    chapanueva = models.CharField(max_length=400, null=True, blank=True)
    numeromotor = models.CharField(max_length=400, null=True, blank=True)
    numerocarroseria = models.CharField(max_length=400, null=True, blank=True)
    marcamotor = models.CharField(max_length=400, null=True, blank=True)
    numeroidentidad = models.CharField(max_length=400, null=True, blank=True)
    datospersona = models.CharField(max_length=400, null=True, blank=True)
    direccion = models.CharField(max_length=400, null=True, blank=True)


class PinarDelRio(models.Model):
    dpa = models.CharField(max_length=4, null=True, blank=True)
    municipio = models.CharField(max_length=400, null=True, blank=True)
    estadovehiculo = models.CharField(max_length=400, null=True, blank=True)
    marcavehiculo = models.CharField(max_length=400, null=True, blank=True)
    chapanueva = models.CharField(max_length=400, null=True, blank=True)
    numeromotor = models.CharField(max_length=400, null=True, blank=True)
    numerocarroseria = models.CharField(max_length=400, null=True, blank=True)
    marcamotor = models.CharField(max_length=400, null=True, blank=True)
    numeroidentidad = models.CharField(max_length=400, null=True, blank=True)
    datospersona = models.CharField(max_length=400, null=True, blank=True)
    direccion = models.CharField(max_length=400, null=True, blank=True)


class SanticEspiritud(models.Model):
    dpa = models.CharField(max_length=4, null=True, blank=True)
    municipio = models.CharField(max_length=400, null=True, blank=True)
    estadovehiculo = models.CharField(max_length=400, null=True, blank=True)
    marcavehiculo = models.CharField(max_length=400, null=True, blank=True)
    chapanueva = models.CharField(max_length=400, null=True, blank=True)
    numeromotor = models.CharField(max_length=400, null=True, blank=True)
    numerocarroseria = models.CharField(max_length=400, null=True, blank=True)
    marcamotor = models.CharField(max_length=400, null=True, blank=True)
    numeroidentidad = models.CharField(max_length=400, null=True, blank=True)
    datospersona = models.CharField(max_length=400, null=True, blank=True)
    direccion = models.CharField(max_length=400, null=True, blank=True)


class Address(models.Model):
    city = models.ForeignKey('City', on_delete=models.CASCADE, null=True, blank=True)
    state = models.ForeignKey('State', on_delete=models.CASCADE, null=True, blank=True)
    country = models.ForeignKey('Country', on_delete=models.CASCADE, null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    class Meta:
        db_table = 'address'

    def __str__(self):
        return '{},{},{}'.format(
            self.city,
            self.state,
            self.country
        )

    def __copy__(self):
        return Address.objects.create(
            city=self.city,
            state=self.state,
            country=self.country
        )


class Country(models.Model):
    code = models.CharField(primary_key=True, max_length=3)
    code_iso2 = models.CharField(max_length=2, unique=True, null=True)
    name_es = models.CharField(max_length=100, default='')
    name_en = models.CharField(max_length=100, default='')
    name_fr = models.CharField(max_length=100, default='')

    class Meta:
        db_table = 'geo_country'
        ordering = ('name_es',)
        verbose_name_plural = 'countries'

    def __str__(self):
        return self.name_es


class State(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'geo_state'

    def __str__(self):
        return self.name


class City(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    latitude = models.CharField(max_length=255, null=True)
    longitude = models.CharField(max_length=255, null=True)

    class Meta:
        db_table = 'geo_city'
        verbose_name_plural = 'cities'

    def __str__(self):
        return self.name


class InfogestiContributors(models.Model):
    nit = models.CharField(max_length=11, blank=True, null=True)
    unidad = models.CharField(max_length=4, blank=True, null=True)
    nombre_completo = models.CharField(max_length=100, blank=True, null=True)
    direccion_principal = models.CharField(max_length=200, blank=True, null=True)
    es_propietario_tt = models.NullBooleanField()

    class Meta:
        db_table = u'"INFOGESTI"."IG_CONTRIBUYENTE_PN"'
        managed = False


class Shipment(models.Model):
    province_number = models.CharField(max_length=2, blank=True, null=True)
    id_number = models.CharField(max_length=11, blank=True, null=True)
    owner_name = models.CharField(max_length=255, blank=True, null=True)
    registry_number = models.CharField(max_length=255, blank=True, null=True)
    shipment_name = models.CharField(max_length=255, blank=True, null=True)
    captaincy_province = models.CharField(max_length=255, blank=True, null=True)
    base_name = models.CharField(max_length=255, blank=True, null=True)


class InfogestiShipment(models.Model):
    class Meta:
        db_table = u'"INFOGESTI"."CLIENTE_EMBARCACION"'
        managed = False


class Cliente(models.Model):
    nombre_completo = models.CharField(max_length=100, blank=True, null=True)
    nit = models.CharField(max_length=11, blank=True, null=True)
    dpa = models.CharField(max_length=4, blank=True, null=True)
    nombre_embarcacion = models.CharField(max_length=50, blank=True, null=True)


    class Meta:
        db_table = u'"INFOGESTI"."CLIENTE"'
        managed = False
