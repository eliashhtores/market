from django.views.generic import ListView, UpdateView
from django.views.generic.edit import FormView
from django.urls import reverse
from django.shortcuts import redirect
from .models import User
from .forms import UserCreateForm


class UserCreateView(FormView):
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
        return self._create_user(email, full_name, password, False, False, True, **kwargs)


class UserListView(ListView):
    model = User
    template_name = 'user/list.html'


class UserUpdateView(UpdateView):
    model = User
    template_name = 'user/edit.html'
    fields = ['__all__']
