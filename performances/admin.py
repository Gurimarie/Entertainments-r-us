from django.contrib import admin
from .models import Category, ArtistType, Performance, Artist


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'category_name'
    )


class ArtistTypeAdmin(admin.ModelAdmin):
    list_display = (
        'artist_type_name'
    )


class PerformanceAdmin(admin.ModelAdmin):
    list_display = (
        'artist_id',
        'performance_title',
        'performance_description',
        'composer',
        'video_url',
        'category',
    )


class ArtistAdmin(admin.ModelAdmin):
    list_display = (
        'artist_name',
        'artist_description',
        'image_url',
        'category',
        'artist_type',
    )


admin.site.register(Category)
admin.site.register(ArtistType)
admin.site.register(Performance)
admin.site.register(Artist)
