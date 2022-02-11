from datetime import timedelta
from django.db import models
from django.utils import timezone
from django.db.models import Sum, F

from applications.product.models import Product


class SaleManager(models.Manager):
    def get_sales_by_date(self, date_start, date_end):
        return self.filter(sale=date_start, sale__lte=date_end)

    def get_open_sales(self):
        return self.filter(closed=False, canceled=False)


class DetailManager(models.Manager):
    def get_monthly_sales(self, product_id):
        end_date = timezone.now()
        start_date = end_date - timedelta(days=30)
        queryset = self.filter(
            sale__canceled=False,
            created__range=(start_date, end_date),
            product__id=product_id
        ).values('sale__date__date', 'product__name').annotate(quantity_sold=Sum('quantity'))
        return queryset

    def restore_stock(self, sale_id):
        canceled_products = []
        details = self.filter(sale__id=sale_id)
        for detail in details:
            detail.product.qty_available += detail.quantity
            detail.product.sales -= detail.quantity
            canceled_products.append(detail.product)

        Product.objects.bulk_update(
            canceled_products, ['qty_available', 'sales'])

    # def get_details_by_sale(self, product_id):
    #     return self.filter(sale__prod=product_id)


class ShoppingCartManager(models.Manager):
    def get_total(self):
        queryset = self.aggregate(total=Sum(
            F('quantity') * F('product__price'), output_field=models.FloatField()))

        return queryset['total']
