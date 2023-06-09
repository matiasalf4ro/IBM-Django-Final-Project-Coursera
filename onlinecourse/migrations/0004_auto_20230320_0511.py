# Generated by Django 3.1.3 on 2023-03-20 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0003_auto_20230320_0436'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='questions',
        ),
        migrations.AddField(
            model_name='question',
            name='courses',
            field=models.ManyToManyField(to='onlinecourse.Course'),
        ),
        migrations.AddField(
            model_name='question',
            name='marks',
            field=models.FloatField(default=1.0),
        ),
    ]
