from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from .models import Product
from .forms import ProductForm
from django.urls import reverse_lazy


class ProductListView(ListView):
    template_name = 'product/list.html'

    def get_queryset(self):
        keyword = self.request.GET.get('keyword', '')
        queryset = Product.objects.product_search(keyword=keyword)
        return queryset


class ProductCreateView(CreateView):
    template_name = 'product/create.html'
    form_class = ProductForm
    success_url = reverse_lazy('product_app:product_list')
