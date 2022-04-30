from django.contrib import admin
from .models import Category, ArtistType, Performances, Artists

# Register your models here.
admin.site.register(Category)
admin.site.register(ArtistType)
admin.site.register(Performances)
admin.site.register(Artists)
