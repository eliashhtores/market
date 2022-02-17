from django.contrib import admin
from .models import Brand, Supplier, Product


class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)
    ordering = ('name',)


class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'web')
    list_filter = ('name',)
    search_fields = ('name', 'email', 'phone', 'web')
    ordering = ('name',)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('barcode', 'name', 'supplier', 'brand', 'expiration_date',
                    'description', 'unit', 'qty_available', 'cost', 'price', 'sales')
    list_filter = ('name',)
    search_fields = ('barcode', 'name', 'supplier', 'brand', 'expiration_date',
                     'description', 'unit', 'qty_available', 'cost', 'price', 'sales')
    ordering = ('name',)


admin.site.register(Brand, BrandAdmin)
admin.site.register(Supplier, SupplierAdmin)
admin.site.register(Product, ProductAdmin)
