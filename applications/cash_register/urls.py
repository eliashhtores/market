from django.urls import path
from . import views


app_name = "cash_register_app"

urlpatterns = [
    path('cash_register/close', views.CashRegisterCloseView.as_view(), name='close'),
    path('cash_register/proccess',
         views.ProcessCloseCashRegisterView.as_view(), name='process')
]
