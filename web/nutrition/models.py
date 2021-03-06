from django.db import models


class MacroNutrient(models.Model):

    name = models.CharField(max_length=50)
    created_on = models.DateTimeField(auto_now_add=True)
    portion_size_in_grams = models.PositiveIntegerField()
    description = models.TextField()


class MicroNutrient(models.Model):

    name = models.CharField(max_length=50)
    created_on = models.DateTimeField(auto_now_add=True)
    portion_size_in_grams = models.PositiveIntegerField()
    description = models.TextField()


