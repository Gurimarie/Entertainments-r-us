""" views for performances-app """
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Performance, Artist, Category, ArtistType, Product
from .forms import ArtistForm, ProductForm, PerformanceForm


def all_performances(request):
    """ A view to return the all_performances, incl. sorting and searching"""

    performances = Performance.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sort_key = request.GET['sort']
            sort = sort_key
            if sort_key == 'name':  # performance_title instead of name?
                sort_key = 'lower_name'
                performances = performances.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sort_key = f'-{sort_key}'
            performances = performances.order_by(sort_key)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            performances = performances.filter(
                                category__category_name__in=categories)
            categories = Category.objects.filter(category_name__in=categories)

        # The search-function will search titles and desriptions of
        # performances for match by using complex lookups with Q objects
        # (https://docs.djangoproject.com/en/3.2/topics/db/queries/)
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                        request, "You didn't enter any search criteria! \
                        Redirect to all performances.")
                return redirect(reverse('performances'))

            queries = Q(performance_title__icontains=query) | Q(
                        performance_description__icontains=query)
            performances = performances.filter(queries)

    # Return current_sorting to the template
    current_sorting = f'{sort}_{direction}'

    context = {
        'performances': performances,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'performances/performances.html', context)


def all_artists(request):
    """ A view to return the all_artists, incl. sorting and searching"""

    artists = Artist.objects.all()

    sort = None
    direction = None
    artist_types = None

    if request.GET:
        if 'sort' in request.GET:
            sort_key = request.GET['sort']
            sort = sort_key
            if sort_key == 'name':  # artist_name instead of just name?
                sort_key = 'lower_name'
                artists = artists.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sort_key = f'-{sort_key}'
            artists = artists.order_by(sort_key)

        if 'artist_type' in request.GET:
            artist_types = request.GET['artist_type'].split(',')
            artists = artists.filter(
                artist_type__artist_type_name__in=artist_types)
            artist_types = ArtistType.objects.filter(
                artist_type_name__in=artist_types)

    current_sorting = f'{sort}_{direction}'

    context = {
        'artists': artists,
        'current_sorting': current_sorting,
        'current_artist_types': artist_types,
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


@login_required
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
    artists_products = Product.objects.filter(artist_id=pk)

    context = {
        'artist': artist,
        'artists_products': artists_products,
    }

    return render(request, 'artists/artist_products.html', context)


@login_required
def artist_product_details(request, pk):
    """ A view to return details for specific product for the chosen artist """

    product = get_object_or_404(Product, pk=pk)

    context = {
        'product': product,
    }

    return render(request, 'artists/artist_product_details.html', context)


# Product Management - ADD


@login_required
def add_artist_product(request):
    """ add a product to the store """
    if not request.user.is_staff:
        messages.error(request, 'Sorry, only the artist can access this.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'You successfully added a product!')
            return redirect(reverse('add_artist_product'))
        else:
            messages.error(request, 'Failed to add performance. \
                           Please ensure the form is valid.')
    else:
        form = ProductForm()

    template = 'artists/add_artist_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def add_performance(request):
    """ add a product to the store """
    if not request.user.is_staff:
        messages.error(request, 'Sorry, only the artist can access this.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = PerformanceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'You successfully added a performance!')
            return redirect(reverse('add_performance'))
        else:
            messages.error(request, 'Failed to add performance. \
                           Please ensure the form is valid.')
    else:
        form = PerformanceForm()

    template = 'performances/add_performance.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def add_artist(request):
    """ add a product to the store """
    if not request.user.is_staff:
        messages.error(request, 'Sorry, only the artist can access this.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ArtistForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'You successfully added a performance!')
            return redirect(reverse('add_performance'))
        else:
            messages.error(request, 'Failed to add performance. \
                           Please ensure the form is valid.')
    else:
        form = ArtistForm()

    template = 'artists/add_artist.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


# Product Management - EDIT


@login_required
def edit_artist_product(request, pk):
    """ edit a product in the store """
    if not request.user.is_staff:
        messages.error(request, 'Sorry, only the artist can access this.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('artist_product_details', args=[pk]))
        else:
            messages.error(request, 'Failed to update product. \
                           Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.product_name}')

    template = 'artists/edit_artist_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def edit_performance(request, pk):
    """ edit a performance in the store """
    if not request.user.is_staff:
        messages.error(request, 'Sorry, only the artist can access this.')
        return redirect(reverse('home'))

    performance = get_object_or_404(Performance, pk=pk)
    if request.method == 'POST':
        form = PerformanceForm(
            request.POST, request.FILES, instance=performance)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated performance!')
            return redirect(reverse('performances'))
        else:
            messages.error(request, 'Failed to update performance. \
                           Please ensure the form is valid.')
    else:
        form = PerformanceForm(instance=performance)
        messages.info(
            request, f'You are editing {performance.performance_title}')

    template = 'performances/edit_performance.html'
    context = {
        'form': form,
        'performance': performance,
    }

    return render(request, template, context)


@login_required
def edit_artist(request, pk):
    """ edit an artist in the store """
    if not request.user.is_staff:
        messages.error(request, 'Sorry, only the artist can access this.')
        return redirect(reverse('home'))

    artist = get_object_or_404(Artist, pk=pk)
    if request.method == 'POST':
        form = ArtistForm(request.POST, request.FILES, instance=artist)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated artist!')
            return redirect(reverse('artist_details', args=[pk]))
        else:
            messages.error(request, 'Failed to update artist. \
                           Please ensure the form is valid.')
    else:
        form = ArtistForm(instance=artist)
        messages.info(request, f'You are editing {artist.artist_name}')

    template = 'artists/edit_artist.html'
    context = {
        'form': form,
        'artist': artist,
    }

    return render(request, template, context)


# Product Management - DELETE


@login_required
def delete_artist_product(request, pk):
    """ edit a product in the store """
    if not request.user.is_staff:
        messages.error(request, 'Sorry, only the artist can access this.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=pk)
    product.delete()
    messages.success(request, 'Product deleted.')
    return redirect(reverse('artists'))


@login_required
def delete_performance(request, pk):
    """ edit a performance in the store """
    if not request.user.is_staff:
        messages.error(request, 'Sorry, only the artist can access this.')
        return redirect(reverse('home'))

    performance = get_object_or_404(Performance, pk=pk)
    performance.delete()
    messages.success(request, 'Performance deleted.')
    return redirect(reverse('performances'))


@login_required
def delete_artist(request, pk):
    """ edit an artist in the store """
    if not request.user.is_staff:
        messages.error(request, 'Sorry, only the artist can access this.')
        return redirect(reverse('home'))

    artist = get_object_or_404(Artist, pk=pk)
    artist.delete()
    messages.success(request, 'Artist deleted.')
    return redirect(reverse('artists'))
