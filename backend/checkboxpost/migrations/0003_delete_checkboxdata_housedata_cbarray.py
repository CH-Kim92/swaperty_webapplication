# Generated by Django 4.0.2 on 2022-03-20 13:15

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkboxpost', '0002_checkboxdata'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CheckBoxData',
        ),
        migrations.AddField(
            model_name='housedata',
            name='cbarray',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.BooleanField(), null=True, size=27),
        ),
    ]
