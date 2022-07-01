from django.contrib import admin

# Register your models here.
from web.periodization.models import MacroCycle, MesoCycle, MicroCycle, Goal, MiniGoal, Defender


@admin.register(MacroCycle)
class MacroCycleAdmin(admin.ModelAdmin):
    pass


@admin.register(MesoCycle)
class MesoCycleAdmin(admin.ModelAdmin):
    pass


@admin.register(MicroCycle)
class MicroCycleAdmin(admin.ModelAdmin):
    pass


@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    pass


@admin.register(MiniGoal)
class MiniGoalAdmin(admin.ModelAdmin):
    pass


@admin.register(Defender)
class DefenderAdmin(admin.ModelAdmin):
    pass
