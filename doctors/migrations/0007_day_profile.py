# Generated by Django 5.0.3 on 2024-03-15 03:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0006_alter_prescription_author_shareddocument'),
    ]

    operations = [
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specialization', models.CharField(max_length=100)),
                ('hospital', models.CharField(max_length=100)),
                ('doctor_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='doctors.doctoruser')),
                ('working_days', models.ManyToManyField(to='doctors.day')),
            ],
        ),
    ]
