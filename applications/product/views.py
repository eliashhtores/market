from django.views.generic import View
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.http import HttpResponse
from applications.sale.models import Detail
from .models import Product
from .forms import ProductForm
from .utils import render_to_pdf


class ProductListView(ListView):
    template_name = 'product/list.html'
    model = Product


class ProductCreateView(CreateView):
    template_name = 'product/create.html'
    form_class = ProductForm
    success_url = reverse_lazy('product_app:product_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mode'] = 'Create product'
        return context


class ProductUpdateView(UpdateView):
    template_name = 'product/create.html'
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('product_app:product_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mode'] = 'Update product'
        return context


class ProductDeleteView(DeleteView):
    template_name = 'product/delete.html'
    model = Product
    success_url = reverse_lazy('product_app:product_list')


class ProductDetailView(DetailView):
    template_name = 'product/detail.html'
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sales'] = Detail.objects.get_monthly_sales(self.kwargs['pk'])
        return context


class ProductPrintView(View):
    def get(self, request, *args, **kwargs):
        product = Product.objects.get(id=self.kwargs['pk'])
        data = {
            'product': product,
            'monthly_sales': Detail.objects.get_monthly_sales(self.kwargs['pk'])
        }
        pdf = render_to_pdf('product/print.html', data)
        return HttpResponse(pdf, content_type='application/pdf')


class ProductReportView(ListView):
    template_name = 'product/report.html'

    def get_queryset(self):
        queryset = Product.objects.report_search(
            start_date=self.request.GET.get('start_date', ''),
            end_date=self.request.GET.get('end_date', ''),
            provider=self.request.GET.get('provider', ''),
            brand=self.request.GET.get('brand', ''),
        )
        return queryset
