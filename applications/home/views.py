from django.views.generic import TemplateView, ListView
from applications.sale.models import Sale, Detail
from applications.product.models import Product
from .forms import SupplierPaymentsForm


class SalesReportView(TemplateView):
    template_name = 'home/panel.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['daily_sold'] = Sale.objects.get_daily_sold()
        context['daily_canceled'] = Sale.objects.get_daily_canceled()
        context['no_inventory'] = Product.objects.get_no_inventory().count()
        context['weekly_sales'] = Detail.objects.get_weekly_sales()
        return context


class AdminReportView(ListView):
    template_name = 'home/report.html'
    context_object_name = 'monthly_sales_summary'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_sold'] = Sale.objects.get_total_sold()
        return context

    def get_queryset(self):
        return Detail.objects.get_monthly_sales_summary()


class SupplierPaymentsView(ListView):
    template_name = 'home/supplier_payments.html'
    context_object_name = 'supplier_payments'
    extra_context = {'form': SupplierPaymentsForm}

    def get_queryset(self):
        sale_list, total_debt = Detail.objects.get_supplier_payments(
            supplier=self.request.GET.get('supplier'),
            start_date=self.request.GET.get('start_date'),
            end_date=self.request.GET.get('end_date')
        )
        self.extra_context['total_debt'] = total_debt

        return sale_list
