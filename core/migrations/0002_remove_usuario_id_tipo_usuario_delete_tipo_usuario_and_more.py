# Generated by Django 4.2.11 on 2024-04-28 06:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='id_tipo_usuario',
        ),
        migrations.DeleteModel(
            name='Tipo_usuario',
        ),
        migrations.DeleteModel(
            name='Usuario',
        ),
    ]
