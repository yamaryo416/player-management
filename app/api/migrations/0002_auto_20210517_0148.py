# Generated by Django 3.1.2 on 2021-05-17 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teamboard',
            name='coach',
            field=models.CharField(max_length=20),
        ),
    ]
