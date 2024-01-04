from django.conf import settings
from django.db import models
from django.contrib.gis.db import models

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Country(models.Model):
    name = models.CharField(max_length=50)
    iso = models.CharField(max_length=3)
    phone_code = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'country'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class PetBreed(models.Model):
    name = models.CharField(blank=True, null=True)
    species = models.ForeignKey('PetSpecies', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pet_breed'


class PetSpecies(models.Model):
    name = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pet_species'


class PetState(models.Model):
    name = models.CharField()

    class Meta:
        managed = False
        db_table = 'pet_state'


class Sex(models.Model):
    id = models.CharField(primary_key=True, max_length=1)
    name = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sex'


class Pet(models.Model):
    class LivingArrangment(models.TextChoices):
        indoor = 'indoor', 'Indoor'
        indoor_outdoor = 'indoor_outdoor', 'Indoor and outdoor'

    slug = models.CharField(unique=True, max_length=10)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=30)
    species = models.ForeignKey(PetSpecies, models.DO_NOTHING)
    breed = models.ForeignKey(PetBreed, models.DO_NOTHING, blank=True, null=True)
    state = models.ForeignKey(PetState, models.DO_NOTHING)
    birthday = models.DateField()
    sex = models.ForeignKey(Sex, models.DO_NOTHING)
    photo_url = models.CharField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    start_search_date = models.DateField()
    location_address = models.CharField()
    location_coordinates = models.PointField()  # This field type is a guess.
    microchip_id = models.IntegerField(blank=True, null=True)
    treat_motivated = models.BooleanField(blank=True, null=True)
    animal_friendly = models.BooleanField(blank=True, null=True)
    human_friendly = models.BooleanField(blank=True, null=True)
    living_arrangment = models.CharField(choices=LivingArrangment.choices)  # This field type is a guess.
    visible = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)


    class Meta:
        managed = False
        db_table = 'pet'



class PetReunited(models.Model):
    class ReunionType(models.TextChoices):
        lost = 'lost_reunion', 'Lost Reunion'
        found = 'found_reunion', 'Found Reunion'

    reunion_type = models.CharField(ReunionType.choices)  # This field type is a guess.
    pet = models.ForeignKey(Pet, models.DO_NOTHING, blank=True, null=True)
    reunited_details = models.ForeignKey('ReunitedDetails', models.DO_NOTHING, blank=True, null=True)


    class Meta:
        managed = False
        db_table = 'pet_reunited'

class DetailFoundDistance(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'detail_found_distance'


class DetailReunitedBy(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'detail_reunited_by'


class DetailReunitedTime(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'detail_reunited_time'

class ReunitedDetails(models.Model):
    reunited = models.BooleanField(blank=True, null=True)
    reunited_by = models.ForeignKey(DetailReunitedBy, models.DO_NOTHING, db_column='reunited_by', blank=True, null=True)
    found_distance = models.ForeignKey(DetailFoundDistance, models.DO_NOTHING, db_column='found_distance', blank=True, null=True)
    reunited_time = models.ForeignKey(DetailReunitedTime, models.DO_NOTHING, db_column='reunited_time', blank=True, null=True)
    reunion_story = models.TextField(blank=True, null=True)
    pet_microchiped = models.BooleanField(blank=True, null=True)
    recommend = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reunited_details'