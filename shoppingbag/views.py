""" Views for shoppingbag-app, from Project Ado, Code Institute... """

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from performances.models import Product


def view_shoppingbag(request):
    """ A view to return the shoppingbag-page """
    return render(request, 'shoppingbag/shoppingbag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})  # Get (or create) bag-variable
    if item_id in list(bag.keys()):
        bag[item_id] += quantity    # Add additional item to bag
        messages.success(
            request, f'Added another {product.product_name}, {product.artist_id} to your bag')
    else:
        bag[item_id] = quantity     # Add item to bag
        messages.success(
            request, f'Added {product.product_name}, {product.artist_id} to your bag')

    request.session['bag'] = bag   # Over-write session-bag with updated bag
    return redirect(redirect_url)


def remove_from_bag(request, item_id):
    """ Remove items from shoppingbag """

    product = get_object_or_404(Product, pk=item_id)
    bag = request.session.get('bag', {})  # Get bag-variable
    if item_id in list(bag.keys()):
        bag.pop(item_id)                # Remove item from bag-list
        messages.success(
            request, f'Removed {product.product_name}, {product.artist_id} from your bag')

    request.session['bag'] = bag    # Over-write session-bag with updated bag
    return redirect('view_shoppingbag')
