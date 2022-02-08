from django.views.generic.list import ListView
from .models import Product


class ProductListView(ListView):
    model = Product
    template_name = 'product/list.html'

    def get_queryset(self):
        keyword = self.request.GET.get('keyword', '')
        queryset = Product.objects.product_search(keyword=keyword)
        return queryset
