from django.views.generic import TemplateView, CreateView
from .models import Product


class SaleCrateView(TemplateView):
    model = Product
    template_name = 'sale/create.html'
