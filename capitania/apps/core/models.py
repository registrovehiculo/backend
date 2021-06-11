from cachecontrol import cache
from datetime import timedelta
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
    province_number = models.CharField(max_length=2, blank=True, null=True, default=None)
    id_number = models.CharField(max_length=20, blank=True, null=True, default=None)
    owner_name = models.CharField(max_length=255, blank=True, null=True, default=None)
    registry_number = models.CharField(max_length=255, blank=True, null=True, default=None)
    shipment_name = models.CharField(max_length=255, blank=True, null=True, default=None)
    captaincy_province = models.CharField(max_length=255, blank=True, null=True, default=None)
    base_name = models.CharField(max_length=255, blank=True, null=True, default=None)


class InfogestiShipment(models.Model):
    class Meta:
        db_table = u'"INFOGESTI"."CLIENTE_EMBARCACION"'
        managed = False


class Cliente(models.Model):
    nombre_completo = models.CharField(max_length=100, blank=True, null=True)
    nit = models.CharField(max_length=11, blank=True, null=True)
    dpa = models.CharField(max_length=4, blank=True, null=True)
    embarcacion = models.CharField(max_length=50, blank=True, null=True)
    capitania = models.CharField(max_length=50, blank=True, null=True)
    basificacion = models.CharField(max_length=50, blank=True, null=True)
    registro = models.CharField(max_length=20, blank=True, null=True)
    matricula = models.CharField(max_length=20, blank=True, null=True)
    direccion = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        db_table = u'"INFOGESTI"."CLIENTE"'
        managed = False


class CreatedUpdatedModel(models.Model):
    """
    A model to reuse the `created_at` and `updated_at` fields
    """
    created_at = models.DateTimeField(default=now, null=True, verbose_name='Fecha de creación')
    updated_at = models.DateTimeField(null=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self._state.adding:
            self.updated_at = now()
        super().save(*args, **kwargs)

    @property
    def is_new(self):
        return self.created_at <= (now() - timedelta(days=1))


class DeletedModel(models.Model):
    """
    A model to reuse the `updated_at` field
    """

    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True

    def safe_delete(self):
        self.deleted_at = now()
        self.save()


class Review(CreatedUpdatedModel):
    """
    A review made by an user
    """
    text = models.CharField(max_length=200)
    reviewer = models.ForeignKey(User, related_name='reviewer', on_delete=models.CASCADE, verbose_name='Usuario')

    class Meta:
        db_table = 'review'
        verbose_name = 'comentario'
        verbose_name_plural = 'comentarios'

    def __str__(self):
        return self.text


class ReviewerAnswers(CreatedUpdatedModel):
    """
    An reviewer's answers made by an user
    """
    text = models.CharField(max_length=200)
    reviewer_answers = models.ForeignKey(Review, related_name='reviewer_answers', on_delete=models.CASCADE,
                                         verbose_name='Review')
    username = models.CharField(max_length=55,  null=True, blank=True)

    class Meta:
        db_table = 'ReviewerAnswers'
        verbose_name = 'respuestas'
        verbose_name_plural = 'respuestas'

    def __str__(self):
        return self.text
