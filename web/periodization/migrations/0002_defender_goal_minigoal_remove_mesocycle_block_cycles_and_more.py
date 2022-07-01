# Generated by Django 4.0.5 on 2022-06-29 21:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('periodization', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Defender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('deadline_date', models.DateField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='MiniGoal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('deadline_date', models.DateField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='mesocycle',
            name='block_cycles',
        ),
        migrations.AddField(
            model_name='mesocycle',
            name='micro_cycles',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='periodization.microcycle'),
        ),
        migrations.AddField(
            model_name='microcycle',
            name='block_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='macrocycle',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='macrocycle',
            name='meso_cycles',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='periodization.mesocycle'),
        ),
        migrations.AlterField(
            model_name='macrocycle',
            name='name',
            field=models.CharField(default='Macro Cycle', max_length=50),
        ),
        migrations.AlterField(
            model_name='mesocycle',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='mesocycle',
            name='name',
            field=models.CharField(default='Meso Cycle', max_length=50),
        ),
        migrations.AlterField(
            model_name='microcycle',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='microcycle',
            name='name',
            field=models.CharField(default='Micro Cycle', max_length=50),
        ),
        migrations.DeleteModel(
            name='BlockCycle',
        ),
        migrations.AddField(
            model_name='macrocycle',
            name='defenders',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='periodization.defender'),
        ),
        migrations.AddField(
            model_name='macrocycle',
            name='goals',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='periodization.goal'),
        ),
        migrations.AddField(
            model_name='macrocycle',
            name='mini_goals',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='periodization.minigoal'),
        ),
        migrations.AddField(
            model_name='mesocycle',
            name='defenders',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='periodization.defender'),
        ),
        migrations.AddField(
            model_name='mesocycle',
            name='goals',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='periodization.goal'),
        ),
        migrations.AddField(
            model_name='mesocycle',
            name='mini_goals',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='periodization.minigoal'),
        ),
        migrations.AddField(
            model_name='microcycle',
            name='defenders',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='periodization.defender'),
        ),
        migrations.AddField(
            model_name='microcycle',
            name='goals',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='periodization.goal'),
        ),
        migrations.AddField(
            model_name='microcycle',
            name='mini_goals',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='periodization.minigoal'),
        ),
    ]