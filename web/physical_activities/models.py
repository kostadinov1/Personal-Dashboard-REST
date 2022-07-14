from django.db import models

from web.periodization.models import Goal


class ActivityType(models.Model):
    NAME_MAX_LEN = 30

    name = models.CharField(max_length=NAME_MAX_LEN, null=False, blank=False, default='Physical')
    description = models.TextField(null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)


class Activity(models.Model):
    NAME_MAX_LEN = 30

    name = models.CharField(max_length=NAME_MAX_LEN, null=False, blank=False, default='Activity')
    description = models.TextField(null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    # ENDURANCE METRICS (WORKOUT TARGETS)
    distance = models.PositiveIntegerField(null=True, blank=True)
    pace = models.PositiveIntegerField(null=True, blank=True)
    speed = models.PositiveIntegerField(null=True, blank=True)
    heart_rate = models.PositiveIntegerField(null=True, blank=True)
    rpe = models.PositiveIntegerField(null=True, blank=True)

    type = models.ForeignKey(ActivityType, on_delete=models.CASCADE)
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE, blank=True, null=True)

# =========================================================================================================


class ExerciseType(models.Model):
    NAME_MAX_LEN = 30

    name = models.CharField(max_length=NAME_MAX_LEN, null=False, blank=False, default='General')
    description = models.TextField(null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)


class Exercise(models.Model):
    NAME_MAX_LEN = 30

    name = models.CharField(max_length=NAME_MAX_LEN, null=False, blank=False, default='Movement')
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    cues = models.TextField(null=True, blank=True)

    # BODYBUILDING METRICS
    reps = models.PositiveIntegerField(null=True, blank=True)
    sets = models.PositiveIntegerField(null=True, blank=True)
    weights_in_kg = models.PositiveIntegerField(null=True, blank=True)
    tempo = []
    calories_burned = models.PositiveIntegerField(null=True, blank=True)
    break_in_seconds = models.PositiveIntegerField(null=True, blank=True)

    type = models.ForeignKey(ExerciseType, on_delete=models.DO_NOTHING, null=True, blank=True)


