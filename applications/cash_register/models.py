from django.db import models
from django.conf import settings
from model_utils.models import TimeStampedModel
from applications.product.models import Product


class CloseCashRegister(TimeStampedModel):
    close_date = models.DateTimeField()
    sales = models.PositiveIntegerField(default=0)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user.full_name) + ' - ' + str(self.close_date)
