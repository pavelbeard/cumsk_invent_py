from django.db import models

# Create your models here.


class CiscoDs(models.Model):
    field_field = models.IntegerField(db_column='№', primary_key=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'.
    идентификатор_оборудования = models.TextField(db_column='Идентификатор оборудования', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    идентификатор_в_системе_управления_в_сети_field = models.TextField(db_column='Идентификатор в системе управления (в сети)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    тип_объекта = models.TextField(db_column='Тип объекта', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    тип_оборудования = models.TextField(db_column='Тип оборудования', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    модель_оборудования = models.TextField(db_column='Модель оборудования', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    комкод = models.TextField(db_column='Комкод', blank=True, null=True)  # Field name made lowercase.
    код_производителя = models.TextField(db_column='Код производителя', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    производитель = models.TextField(db_column='Производитель', blank=True, null=True)  # Field name made lowercase.
    наименование_eng_field = models.TextField(db_column='Наименование (ENG)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    сеть = models.TextField(db_column='Сеть', blank=True, null=True)  # Field name made lowercase.
    код_железной_дороги = models.IntegerField(db_column='Код железной дороги', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    узел_связи = models.TextField(db_column='Узел связи', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    название_помещения = models.TextField(db_column='Название помещения', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    статус = models.TextField(db_column='Статус', blank=True, null=True)  # Field name made lowercase.
    комментарий_1 = models.TextField(db_column='Комментарий 1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    комментарий_2 = models.TextField(db_column='Комментарий 2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    комментарий_3 = models.TextField(db_column='Комментарий 3', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    комментарий_4 = models.TextField(db_column='Комментарий 4', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    комментарий_5 = models.TextField(db_column='Комментарий 5', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    комментарий_6 = models.TextField(db_column='Комментарий 6', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    комментарий_7 = models.TextField(db_column='Комментарий 7', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    def __str__(self):
        return str(self.field_field)

    class Meta:
        managed = False
        db_table = 'cisco_ds'





class Esmacards(models.Model):
    iddevice = models.TextField(blank=True, null=True)
    idnetwork = models.TextField(blank=True, null=True)
    devicename = models.TextField(blank=True, null=True)
    vendor = models.TextField(blank=True, null=True)
    expdep = models.TextField(blank=True, null=True)
    lastpolling = models.TextField(blank=True, null=True)
    ip = models.TextField(blank=True, null=True)
    originalid = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'esmacards'


class Hardwareinfo(models.Model):
    id = models.IntegerField(primary_key=True)
    version = models.TextField(blank=True, null=True)
    hostname = models.TextField(blank=True, null=True)
    uptime = models.TextField(blank=True, null=True)
    runningimage = models.TextField(blank=True, null=True)
    hardware = models.TextField(blank=True, null=True)
    serial = models.TextField(blank=True, null=True)
    configregister = models.TextField(blank=True, null=True)
    pingariumresult_modelid = models.ForeignKey('Pingariumresults', models.DO_NOTHING, db_column='pingariumresult_modelid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hardwareinfo'


class Nodetable(models.Model):
    # node_id = models.TextField(blank=True, null=True)         //non primary key old
    node_id = models.TextField(blank=True, primary_key=True)
    label = models.TextField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    mac_address = models.TextField(blank=True, null=True)
    parent_id = models.TextField(blank=True, null=True)
    polling_agent = models.TextField(blank=True, null=True)
    get_community = models.TextField(blank=True, null=True)
    has_snmp = models.IntegerField(blank=True, null=True)
    has_web = models.IntegerField(blank=True, null=True)
    has_ftp = models.IntegerField(blank=True, null=True)
    has_telent = models.IntegerField(blank=True, null=True)
    has_rmon = models.IntegerField(blank=True, null=True)
    has_smtp = models.IntegerField(blank=True, null=True)
    has_tcp1 = models.IntegerField(blank=True, null=True)
    has_tcp2 = models.IntegerField(blank=True, null=True)
    has_tcp3 = models.IntegerField(blank=True, null=True)
    has_tcp4 = models.IntegerField(blank=True, null=True)
    node_group = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.label

    class Meta:
        managed = False
        db_table = 'nodetable'


class Pingariumresults(models.Model):
    id = models.IntegerField(primary_key=True)
    protocol = models.TextField(blank=True, null=True)
    status = models.TextField(blank=True, null=True)
    host = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pingariumresults'
