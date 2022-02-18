from django.urls import path
from . import views


app_name = "user_app"

urlpatterns = [
    path('user/create', views.UserCreateView.as_view(), name='user_create'),
    path('user/list', views.UserListView.as_view(), name='user_list'),
]
