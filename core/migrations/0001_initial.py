# Generated by Django 4.2.11 on 2024-04-13 18:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tipo_usuario',
            fields=[
                ('id_tipo_usuairo', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id tipo usuario')),
                ('descripcion', models.CharField(max_length=15, verbose_name='Nombre tipo usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id_usuario', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id usuario')),
                ('username', models.CharField(max_length=30, verbose_name='username')),
                ('useremail', models.EmailField(max_length=254, verbose_name='email')),
                ('password', models.CharField(max_length=255, verbose_name='password')),
                ('perfil', models.IntegerField(blank=True, null=True, verbose_name='perfil')),
                ('id_tipo_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.tipo_usuario', verbose_name='Tipo_de_usuario')),
            ],
        ),
    ]
