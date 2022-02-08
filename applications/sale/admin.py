from django.contrib import admin
from .models import Sale, Detail, ShoppingCart


class SaleAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'quantity', 'amount',
                    'invoice_type', 'payment_type', 'closed', 'canceled', 'user')
    list_filter = ('date', 'invoice_type', 'payment_type',
                   'closed', 'canceled', 'user')
    search_fields = ('id', 'date', 'quantity', 'amount',
                     'invoice_type', 'payment_type', 'closed', 'canceled', 'user')
    ordering = ('id',)


class DetailAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'sale', 'quantity', 'tax')
    list_filter = ('product', 'sale')
    search_fields = ('id', 'product', 'sale', 'quantity', 'tax')
    ordering = ('id',)


class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = ('id', 'barcode', 'product', 'quantity')
    list_filter = ('barcode', 'product')
    search_fields = ('id', 'barcode', 'product', 'quantity')
    ordering = ('id',)


admin.site.register(Sale, SaleAdmin)
admin.site.register(Detail, DetailAdmin)
admin.site.register(ShoppingCart, ShoppingCartAdmin)
