from django.db import models


class Goal(models.Model):
    name = models.CharField(max_length=40, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    deadline_date = models.DateField(blank=False, null=False)


class Defender(models.Model):
    name = models.CharField(max_length=40, blank=False, null=False)
    description = models.TextField(blank=False, null=False)


class MicroCycle(models.Model):
    # MICRO DURATION = 1 WEEK

    name = models.CharField(max_length=30, blank=False, null=False, default='Micro Cycle')
    start_date = models.DateField(blank=False, null=False)
    end_date = models.DateField(blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    goals = models.ForeignKey(Goal, on_delete=models.CASCADE)
    defenders = models.ForeignKey(Defender, on_delete=models.CASCADE)
    block_name = models.CharField(max_length=30, blank=True, null=True)
    activities = []
    meals = []


class MesoCycle(models.Model):
    # MESO DURATION =  1-4 MONTHS

    name = models.CharField(max_length=30)
    start_date = models.DateField(blank=False, null=False)
    end_date = models.DateField(blank=False, null=False)
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    micro_cycles = models.ForeignKey(MicroCycle, on_delete=models.CASCADE)

    goals = models.ForeignKey(Goal, on_delete=models.CASCADE)
    defenders = models.ForeignKey(Defender, on_delete=models.CASCADE)


class MacroCycle(models.Model):
    # MACRO DURATION = 1 YEAR

    name = models.CharField(max_length=30)
    start_date = models.DateField(blank=False, null=False)
    end_date = models.DateField(blank=False, null=False)
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    meso_cycles = models.ForeignKey(MesoCycle, on_delete=models.CASCADE)

    goals = models.ForeignKey(Goal, on_delete=models.CASCADE)
    defenders = models.ForeignKey(Defender, on_delete=models.CASCADE)


