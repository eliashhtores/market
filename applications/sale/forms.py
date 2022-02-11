from django import forms
from applications.product.models import Product
from .models import Sale


class ShoppingCartForm(forms.Form):
    barcode = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Barcode'}))
    quantity = forms.IntegerField(required=True, widget=forms.NumberInput(
        attrs={'class': 'form-control', 'placeholder': 'Quantity', 'value': 1, 'min': 1}))

    def clean(self):
        cleaned_data = super(ShoppingCartForm, self).clean()
        quantity = cleaned_data.get('quantity')
        barcode = cleaned_data.get('barcode')

        product = Product.objects.filter(barcode=barcode)
        if not product:
            self.add_error('barcode', 'Product not found')
            return cleaned_data

        product = Product.objects.get(barcode=barcode)
        if product.qty_available < quantity:
            self.add_error('quantity', 'Not enough stock')

        return cleaned_data


class VoucherForm(forms.Form):
    payment_type = forms.ChoiceField(
        required=True,
        choices=Sale.PAYMENT_TYPE_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    invoice_type = forms.ChoiceField(
        required=True,
        choices=Sale.INVOICE_TYPE_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
