from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

from web.accounts.forms import UserRegistrationForm, UserChangeAdminForm
from web.accounts.models import Profile

CustomUserModel = get_user_model()


class CustomUserAdmin(UserAdmin):
    add_form = UserRegistrationForm
    form = UserChangeAdminForm
    model = CustomUserModel
    list_display = ('email', 'is_staff', 'is_active','is_superuser')
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('has_profile', 'is_staff', 'is_active', 'is_superuser', 'groups')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2','has_profile', 'is_staff', 'is_active', 'is_superuser', 'groups')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(CustomUserModel, CustomUserAdmin)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass

