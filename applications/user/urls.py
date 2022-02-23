from django.urls import path
from . import views


app_name = "user_app"

urlpatterns = [
    path('', views.UserLoginView.as_view(), name='user_login'),
    path("user/logout", views.UserLogoutView.as_view(), name="user_logout"),
    path('user/create', views.UserCreateView.as_view(), name='user_create'),
    path('user/update/<pk>', views.UserUpdateView.as_view(), name='user_update'),
    path('user/delete/<pk>', views.UserDeleteView.as_view(), name='user_delete'),
    path('user/list', views.UserListView.as_view(), name='user_list'),
]
