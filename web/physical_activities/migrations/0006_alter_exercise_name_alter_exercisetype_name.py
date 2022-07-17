# Generated by Django 4.0.5 on 2022-07-17 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('physical_activities', '0005_exercise_sets'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='name',
            field=models.CharField(default='Movement', max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='exercisetype',
            name='name',
            field=models.CharField(default='General', max_length=30, unique=True),
        ),
    ]
