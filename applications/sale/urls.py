from django.urls import path
from . import views


app_name = "sale_app"

urlpatterns = [
    path('sale/create', views.SaleCrateView.as_view(), name='sale_create'),
    path('sale/update/<pk>', views.ShoppingCartUpdateView.as_view(),
         name='sale_update'),
    path('sale/delete/<pk>', views.ShoppingCartDeleteView.as_view(),
         name='sale_delete'),
    path('sale/delete-all', views.ShoppingCartDeleteAll.as_view(),
         name='sale_delete_all'),
    path('sale/process', views.SaleProcessView.as_view(), name='sale_process'),
    path('sale/voucher', views.SaleProcessVoucherView.as_view(),
         name='sale_voucher'),
    path('sale/create_voucher/<pk>', views.SaleCrateVoucherView.as_view(),
         name='sale_create_voucher'),

]
