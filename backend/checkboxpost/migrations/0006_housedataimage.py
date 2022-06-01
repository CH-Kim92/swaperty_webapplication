# Generated by Django 4.0.2 on 2022-04-19 13:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('checkboxpost', '0005_alter_housedata_user_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='HouseDataImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('HouseData_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='checkboxpost.housedata')),
            ],
        ),
    ]
