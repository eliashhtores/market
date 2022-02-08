from django.contrib import admin
from .models import Brand, Provider, Product


class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)
    ordering = ('name',)


class ProviderAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'web')
    list_filter = ('name',)
    search_fields = ('name', 'email', 'phone', 'web')
    ordering = ('name',)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('barcode', 'name', 'provider', 'brand', 'expiration_date',
                    'description', 'unit', 'qty_available', 'cost', 'price', 'sales')
    list_filter = ('name',)
    search_fields = ('barcode', 'name', 'provider', 'brand', 'expiration_date',
                     'description', 'unit', 'qty_available', 'cost', 'price', 'sales')
    ordering = ('name',)


admin.site.register(Brand, BrandAdmin)
admin.site.register(Provider, ProviderAdmin)
admin.site.register(Product, ProductAdmin)
