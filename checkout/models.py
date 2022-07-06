""" models for checkout-app """
import uuid  # used to generate order-number
from django.db import models
from django.db.models import Sum
from django.conf import settings
from performances.models import Product


class Order(models.Model):
    """ model for checkout each order """
    order_number = models.CharField(max_length=32, null=False, editable=False)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = models.CharField(max_length=40, null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(
        max_digits=20, decimal_places=0, null=False, default=0)

    def _generate_order_number(self):
        """ generate a random and unique ordernumber using UUID """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """ update total each time a line atem is added """
        self.order_total = self.lineitems.aggregate(
            Sum('lineitem_total'))['lineitem_total__sum']
        self.grand_total = self.order_total
        self.save()

    def save(self, *args, **kwargs):
        """
        override default save-method to set the ordernumber,
        if not set already
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    """ model for each shoppingbag-item """
    order = models.ForeignKey(
        Order, null=False, blank=False,
        related_name='lineitems', on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, null=False, blank=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(
        max_digits=10, decimal_places=0, null=False, blank=False,
        editable=False)

    def save(self, *args, **kwargs):
        """
        override default save-method to set the lineitem-total,
        and update the order-total
        """
        self.lineitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'ID {self.product.id} on order {self.order.order_number}'