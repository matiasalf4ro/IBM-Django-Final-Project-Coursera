# Generated by Django 3.1.3 on 2023-03-20 05:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0004_auto_20230320_0511'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='correct',
            new_name='is_correct',
        ),
    ]
