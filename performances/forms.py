""" forms for performances-app, used for admin av performances etc """
from django import forms
from .models import Product, Artist, Performance


class ProductForm(forms.ModelForm):
    """ form to get product and artist-names to form for product admin """
    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded'


class PerformanceForm(forms.ModelForm):
    """ form to get product and artist-names to form for product admin """
    class Meta:
        model = Performance
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded'


class ArtistForm(forms.ModelForm):
    """ form to get product and artist-names to form for product admin """
    class Meta:
        model = Artist
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded'
