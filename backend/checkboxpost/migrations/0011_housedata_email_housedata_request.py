# Generated by Django 4.0.2 on 2022-04-30 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkboxpost', '0010_delete_housedataimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='housedata',
            name='Email',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='housedata',
            name='request',
            field=models.BooleanField(null=True),
        ),
    ]
