""" forms for performances-app, used for admin av performances etc """
from django import forms
from .models import Product, Artist, Performance, Category, ArtistType


class ProductForm(forms.ModelForm):
    """ form to get product and artist-names to form for product admin """
    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        artists = Artist.objects.all()

        self.fields['artist'].choices = artists
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded'


class PerformancesForm(forms.ModelForm):
    """ form to get product and artist-names to form for product admin """
    class Meta:
        model = Performance
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        artists = Artist.objects.all()
        categories = Category.objects.all()
        artisttypes = ArtistType.objects.all()

        self.fields['artist'].choices = artists
        self.fields['category'].choices = categories
        self.fields['artisttype'].choices = artisttypes
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded'


class ArtistForm(forms.ModelForm):
    """ form to get product and artist-names to form for product admin """
    class Meta:
        model = Artist
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        artisttypes = ArtistType.objects.all()

        self.fields['category'].choices = categories
        self.fields['artisttype'].choices = artisttypes

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded'
