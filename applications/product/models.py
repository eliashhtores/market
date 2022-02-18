from model_utils.models import TimeStampedModel
from django.db import models
from .managers import ProductManager


class Brand(TimeStampedModel):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Supplier(TimeStampedModel):
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=40, blank=True, null=True)
    web = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name


class Product(TimeStampedModel):
    PIECE = 'PI'
    KILOGRAM = 'KG'
    LITTER = 'LT'
    METTER = 'MT'

    UNIT_CHOICES = (
        (PIECE, 'Piece'),
        (KILOGRAM, 'Kg'),
        (LITTER, 'Lt'),
        (METTER, 'Metter')
    )

    barcode = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=100)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    expiration_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    unit = models.CharField(max_length=2, choices=UNIT_CHOICES)
    qty_available = models.PositiveIntegerField(default=0)
    cost = models.DecimalField(max_digits=7, decimal_places=2)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    sales = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)

    objects = ProductManager()

    def __str__(self):
        return self.name
