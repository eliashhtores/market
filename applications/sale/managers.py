from datetime import timedelta
from django.db import models
from django.utils import timezone
from django.db.models import Sum, F
from applications.product.models import Product


class SaleManager(models.Manager):
    def get_sales_by_date(self, start_date, end_date):
        return self.filter(date__gte=start_date, date__lte=end_date)

    def get_open_sales(self):
        return self.filter(closed=False, canceled=False)

    def get_daily_sold(self):
        daily_sold = self.filter(
            closed=False, canceled=False).aggregate(total=Sum('amount'))

        return daily_sold['total'] if daily_sold['total'] else 0

    def get_daily_canceled(self):
        daily_canceled = self.filter(
            closed=False, canceled=True).aggregate(total=Sum('amount'))

        return daily_canceled['total'] if daily_canceled['total'] else 0

    def close_all_sales(self):
        open_sales = self.get_open_sales()
        total = open_sales.aggregate(total=Sum('amount'))['total']
        closed = open_sales.update(closed=True)
        return closed, total


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

    def get_weekly_sales(self):
        end_date = timezone.now()
        start_date = end_date - timedelta(days=7)
        queryset = self.filter(
            sale__canceled=False,
            sale__closed=True,
            created__range=(start_date, end_date)).values('sale__date__date').annotate(
            total_sold=Sum(F('product__price')*F('quantity'),
                           output_field=models.FloatField()),
            profit=Sum(F('product__price')*F('quantity') - F('product__cost') *
                       F('quantity'), output_field=models.FloatField()),
            total=Sum('quantity'))
        return queryset

    # def get_details_by_sale(self, product_id):
    #     return self.filter(sale__prod=product_id)


class ShoppingCartManager(models.Manager):
    def get_total(self):
        queryset = self.aggregate(total=Sum(
            F('quantity') * F('product__price'), output_field=models.FloatField()))

        return queryset['total']
