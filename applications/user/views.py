from django.views.generic import ListView
from django.views.generic.edit import FormView
from .models import User
from .forms import UserCreateForm


class UserCreateView(FormView):
    template_name = "user/create.html"
    form_class = UserCreateForm
    success_url = "/"

    def form_valid(self, form):
        user = User.objects.create_user(
            form.cleaned_data["email"],
            form.cleaned_data["full_name"],
            form.cleaned_data["password"],
            form.cleaned_data["role"],
            gender=form.cleaned_data["gender"],
        )

    def create_user(self, email, full_name, password=None, role='0', **extra_fields):
        return self._create_user(email, full_name, password, role, False, False, True, **extra_fields)


class UserListView(ListView):
    model = User
    template_name = 'user/list.html'
