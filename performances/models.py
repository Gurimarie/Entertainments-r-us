""" Models for app performances, incl. artists and products """
from django.db import models


class Category(models.Model):
    """ plural name to show in the admin """
    class Meta:
        verbose_name_plural = 'Categories'

    category_name = models.CharField(max_length=200)

    def __str__(self):
        return self.category_name


class ArtistType(models.Model):
    """ plural name to show in the admin """
    class Meta:
        verbose_name_plural = 'ArtistTypes'

    artist_type_name = models.CharField(max_length=200)

    def __str__(self):
        return self.artist_type_name


class Performance(models.Model):
    """ plural name to show in the admin """
    class Meta:
        verbose_name_plural = 'Performances'

    artist_id = models.ForeignKey(
        'Artist', null=True, on_delete=models.SET_NULL)
    performance_title = models.CharField(
        max_length=254, null=False, blank=False)
    performance_description = models.TextField(null=True, blank=True)
    composer = models.CharField(max_length=300, null=True, blank=True)
    video_url = models.URLField(max_length=1024, null=True, blank=True)
    category = models.ForeignKey(
        'Category', null=True, on_delete=models.SET_NULL)

    def get_performance_title(self):
        return self.performance_title

    def get_performance_description(self):
        return self.performance_description

    def get_composer(self):
        return self.composer


class Artist(models.Model):
    """ plural name to show in the admin """
    class Meta:
        verbose_name_plural = 'Artists'

    artist_name = models.CharField(max_length=254)
    artist_description = models.TextField(null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    category = models.ForeignKey(
        'Category', null=True, on_delete=models.SET_NULL)
    artist_type = models.ForeignKey(
        'ArtistType', null=True, on_delete=models.SET_NULL)
    artist_rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.pk

    def get_artist_name(self):
        return self.artist_name

    def get_artist_description(self):
        return self.artist_description


class Product(models.Model):
    """ plural name to show in the admin """
    class Meta:
        verbose_name_plural = 'Products'

    product_name = models.CharField(max_length=200)
    artist_id = models.ForeignKey(
        'Artist', on_delete=models.CASCADE, default="0")
    product_description = models.CharField(
        max_length=500, null=True, blank=True)
    price = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
