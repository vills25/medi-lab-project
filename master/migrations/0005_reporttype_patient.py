# Generated by Django 5.0 on 2024-01-06 08:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0004_doctor'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReportType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('report_charge', models.FloatField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('mobile', models.CharField(max_length=255)),
                ('paid_payment', models.FloatField()),
                ('payment_status', models.CharField(default='pending', max_length=255)),
                ('address', models.TextField()),
                ('doctor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master.doctor')),
                ('report_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master.reporttype')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
