# Generated by Django 3.1.3 on 2023-03-19 22:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='submission',
            name='date_submitted',
            field=models.DateField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AddField(
            model_name='submission',
            name='time',
            field=models.TimeField(default=django.utils.timezone.now, editable=False),
        ),
    ]
