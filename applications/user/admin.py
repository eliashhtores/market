from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'full_name', 'role',
                    'gender', 'is_staff', 'is_active')
    list_filter = ('role',)
    search_fields = ('email', 'full_name', 'role')
    ordering = ('email',)


admin.site.register(User, UserAdmin)
