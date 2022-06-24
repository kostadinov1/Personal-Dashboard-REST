from django.db import models


class TimeCycle(models.Model):
    start_date = models.DateField(blank=False, null=False)
    end_date = models.DateField(blank=False, null=False)
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    activities = []
    meals = []
    user = ''

