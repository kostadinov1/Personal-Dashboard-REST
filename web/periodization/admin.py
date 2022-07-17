from django.contrib import admin

from web.periodization.models import Goal, MiniGoal, Defender, MicroCycle, MesoCycle, MacroCycle


@admin.register(MicroCycle)
class MicroCycleAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(MesoCycle)
class MesoCycleAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(MacroCycle)
class MacroCycleAdmin(admin.ModelAdmin):
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

