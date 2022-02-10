from django.urls import path
from . import views


app_name = "product_app"

urlpatterns = [
    path('product/list', views.ProductListView.as_view(), name='product_list'),
    path('product/create', views.ProductCreateView.as_view(), name='product_create'),
    path('product/detail/<pk>', views.ProductDetailView.as_view(),
         name='product_detail'),
    path('product/update/<pk>', views.ProductUpdateView.as_view(),
         name='product_update'),
    path('product/delete/<pk>',
         views.ProductDeleteView.as_view(), name='product_delete'),
    path('product/print/<pk>', views.ProductPrintView.as_view(), name='product_print'),
]
