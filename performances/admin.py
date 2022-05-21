""" admin-file for performances """
from django.contrib import admin
from .models import Category, ArtistType, Performance, Artist, Product


class CategoryAdmin(admin.ModelAdmin):
    """ list what fields to show in the admin """
    list_display = (
        'category_name',
    )


class ArtistTypeAdmin(admin.ModelAdmin):
    """ list what fields to show in the admin """
    list_display = (
        'artist_type_name',
    )


class PerformanceAdmin(admin.ModelAdmin):
    """ list what fields to show in the admin """
    list_display = (
        'artist_id',
        'performance_title',
        'performance_description',
        'composer',
        'video_url',
        'category',
    )


class ArtistAdmin(admin.ModelAdmin):
    """ list what fields to show in the admin """
    list_display = (
        'artist_name',
        'artist_description',
        'image_url',
        'category',
        'artist_type',
    )


class ProductAdmin(admin.ModelAdmin):
    """ list what fields to show in the admin """
    list_display = (
        'artist_id',
        'product_name',
        'product_description',
        'price',
    )


admin.site.register(Category, CategoryAdmin)
admin.site.register(ArtistType, ArtistTypeAdmin)
admin.site.register(Performance, PerformanceAdmin)
admin.site.register(Artist, ArtistAdmin)
admin.site.register(Product, ProductAdmin)
