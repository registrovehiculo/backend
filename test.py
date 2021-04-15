# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(unique=True, max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=255, blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class CoreIgContribuyentePn(models.Model):
    id = models.CharField(max_length=36, blank=True, null=True)
    unidad = models.CharField(max_length=4, blank=True, null=True)
    nit = models.CharField(max_length=11, blank=True, null=True)
    nombre_completo = models.CharField(max_length=100, blank=True, null=True)
    nombre_pais = models.CharField(max_length=20, blank=True, null=True)
    estado = models.NullBooleanField()
    fecha_alta = models.DateField(blank=True, null=True)
    fecha_baja = models.DateField(blank=True, null=True)
    nombre = models.CharField(max_length=30, blank=True, null=True)
    apellido1 = models.CharField(max_length=30, blank=True, null=True)
    apellido2 = models.CharField(max_length=30, blank=True, null=True)
    apodo = models.CharField(max_length=30, blank=True, null=True)
    num_ci = models.CharField(max_length=11, blank=True, null=True)
    num_ci_invalido = models.NullBooleanField()
    fecha_nacimiento = models.DateField(blank=True, null=True)
    sexo = models.NullBooleanField()
    militar = models.NullBooleanField()
    num_carne_militar = models.CharField(max_length=15, blank=True, null=True)
    extranjero = models.NullBooleanField()
    num_pasaporte = models.CharField(max_length=15, blank=True, null=True)
    afiliacion_seg_social = models.NullBooleanField()
    nombre_registro_seg_social = models.CharField(max_length=20, blank=True, null=True)
    nit_ct_ss = models.CharField(max_length=11, blank=True, null=True)
    nombre_ct_ss = models.CharField(max_length=100, blank=True, null=True)
    regimen = models.NullBooleanField()
    contabilidad = models.NullBooleanField()
    tcp_antes = models.NullBooleanField()
    cnt_empleado = models.IntegerField(blank=True, null=True)
    periodo_inicial_tcp = models.DateField(blank=True, null=True)
    periodo_final_tcp = models.DateField(blank=True, null=True)
    fecha_reinscripcion_tcp = models.DateField(blank=True, null=True)
    fecha_requerimiento_cbf = models.DateField(blank=True, null=True)
    cuentapropista_reinscripto = models.NullBooleanField()
    es_cuentapropista = models.NullBooleanField()
    es_arrendador = models.NullBooleanField()
    es_tcp = models.NullBooleanField()
    es_transportista = models.NullBooleanField()
    es_trabajador_contratado = models.NullBooleanField()
    es_sector_cultura = models.NullBooleanField()
    es_propietario_tt = models.NullBooleanField()
    es_propietario_embarcacion = models.NullBooleanField()
    calle_direccion = models.CharField(max_length=40, blank=True, null=True)
    numero_direccion = models.CharField(max_length=20, blank=True, null=True)
    entrecalles_direccion = models.CharField(max_length=60, blank=True, null=True)
    consejo_popular_direccion = models.CharField(max_length=50, blank=True, null=True)
    direccion_principal = models.CharField(max_length=200, blank=True, null=True)
    correo_electronico_principal = models.CharField(max_length=50, blank=True, null=True)
    telefono_principal = models.CharField(max_length=25, blank=True, null=True)
    lista_cuenta_bancaria = models.CharField(max_length=200, blank=True, null=True)
    lista_cuenta_bancaria_auxiliar = models.CharField(max_length=500, blank=True, null=True)
    lista_actividad = models.CharField(max_length=100, blank=True, null=True)
    lista_actividad_auxiliar = models.CharField(max_length=1000, blank=True, null=True)
    lista_obligacion = models.CharField(max_length=100, blank=True, null=True)
    lista_obligacion_auxiliar = models.CharField(max_length=500, blank=True, null=True)
    optimisticlockfield = models.BigIntegerField(blank=True, null=True)
    gcrecord = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'core_ig_contribuyente_pn'


class CoreVehiculo(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    municipio = models.CharField(max_length=400, blank=True, null=True)
    estadovehiculo = models.CharField(max_length=400, blank=True, null=True)
    marcavehiculo = models.CharField(max_length=400, blank=True, null=True)
    chapanueva = models.CharField(max_length=400, blank=True, null=True)
    numeromotor = models.CharField(max_length=400, blank=True, null=True)
    numerocarroseria = models.CharField(max_length=400, blank=True, null=True)
    marcamotor = models.CharField(max_length=400, blank=True, null=True)
    numeroidentidad = models.CharField(max_length=400, blank=True, null=True)
    datospersona = models.CharField(max_length=400, blank=True, null=True)
    direccion = models.CharField(max_length=400, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'core_vehiculo'


class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200, blank=True, null=True)
    action_flag = models.IntegerField()
    change_message = models.TextField(blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('User', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app_label = models.CharField(max_length=100, blank=True, null=True)
    model = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField(blank=True, null=True)
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class User(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    password = models.CharField(max_length=128, blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150, blank=True, null=True)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    email = models.CharField(max_length=254, blank=True, null=True)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    first_login = models.DateTimeField(blank=True, null=True)
    genre = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'


class UserGroups(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(User, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'user_groups'
        unique_together = (('user', 'group'),)


class UserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(User, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'user_user_permissions'
        unique_together = (('user', 'permission'),)
