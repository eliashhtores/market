from django.views.generic import FormView, View, DeleteView, ListView
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse, reverse_lazy
from applications.user.mixins import SalesPermissionMixin
from applications.product.models import Product
from applications.product.utils import render_to_pdf
from .models import ShoppingCart, Sale, Detail
from .forms import ShoppingCartForm, VoucherForm
from .functions import process_sale


class SaleCrateView(SalesPermissionMixin, FormView):
    template_name = 'sale/create.html'
    form_class = ShoppingCartForm
    success_url = 'create'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = ShoppingCart.objects.all().order_by('created')
        context['total'] = ShoppingCart.objects.get_total()
        context['voucher_form'] = VoucherForm()

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


class ShoppingCartUpdateView(SalesPermissionMixin, View):
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


class ShoppingCartDeleteView(SalesPermissionMixin, DeleteView):
    model = ShoppingCart
    success_url = reverse_lazy('sale_app:sale_create')


class ShoppingCartDeleteAll(SalesPermissionMixin, View):

    def post(self, request, *args, **kwargs):
        ShoppingCart.objects.all().delete()
        return HttpResponseRedirect(reverse('sale_app:sale_create'))


class SaleProcessView(SalesPermissionMixin, View):

    def post(self, request, *args, **kwargs):
        process_sale(
            self=self,
            invoice_type=Sale.NO_RECEIPT,
            payment_type=Sale.CASH,
            user=request.user,
        )
        return HttpResponseRedirect(reverse('sale_app:sale_create'))


class SaleProcessVoucherView(SalesPermissionMixin, FormView):
    form_class = VoucherForm
    success_url = 'create'

    def form_valid(self, form):
        invoice_type = form.cleaned_data['invoice_type']
        payment_type = form.cleaned_data['payment_type']
        sale = process_sale(
            self=self,
            invoice_type=invoice_type,
            payment_type=payment_type,
            user=self.request.user,
        )

        if sale:
            return HttpResponseRedirect(reverse('sale_app:sale_create_voucher', kwargs={'pk': sale.id}))
        return HttpResponseRedirect(reverse('sale_app:sale_create'))


class SaleCrateVoucherView(SalesPermissionMixin, View):

    def get(self, request, *args, **kwargs):
        sale = Sale.objects.get(id=self.kwargs.get('pk'))
        data = {
            'sale': sale,
            'details': Detail.objects.filter(sale=sale),
        }
        pdf = render_to_pdf('sale/voucher.html', data)
        return HttpResponse(pdf, content_type='application/pdf')


class SaleLatestView(SalesPermissionMixin, ListView):
    model = Sale
    template_name = 'sale/latest.html'

    def get_queryset(self):
        return Sale.objects.get_open_sales()


class SaleDeleteView(SalesPermissionMixin, DeleteView):
    template_name = 'sale/delete.html'
    model = Sale
    success_url = reverse_lazy('sale_app:sale_latest')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.canceled = True
        self.object.save()
        Detail.objects.restore_stock(self.object.id)
        return HttpResponseRedirect(self.get_success_url())
