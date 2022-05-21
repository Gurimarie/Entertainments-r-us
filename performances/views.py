""" views for performances-app """
from django.shortcuts import render, get_object_or_404
from .models import Performance, Artist, Product

# Create your views here.


def all_performances(request):
    """ A view to return the all_performances, incl. sorting and searching"""

    performances = Performance.objects.all()

    context = {
        'performances': performances,
    }

    return render(request, 'performances/performances.html', context)


def all_artists(request):
    """ A view to return the all_artists, incl. sorting and searching"""

    artists = Artist.objects.all()

    context = {
        'artists': artists,
    }

    return render(request, 'artists/artists.html', context)


def artist_page(request, pk):
    """ A view to return the chosen artists page """

    artist = get_object_or_404(Artist, pk=pk)
    artist_performances = Performance.objects.filter(artist_id=pk)

    context = {
        'artist': artist,
        'artist_performances': artist_performances,
    }

    return render(request, 'artists/artist_page.html', context)


def artist_products(request, pk):
    """ A view to return all products for chosen artist """

    artist = get_object_or_404(Artist, pk=pk)
    products = Product.objects.filter(artist_id=pk)

    context = {
        'artist': artist,
        'products': products,
    }

    return render(request, 'products/artist_products.html', context)
