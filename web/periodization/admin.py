from django.contrib import admin

# Register your models here.
from web.periodization.models import MacroCycle, MesoCycle, MicroCycle, Goal, MiniGoal, Defender


@admin.register(MacroCycle)
class MacroCycleAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(MesoCycle)
class MesoCycleAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(MicroCycle)
class MicroCycleAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(MiniGoal)
class MiniGoalAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Defender)
class DefenderAdmin(admin.ModelAdmin):
    list_display = ('name',)

