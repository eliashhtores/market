from django.urls import path
from . import views


app_name = "sale_app"

urlpatterns = [
    path('sale/create', views.SaleCrateView.as_view(), name='sale_create'),
]
