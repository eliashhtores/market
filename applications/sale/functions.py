from datetime import datetime
from django.db.models import F, ExpressionWrapper, Prefetch, FloatField
from applications.product.models import Product
from .models import Sale, Detail, ShoppingCart


def process_sale(**kwargs):
    TAX = .16
    # Get the shopping cart
    shopping_cart = ShoppingCart.objects.all()
    if shopping_cart.count() > 0:
        # Get the total
        total = ShoppingCart.objects.get_total()
        # Create the sale
        sale = Sale.objects.create(
            date=datetime.now(),
            quantity=0,
            amount=total,
            invoice_type=kwargs.get('invoice_type'),
            payment_type=kwargs.get('payment_type'),
            user=kwargs.get('user'),
        )
        # Create the details
        sale_details = []
        sale_products = []
        for cart in shopping_cart:
            sale_detail = Detail(
                product=cart.product,
                sale=sale,
                quantity=cart.quantity,
                tax=float(cart.product.price) * TAX,
            )
            sale.quantity += cart.quantity
            sale_details.append(sale_detail)
            product = cart.product
            product.qty_available -= cart.quantity
            product.sales += cart.quantity
            sale_products.append(product)
        sale.save()
        # Save the details
        Detail.objects.bulk_create(sale_details)
        # Update the product stock
        Product.objects.bulk_update(sale_products, ['qty_available', 'sales'])
        # Delete the shopping cart
        shopping_cart.delete()
        # Return the sale
        return sale


def open_sales_detail():
    open_sales = Sale.objects.get_open_sales()
    results = open_sales.prefetch_related(
        Prefetch(
            'sale_details',
            queryset=Detail.objects.filter(sale__id__in=open_sales).annotate(
                subtotal=ExpressionWrapper(
                    F('quantity') * F('product__price'), output_field=FloatField())
            )
        )
    ).order_by('id')

    return results
