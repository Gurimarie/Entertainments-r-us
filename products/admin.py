""" admin-file for products """
from django.contrib import admin
from .models import Product

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    """ list what fields to show in the admin """
    list_display = (
        'product_name',
        'product_description',
        'price',
    )


admin.site.register(Product, ProductAdmin)
