from django.db import models


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    category_name = models.CharField(max_length=200)

    def __str__(self):
        return self.category_name


class ArtistType(models.Model):

    class Meta:
        verbose_name_plural = 'ArtistTypes'

    artist_type_name = models.CharField(max_length=200)

    def __str__(self):
        return self.artist_type_name


class Performance(models.Model):

    class Meta:
        verbose_name_plural = 'Performances'

    artist_id = models.ForeignKey('Artist', null=True, on_delete=models.SET_NULL)
    performance_title = models.CharField(max_length=254, null=False, blank=False)
    performance_description = models.TextField(null=True, blank=True)
    composer = models.CharField(max_length=300, null=True, blank=True)
    video_url = models.URLField(max_length=1024, null=True, blank=True)
    category = models.ForeignKey('Category', null=True, on_delete=models.SET_NULL)

    def performance_title(self):
        return self.performance_title

    def performance_description(self):
        return self.performance_description

    def composer(self):
        return self.composer


class Artist(models.Model):

    class Meta:
        verbose_name_plural = 'Artists'

    artist_name = models.CharField(max_length=254)
    artist_description = models.TextField(null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    category = models.ForeignKey('Category', null=True, on_delete=models.SET_NULL)
    artist_type = models.ForeignKey('ArtistType', null=True, on_delete=models.SET_NULL)

    def artist_name(self):
        return self.artist_name

    def artist_description(self):
        return self.artist_description
