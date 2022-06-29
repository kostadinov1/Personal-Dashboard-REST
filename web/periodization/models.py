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

    name = models.CharField(max_length=NAME_MAX_LEN, blank=False, null=False, default='Micro Cycle')
    start_date = models.DateField(blank=False, null=False)
    end_date = models.DateField(blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    block_name = models.CharField(max_length=30, blank=True, null=True)

    goals = models.ForeignKey(Goal, on_delete=models.CASCADE)
    mini_goals = models.ForeignKey(MiniGoal, on_delete=models.CASCADE)
    defenders = models.ForeignKey(Defender, on_delete=models.CASCADE)

    activities = []
    meals = []


# MESO DURATION =  1-4 MONTHS
class MesoCycle(models.Model):
    NAME_MAX_LEN = 50

    name = models.CharField(max_length=NAME_MAX_LEN, blank=False, null=False, default='Meso Cycle')
    start_date = models.DateField(blank=False, null=False)
    end_date = models.DateField(blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)

    micro_cycles = models.ForeignKey(MicroCycle, on_delete=models.CASCADE)
    goals = models.ForeignKey(Goal, on_delete=models.CASCADE)
    mini_goals = models.ForeignKey(MiniGoal, on_delete=models.CASCADE)
    defenders = models.ForeignKey(Defender, on_delete=models.CASCADE)


# MACRO DURATION = 1 YEAR
class MacroCycle(models.Model):
    NAME_MAX_LEN = 50

    name = models.CharField(max_length=NAME_MAX_LEN, blank=False, null=False, default='Macro Cycle')
    start_date = models.DateField(blank=False, null=False)
    end_date = models.DateField(blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)

    meso_cycles = models.ForeignKey(MesoCycle, on_delete=models.CASCADE)
    goals = models.ForeignKey(Goal, on_delete=models.CASCADE)
    mini_goals = models.ForeignKey(MiniGoal, on_delete=models.CASCADE)
    defenders = models.ForeignKey(Defender, on_delete=models.CASCADE)


