from django.db import models
from django.db.models import Q


class ProductManager(models.Manager):
    # def get_queryset(self):
    #     return super().get_queryset().filter(active=True)

    def product_search(self, keyword):
        return self.filter(Q(barcode=keyword) | Q(name__icontains=keyword) | Q(description__icontains=keyword)).order_by('name')
