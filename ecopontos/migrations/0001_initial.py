# Generated by Django 4.2.1 on 2023-09-08 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ecopontos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cep', models.CharField(default='-', max_length=20)),
                ('bairro', models.CharField(default='-', max_length=20)),
                ('endereco', models.CharField(default='-', max_length=30)),
                ('situacao', models.CharField(default='-', max_length=10)),
            ],
        ),
    ]
