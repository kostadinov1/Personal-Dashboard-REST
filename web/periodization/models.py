from django.db import models


class MicroCycle(models.Model):

    HINT = 'WEEK'

    name = models.CharField(max_length=30)
    start_date = models.DateField(blank=False, null=False)
    end_date = models.DateField(blank=False, null=False)
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    activities = []
    meals = []


class BlockCycle(models.Model):

    HINT = '2-6 WEEKS'
    name = models.CharField(max_length=30)
    start_date = models.DateField(blank=False, null=False)
    end_date = models.DateField(blank=False, null=False)
    description = models.TextField()
    micro_cycles = models.ForeignKey(MicroCycle, on_delete=models.CASCADE)


class MesoCycle(models.Model):

    HINT = '2-4 MONTHS'


    name = models.CharField(max_length=30)
    start_date = models.DateField(blank=False, null=False)
    end_date = models.DateField(blank=False, null=False)
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    block_cycles = models.ForeignKey(BlockCycle, on_delete=models.CASCADE)


class MacroCycle(models.Model):

    HINT = 'YEAR'

    name = models.CharField(max_length=30)
    start_date = models.DateField(blank=False, null=False)
    end_date = models.DateField(blank=False, null=False)
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    meso_cycles = models.ForeignKey(MesoCycle, on_delete=models.CASCADE)
