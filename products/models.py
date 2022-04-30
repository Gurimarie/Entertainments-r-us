from django.db import models


# Create your models here.
class Products(models.Model):

    class Meta:
        verbose_name_plural = 'Products'
        
    product_name = models.CharField(max_length=200)
    product_description = models.CharField(max_length=500, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.product_name
