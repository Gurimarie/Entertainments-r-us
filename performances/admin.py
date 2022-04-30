from django.contrib import admin
from .models import Category, ArtistType, Performances, Artists


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'category_name'
    )


class ArtistTypeAdmin(admin.ModelAdmin):
    list_display = (
        'artist_type_name'
    )


class PerformancesAdmin(admin.ModelAdmin):
    list_display = (
        'artist_id',
        'performance_title',
        'performance_description',
        'composer',
        'video_url',
        'category',
    )


class ArtistsAdmin(admin.ModelAdmin):
    list_display = (
        'artist_name',
        'artist_description',
        'image_url',
        'category',
        'artist_type',
    )


admin.site.register(Category)
admin.site.register(ArtistType)
admin.site.register(Performances)
admin.site.register(Artists)
