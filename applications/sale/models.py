from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from model_utils.models import TimeStampedModel
from applications.product.models import Product
from .managers import SaleManager, DetailManager, ShoppingCartManager
from .signals import update_stock


class Sale(TimeStampedModel):
    TICKET = 'T'
    INVOICE = 'I'
    NO_RECEIPT = 'N'

    CARD = 'CR'
    CASH = 'CA'
    OTHER = 'O'

    INVOICE_TYPE_CHOICES = [
        (TICKET, 'Ticket'),
        (INVOICE, 'Invoice'),
        (NO_RECEIPT, 'No Receipt')
    ]

    PAYMENT_TYPE_CHOICES = [
        (CARD, 'Card'),
        (CASH, 'Cash'),
        (OTHER, 'Other')
    ]

    date = models.DateTimeField(auto_now_add=True)
    quantity = models.PositiveIntegerField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    invoice_type = models.CharField(max_length=2, choices=INVOICE_TYPE_CHOICES)
    payment_type = models.CharField(max_length=2, choices=PAYMENT_TYPE_CHOICES)
    closed = models.BooleanField(default=False)
    canceled = models.BooleanField(default=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # noqa

    objects = SaleManager()

    def __str__(self):
        return 'Nº [' + str(self.id) + '] - ' + str(self.date)


class Detail(TimeStampedModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    sale = models.ForeignKey(
        Sale, on_delete=models.CASCADE, related_name='sale_details')
    quantity = models.PositiveIntegerField()
    tax = models.DecimalField(max_digits=5, decimal_places=2)

    objects = DetailManager()

    def __str__(self):
        return str(self.sale.id) + ' - ' + str(self.product.name)


class ShoppingCart(TimeStampedModel):
    barcode = models.CharField(max_length=50, unique=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    objects = ShoppingCartManager()

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return str(self.product.name)


post_save.connect(update_stock, sender=Detail)
