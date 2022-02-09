from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['barcode', 'name', 'provider', 'brand', 'unit', 'expiration_date',
                  'cost', 'price', 'qty_available', 'description']
        widgets = {
            'barcode': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'provider': forms.Select(attrs={'class': 'form-control'}),
            'brand': forms.Select(attrs={'class': 'form-control'}),
            'unit': forms.Select(attrs={'class': 'form-control'}),
            'expiration_date': forms.DateInput(
                format='%Y-%m-%d',
                attrs={'class': 'form-control', 'type': 'date'}),
            'cost': forms.NumberInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'qty_available': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }

    def clean_barcode(self):
        barcode = self.cleaned_data.get('barcode')
        if Product.objects.filter(barcode=barcode).exists():
            raise forms.ValidationError(
                'A product with this barcode already exists.')
        return barcode

    def clean_cost(self):
        cost = self.cleaned_data.get('cost')
        if cost < 0:
            raise forms.ValidationError('Cost must be greater than 0.')
        return cost

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price < 0:
            raise forms.ValidationError('Price must be greater than 0.')
        return price