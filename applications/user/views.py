from django.views.generic import ListView, UpdateView, DeleteView, View
from django.views.generic.edit import FormView
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from .mixins import AdminPermissionMixin
from .models import User
from .forms import UserCreateForm, UserUpdateForm, LoginForm


class UserLoginView(FormView):
    template_name = "user/login.html"
    form_class = LoginForm
    success_url = reverse_lazy("product_app:product_list")

    def form_valid(self, form):
        user = authenticate(
            email=form.cleaned_data["email"],
            password=form.cleaned_data["password"],
        )
        login(self.request, user)
        return super(UserLoginView, self).form_valid(form)


class UserLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse("user_app:user_login"))


class UserCreateView(AdminPermissionMixin, FormView):
    template_name = "user/create.html"
    form_class = UserCreateForm
    success_url = "/"

    def form_valid(self, form):
        User.objects.create_user(
            form.cleaned_data["email"],
            form.cleaned_data["full_name"],
            form.cleaned_data["password"],
            role=form.cleaned_data["role"],
            gender=form.cleaned_data["gender"],
        )
        return redirect(reverse("user_app:user_list"))

    def create_user(self, email, full_name, password=None, **kwargs):
        return self._create_user(email, full_name, password, False, False, **kwargs)


class UserListView(AdminPermissionMixin, ListView):
    model = User
    template_name = 'user/list.html'


class UserUpdateView(AdminPermissionMixin, UpdateView):
    template_name = 'user/edit.html'
    model = User
    form_class = UserUpdateForm
    success_url = reverse_lazy('user_app:user_list')


class UserDeleteView(AdminPermissionMixin, DeleteView):
    template_name = 'user/delete.html'
    model = User
    success_url = reverse_lazy('user_app:user_list')
