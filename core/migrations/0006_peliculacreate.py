# Generated by Django 3.2.3 on 2021-06-22 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20210616_2157'),
    ]

    operations = [
        migrations.CreateModel(
            name='peliculaCreate',
            fields=[
                ('foto', models.ImageField(upload_to='photos', verbose_name='foto')),
                ('nombre', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='nombre')),
                ('sinopsis', models.TextField(verbose_name='sinopsis')),
            ],
        ),
    ]
