from django.urls import path
from . import views


app_name = "sale_app"

urlpatterns = [
    path('sale/create', views.SaleCrateView.as_view(), name='sale_create'),
    path('sale/update/<pk>', views.ShoppingCartUpdateView.as_view(),
         name='sale_update'),
    path('sale/delete/<pk>', views.SaleDeleteView.as_view(),
         name='sale_delete'),
    path('sale/cart-delete/<pk>', views.ShoppingCartDeleteView.as_view(),
         name='sale_cart_delete'),
    path('sale/delete-cart-all', views.ShoppingCartDeleteAll.as_view(),
         name='sale_delete_cart_all'),
    path('sale/process', views.SaleProcessView.as_view(), name='sale_process'),
    path('sale/voucher', views.SaleProcessVoucherView.as_view(),
         name='sale_voucher'),
    path('sale/create-voucher/<pk>', views.SaleCrateVoucherView.as_view(),
         name='sale_create_voucher'),
    path('sale/latest', views.SaleLatestView.as_view(), name='sale_latest'),
]
