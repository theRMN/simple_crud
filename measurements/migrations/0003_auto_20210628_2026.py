# Generated by Django 3.2.4 on 2021-06-28 14:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('measurements', '0002_auto_20210628_1716'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='measurement',
            options={'verbose_name': 'Измерение температуры', 'verbose_name_plural': 'Измерения температуры'},
        ),
        migrations.AlterModelOptions(
            name='project',
            options={'verbose_name': 'Объект', 'verbose_name_plural': 'Объекты'},
        ),
    ]