from django.views.generic import FormView, View, DeleteView
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from applications.product.models import Product
from .models import ShoppingCart
from .forms import ShoppingCartForm


class SaleCrateView(FormView):
    template_name = 'sale/create.html'
    form_class = ShoppingCartForm
    success_url = 'create'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = ShoppingCart.objects.all().order_by('created')
        context['total'] = ShoppingCart.objects.get_total()
        # context['form_voucher'] = VoucherForm()

        return context

    def form_valid(self, form):
        barcode = form.cleaned_data['barcode']
        quantity = form.cleaned_data['quantity']
        product = Product.objects.get(barcode=barcode)

        obj, created = ShoppingCart.objects.get_or_create(
            barcode=barcode,
            defaults={
                'product': product,
                'quantity': quantity
            }
        )
        if not created:
            obj.quantity += quantity
            obj.save()

        return super(SaleCrateView, self).form_valid(form)


class ShoppingCartUpdateView(View):
    model = ShoppingCart

    def post(self, request, *args, **kwargs):
        cart = ShoppingCart.objects.get(id=self.kwargs.get('pk'))
        if cart.quantity == 1:
            cart.delete()
            return HttpResponseRedirect(reverse('sale_app:sale_create'))

        if cart.quantity > 1:
            cart.quantity -= 1
            cart.save()

        return HttpResponseRedirect(reverse('sale_app:sale_create'))


class ShoppingCartDeleteView(DeleteView):
    model = ShoppingCart
    success_url = reverse_lazy('sale_app:sale_create')


class ShoppingCartDeleteAll(View):

    def post(self, request, *args, **kwargs):
        ShoppingCart.objects.all().delete()
        return HttpResponseRedirect(reverse('sale_app:sale_create'))
