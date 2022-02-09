from datetime import timedelta
from django.db import models
from django.utils import timezone
from django.db.models import Sum


class SaleManager(models.Manager):
    def get_sales_by_date(self, date_start, date_end):
        return self.filter(sale=date_start, sale__lte=date_end)


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

    # def get_details_by_sale(self, product_id):
    #     return self.filter(sale__prod=product_id)


class ShoppingCartManager(models.Manager):
    def get_products_by_barcode(self, barcode):
        return self.filter(barcode=barcode)
