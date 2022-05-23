""" views for performances-app """
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Performance, Artist


# Create your views here.


def all_performances(request):
    """ A view to return the all_performances, incl. sorting and searching"""

    performances = Performance.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products/'))

            queries = Q(performance_title__icontains=query) | Q(performance_description__icontains=query)
            performances = performances.filter(queries)

    context = {
        'performances': performances,
        'search_term': query
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


def artist_details(request, pk):
    """ A view to return the chosen artists detail-page """

    artist = get_object_or_404(Artist, pk=pk)

    context = {
        'artist': artist,
    }

    return render(request, 'artists/artist_details.html', context)


def artist_products(request, pk):
    """ A view to return all products for chosen artist """

    artist = get_object_or_404(Artist, pk=pk)
    products = Product.objects.filter(artist_id=pk)

    context = {
        'artist': artist,
        'products': products,
    }

    return render(request, 'artists/artist_products.html', context)
