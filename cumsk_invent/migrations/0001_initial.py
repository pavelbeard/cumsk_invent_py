# Generated by Django 4.0.6 on 2022-07-29 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CiscoDs',
            fields=[
                ('field_field', models.IntegerField(db_column='№', primary_key=True, serialize=False)),
                ('идентификатор_оборудования', models.TextField(blank=True, db_column='Идентификатор оборудования', null=True)),
                ('идентификатор_в_системе_управления_в_сети_field', models.TextField(blank=True, db_column='Идентификатор в системе управления (в сети)', null=True)),
                ('тип_объекта', models.TextField(blank=True, db_column='Тип объекта', null=True)),
                ('тип_оборудования', models.TextField(blank=True, db_column='Тип оборудования', null=True)),
                ('модель_оборудования', models.TextField(blank=True, db_column='Модель оборудования', null=True)),
                ('комкод', models.TextField(blank=True, db_column='Комкод', null=True)),
                ('код_производителя', models.TextField(blank=True, db_column='Код производителя', null=True)),
                ('производитель', models.TextField(blank=True, db_column='Производитель', null=True)),
                ('наименование_eng_field', models.TextField(blank=True, db_column='Наименование (ENG)', null=True)),
                ('сеть', models.TextField(blank=True, db_column='Сеть', null=True)),
                ('код_железной_дороги', models.IntegerField(blank=True, db_column='Код железной дороги', null=True)),
                ('узел_связи', models.TextField(blank=True, db_column='Узел связи', null=True)),
                ('название_помещения', models.TextField(blank=True, db_column='Название помещения', null=True)),
                ('статус', models.TextField(blank=True, db_column='Статус', null=True)),
                ('комментарий_1', models.TextField(blank=True, db_column='Комментарий 1', null=True)),
                ('комментарий_2', models.TextField(blank=True, db_column='Комментарий 2', null=True)),
                ('комментарий_3', models.TextField(blank=True, db_column='Комментарий 3', null=True)),
                ('комментарий_4', models.TextField(blank=True, db_column='Комментарий 4', null=True)),
                ('комментарий_5', models.TextField(blank=True, db_column='Комментарий 5', null=True)),
                ('комментарий_6', models.TextField(blank=True, db_column='Комментарий 6', null=True)),
                ('комментарий_7', models.TextField(blank=True, db_column='Комментарий 7', null=True)),
            ],
            options={
                'db_table': 'cisco_ds',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Esmacards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iddevice', models.TextField(blank=True, null=True)),
                ('idnetwork', models.TextField(blank=True, null=True)),
                ('devicename', models.TextField(blank=True, null=True)),
                ('vendor', models.TextField(blank=True, null=True)),
                ('expdep', models.TextField(blank=True, null=True)),
                ('lastpolling', models.TextField(blank=True, null=True)),
                ('ip', models.TextField(blank=True, null=True)),
                ('originalid', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'esmacards',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Hardwareinfo',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('version', models.TextField(blank=True, null=True)),
                ('hostname', models.TextField(blank=True, null=True)),
                ('uptime', models.TextField(blank=True, null=True)),
                ('runningimage', models.TextField(blank=True, null=True)),
                ('hardware', models.TextField(blank=True, null=True)),
                ('serial', models.TextField(blank=True, null=True)),
                ('configregister', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'hardwareinfo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Nodetable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('node_id', models.TextField(blank=True, null=True)),
                ('label', models.TextField(blank=True, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('mac_address', models.TextField(blank=True, null=True)),
                ('parent_id', models.TextField(blank=True, null=True)),
                ('polling_agent', models.TextField(blank=True, null=True)),
                ('get_community', models.TextField(blank=True, null=True)),
                ('has_snmp', models.IntegerField(blank=True, null=True)),
                ('has_web', models.IntegerField(blank=True, null=True)),
                ('has_ftp', models.IntegerField(blank=True, null=True)),
                ('has_telent', models.IntegerField(blank=True, null=True)),
                ('has_rmon', models.IntegerField(blank=True, null=True)),
                ('has_smtp', models.IntegerField(blank=True, null=True)),
                ('has_tcp1', models.IntegerField(blank=True, null=True)),
                ('has_tcp2', models.IntegerField(blank=True, null=True)),
                ('has_tcp3', models.IntegerField(blank=True, null=True)),
                ('has_tcp4', models.IntegerField(blank=True, null=True)),
                ('node_group', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'nodetable',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Pingariumresults',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('protocol', models.TextField(blank=True, null=True)),
                ('status', models.TextField(blank=True, null=True)),
                ('host', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'pingariumresults',
                'managed': False,
            },
        ),
    ]
