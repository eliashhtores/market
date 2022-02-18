from django.urls import path
from . import views


app_name = "home_app"

urlpatterns = [
    path('home/panel', views.SalesReportView.as_view(), name='home_panel'),
<<<<<<< HEAD
    path('home/report', views.AdminReportView.as_view(), name='home_report'),
    path('home/supplier-payments', views.SupplierPaymentsView.as_view(),
         name='supplier_payments'),
=======
    path('home/sales-summary', views.SalesSummaryView.as_view(),
         name='home_sales_summary'),
>>>>>>> 1f41c429514b43b4ad938cf0c795412fb646ccde
]
