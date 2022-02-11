from django.urls import path
from . import views


app_name = "sale_app"

urlpatterns = [
    path('sale/create', views.SaleCrateView.as_view(), name='sale_create'),
    path('sale/update/<pk>', views.ShoppingCartUpdateView.as_view(),
         name='sale_update'),
    path('sale/delete/<pk>', views.ShoppingCartDeleteView.as_view(),
         name='sale_delete'),
    path('sale/delete_all', views.ShoppingCartDeleteAll.as_view(),
         name='sale_delete_all'),
    path('sale/', views.ProcessSaleView.as_view(), name='sale_process'),
]
