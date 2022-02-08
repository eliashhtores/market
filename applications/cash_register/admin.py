from django.contrib import admin
from .models import CloseCashRegister


class CloseCashRegisterAdmin(admin.ModelAdmin):
    list_display = ('close_date', 'user', 'sales', 'amount')
    list_filter = ('close_date',)
    search_fields = ('close_date', 'user')
    ordering = ('close_date',)


admin.site.register(CloseCashRegister, CloseCashRegisterAdmin)
