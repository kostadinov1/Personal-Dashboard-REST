from django.db import models


class Goal(models.Model):
    NAME_MAX_LEN = 50

    name = models.CharField(max_length=NAME_MAX_LEN, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    deadline_date = models.DateField(blank=False, null=False)
    created_on = models.DateTimeField(auto_now_add=True)


class MiniGoal(models.Model):
    NAME_MAX_LEN = 50

    name = models.CharField(max_length=NAME_MAX_LEN, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    deadline_date = models.DateField(blank=False, null=False)
    created_on = models.DateTimeField(auto_now_add=True)


class Defender(models.Model):
    NAME_MAX_LEN = 50

    name = models.CharField(max_length=NAME_MAX_LEN, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    created_on = models.DateTimeField(auto_now_add=True)


# MICRO DURATION = 1 WEEK
class MicroCycle(models.Model):
    NAME_MAX_LEN = 50
    TAG = 'Week'

    name = models.CharField(max_length=NAME_MAX_LEN, blank=False, null=False, default='Micro Cycle')
    start_date = models.DateField(blank=False, null=False)
    end_date = models.DateField(blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)

    goals = models.ForeignKey(Goal, on_delete=models.CASCADE, blank=True, null=True)
    mini_goals = models.ForeignKey(MiniGoal, on_delete=models.CASCADE, blank=True, null=True)
    defenders = models.ForeignKey(Defender, on_delete=models.CASCADE, blank=True, null=True)

    activities = []


class MesoCycle(models.Model):
    NAME_MAX_LEN = 50
    TAG = 'Month/s'

    name = models.CharField(max_length=NAME_MAX_LEN, blank=False, null=False, default='Meso Cycle')
    start_date = models.DateField(blank=False, null=False)
    end_date = models.DateField(blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)

    goals = models.ForeignKey(Goal, on_delete=models.CASCADE, blank=True, null=True)
    mini_goals = models.ForeignKey(MiniGoal, on_delete=models.CASCADE, blank=True, null=True)
    defenders = models.ForeignKey(Defender, on_delete=models.CASCADE, blank=True, null=True)


class MacroCycle(models.Model):
    NAME_MAX_LEN = 50
    TAG = 'Year'

    name = models.CharField(max_length=NAME_MAX_LEN, blank=False, null=False, default='Macro Cycle')
    start_date = models.DateField(blank=False, null=False)
    end_date = models.DateField(blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)

    goals = models.ForeignKey(Goal, on_delete=models.CASCADE, blank=True, null=True)
    mini_goals = models.ForeignKey(MiniGoal, on_delete=models.CASCADE, blank=True, null=True)
    defenders = models.ForeignKey(Defender, on_delete=models.CASCADE, blank=True, null=True)
