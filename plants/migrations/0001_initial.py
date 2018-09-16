# Generated by Django 2.1.1 on 2018-09-16 04:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Plant',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='PlantDataPoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sensor_id', models.CharField(max_length=255)),
                ('sensor_name', models.CharField(max_length=255)),
                ('soil_humidity', models.IntegerField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('plant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plants.Plant')),
            ],
            options={
                'verbose_name': 'Plant data point',
            },
        ),
    ]
