from django.urls import path
from . import views


app_name = "home_app"

urlpatterns = [
    path('home/panel', views.SalesReportView.as_view(), name='home_panel'),
    path('home/report', views.AdminReportView.as_view(), name='home_report'),
    path('home/supplier-payments', views.SupplierPaymentsView.as_view(),
         name='supplier_payments'),
]
