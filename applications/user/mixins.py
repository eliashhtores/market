from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from .models import User


def check_user_role(role, user_role):
    if role == User.ADMINISTRATOR or role == user_role:
        return False

    return True


class WarehousePermissionMixin(LoginRequiredMixin):
    login_url = reverse_lazy('user_app:user_login')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()

        if check_user_role(request.user.role, User.WAREHOUSE):
            return HttpResponseRedirect(reverse('user_app:user_login'))

        return super(WarehousePermissionMixin, self).dispatch(request, *args, **kwargs)


class SalesPermissionMixin(LoginRequiredMixin):
    login_url = reverse_lazy('user_app:user_login')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()

        if check_user_role(request.user.role, User.SALES):
            return HttpResponseRedirect(reverse('user_app:user_login'))

        return super(SalesPermissionMixin, self).dispatch(request, *args, **kwargs)


class AdminPermissionMixin(LoginRequiredMixin):
    login_url = reverse_lazy('user_app:user_login')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()

        if check_user_role(request.user.role, User.ADMINISTRATOR):
            return HttpResponseRedirect(reverse('user_app:user_login'))

        return super(AdminPermissionMixin, self).dispatch(request, *args, **kwargs)
