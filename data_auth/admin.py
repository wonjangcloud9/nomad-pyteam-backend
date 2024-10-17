from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from data_auth.models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (
            'Profile',
            {
                'fields': (
                    'username',
                    'password',
                ),
                'classes': ('wide',),
            },
        ),
        (
            'Important Dates',
            {
                'fields': ('last_login', 'date_joined'),
                'classes': ('collapse',),
            },
        ),
    )

    list_display = ('id', 'username',)
    readonly_fields = ('id', 'last_login', 'date_joined',)
