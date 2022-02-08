from django.urls import path
from . import views


app_name = "product_app"

urlpatterns = [
    path('product/list', views.ProductListView.as_view(), name='product_list'),
    path('product/create', views.ProductCreateView.as_view(), name='product_create'),
]
