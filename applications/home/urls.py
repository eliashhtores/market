from django.urls import path
from . import views


app_name = "home_app"

urlpatterns = [
    path('home/panel', views.SalesReportView.as_view(), name='home_panel'),
    path('home/sales-summary', views.SalesSummaryView.as_view(),
         name='home_sales_summary'),
]
