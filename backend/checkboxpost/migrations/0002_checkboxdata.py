# Generated by Django 4.0.2 on 2022-03-19 16:47

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkboxpost', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CheckBoxData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cbarray', django.contrib.postgres.fields.ArrayField(base_field=models.BooleanField(), null=True, size=27)),
            ],
        ),
    ]
