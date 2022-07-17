from django.contrib import admin

from web.periodization.models import TimeCycle, Goal, MiniGoal, Defender


@admin.register(TimeCycle)
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

