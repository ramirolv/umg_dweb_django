# Generated by Django 4.1.1 on 2022-09-11 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('creacion', models.DateTimeField(auto_now_add=True)),
                ('Estudiante', models.ManyToManyField(to='home.estudiante')),
            ],
        ),
    ]
