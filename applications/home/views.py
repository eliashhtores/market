from django.views.generic import TemplateView
from applications.sale.models import Sale, Detail
from applications.product.models import Product


class SalesReportView(TemplateView):
    template_name = 'home/panel.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['daily_sold'] = Sale.objects.get_daily_sold()
        context['daily_canceled'] = Sale.objects.get_daily_canceled()
        context['no_inventory'] = Product.objects.get_no_inventory().count()
        context['weekly_sales'] = Detail.objects.get_weekly_sales()
        return context
