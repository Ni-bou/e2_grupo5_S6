# Generated by Django 4.2.11 on 2024-04-28 07:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_usuario',
            fields=[
                ('id_tipo_usuario', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id tipo usuario')),
                ('descripcion', models.CharField(max_length=30, verbose_name='Nombre tipo usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id_usuario', models.AutoField(primary_key=True, serialize=False, verbose_name='Id usuario')),
                ('username', models.CharField(max_length=30, verbose_name='username')),
                ('useremail', models.EmailField(max_length=254, verbose_name='email')),
                ('password', models.CharField(max_length=255, verbose_name='password')),
                ('mascota_name', models.CharField(max_length=255, verbose_name='mascota_name')),
                ('id_tipo_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApp.tipo_usuario', verbose_name='Tipo usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('codigo_isbn', models.AutoField(primary_key=True, serialize=False, verbose_name='codigo_isbn_libro')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.CharField(blank=True, max_length=255, null=True)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='libros/')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='libros', to='myApp.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Autor_registro_libro',
            fields=[
                ('id_modificación', models.AutoField(primary_key=True, serialize=False, verbose_name='Id_modificación')),
                ('descripcion_realizado', models.CharField(blank=True, max_length=255, null=True)),
                ('codigo_isbn', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApp.libro', verbose_name='Libro')),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApp.usuario', verbose_name='modificación_libro_usuario')),
            ],
        ),
    ]
