from django.contrib import admin
from web.core.models import ToDoCategory, ToDo


@admin.register(ToDoCategory)
class ToDoCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(ToDo)
class ToDoAdmin(admin.ModelAdmin):
    list_display = ('title', 'email', 'content', 'created_on','is_done', 'category', 'user')

    @staticmethod
    def email(obj):
        return obj.user.email
