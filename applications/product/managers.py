from datetime import timedelta
from django.db import models
from django.utils import timezone


class ProductManager(models.Manager):

    def report_search(self, **kwargs):
        kwargs['start_date'] = timezone.now().date(
        ) - timedelta(days=30) if kwargs['start_date'] == '' else kwargs['start_date']
        kwargs['end_date'] = timezone.now().date(
        ) + timedelta(days=30) if kwargs['end_date'] == '' else kwargs['end_date']
        return self.filter(expiration_date__range=[kwargs['start_date'], kwargs['end_date']]).filter(
            brand__name__icontains=kwargs['brand'], provider__name__icontains=kwargs['provider'])

    def get_no_inventory(self):
        return self.filter(qty_available=0)
