from django.db import models


class ActivityType(models.Model):
    NAME_MAX_LEN = 30

    name = models.CharField(max_length=NAME_MAX_LEN)
    description = models.TextField(null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)


class Activity(models.Model):
    NAME_MAX_LEN = 30

    name = models.CharField(max_length=NAME_MAX_LEN)
    # type = models.ForeignKey(ActivityType)

    description = models.TextField(null=True, blank=True)

    created_on = models.DateTimeField(auto_now_add=True)


class ExerciseType(models.Model):
    NAME_MAX_LEN = 30

    name = models.CharField(max_length=NAME_MAX_LEN)
    description = models.TextField(null=True, blank=True)

    created_on = models.DateTimeField(auto_now_add=True)


class Exercise(models.Model):
    NAME_MAX_LEN = 30

    name = models.CharField(max_length=NAME_MAX_LEN)
    # type = models.ForeignKey(ExerciseType, )
    description = models.TextField(null=True, blank=True)
    calories_burned = models.PositiveIntegerField()
    image = models.ImageField()


    created_on = models.DateTimeField(auto_now_add=True)


