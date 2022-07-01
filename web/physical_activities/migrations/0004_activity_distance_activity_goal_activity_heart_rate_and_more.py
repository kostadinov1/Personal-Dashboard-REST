# Generated by Django 4.0.5 on 2022-06-29 21:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('periodization', '0002_defender_goal_minigoal_remove_mesocycle_block_cycles_and_more'),
        ('physical_activities', '0003_exercise_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='distance',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='activity',
            name='goal',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='periodization.goal'),
        ),
        migrations.AddField(
            model_name='activity',
            name='heart_rate',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='activity',
            name='pace',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='activity',
            name='rpe',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='activity',
            name='speed',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='exercise',
            name='break_in_seconds',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='exercise',
            name='cues',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='exercise',
            name='reps',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='exercise',
            name='weights_in_kg',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='activity',
            name='name',
            field=models.CharField(default='Activity', max_length=30),
        ),
        migrations.AlterField(
            model_name='activitytype',
            name='name',
            field=models.CharField(default='Physical', max_length=30),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='name',
            field=models.CharField(default='Movement', max_length=30),
        ),
        migrations.AlterField(
            model_name='exercisetype',
            name='name',
            field=models.CharField(default='General', max_length=30),
        ),
    ]
