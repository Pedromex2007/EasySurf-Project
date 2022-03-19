# Generated by Django 4.0.2 on 2022-03-18 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='birth_date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='account',
            name='phone_number',
            field=models.PositiveIntegerField(default=0),
        ),
    ]