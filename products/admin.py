from django.contrib import admin
from .models import Products

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'product_name',
        'product_description',
        'Procfile',
    )


admin.site.register(Products)
