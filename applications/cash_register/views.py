from django.utils import timezone
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import TemplateView, View
from applications.sale.models import Sale
from applications.sale.functions import open_sales_detail
from .models import CloseCashRegister


class CashRegisterCloseView(TemplateView):
    template_name = 'cash_register/close.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['open_sales_detail'] = open_sales_detail
        context['daily_sold'] = Sale.objects.get_daily_sold()
        context['daily_canceled'] = Sale.objects.get_daily_canceled()
        context['total_sales'] = Sale.objects.get_open_sales().count()
        return context


class ProcessCloseCashRegisterView(View):
    def post(self, request, *args, **kwargs):
        closed, total = Sale.objects.close_all_sales()
        if closed:
            CloseCashRegister.objects.create(
                close_date=timezone.now(),
                sales=closed,
                amount=total,
                user=request.user
            )
        return HttpResponseRedirect(reverse('cash_register_app:close'))
