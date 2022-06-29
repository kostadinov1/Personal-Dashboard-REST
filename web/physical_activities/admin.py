from django.contrib import admin

from web.physical_activities.models import Exercise


@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    pass
