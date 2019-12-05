# Generated by Django 2.2.8 on 2019-12-05 12:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='patient_info',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('names', models.CharField(max_length=255, unique=True)),
                ('telephone', models.CharField(max_length=10, null=True)),
                ('supporter_name', models.CharField(max_length=255, null=True)),
                ('supporter_telephone', models.CharField(max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Treatment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('started_treatment', models.DateTimeField()),
                ('first_refill', models.DateTimeField()),
                ('second_refill', models.DateTimeField()),
                ('patient', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.patient_info')),
            ],
        ),
    ]
