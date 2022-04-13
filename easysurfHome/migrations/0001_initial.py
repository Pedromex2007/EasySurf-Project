# Generated by Django 4.0.2 on 2022-04-13 15:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('phone_number', models.CharField(max_length=12)),
                ('visitor_relationship', models.CharField(choices=[('SO', 'Son'), ('DA', 'Daughter'), ('GS', 'Grandson'), ('GD', 'Granddaughter'), ('BR', 'Brother'), ('SI', 'Sister')], default='SO', max_length=2)),
                ('visitor_portrait', models.ImageField(default=None, null=True, upload_to='images/')),
                ('resident', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrientationResidentDate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orientation_date', models.DateTimeField(blank=True, default=None, null=True)),
                ('resident', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
