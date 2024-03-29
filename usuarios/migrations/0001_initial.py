# Generated by Django 4.2.1 on 2023-09-08 21:04

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ecopontos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='-', max_length=30)),
                ('document', models.CharField(default='-', max_length=15)),
                ('email', models.CharField(default='-', max_length=30)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_active', models.BooleanField(default='true', max_length=30)),
                ('is_staff', models.BooleanField(default='false', max_length=30)),
                ('ecoponto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecopontos.ecopontos')),
            ],
        ),
    ]
