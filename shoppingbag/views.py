""" Views for shoppingbag-app, from Project Ado, Code Institute... """

from django.shortcuts import render, redirect


def view_shoppingbag(request):
    """ A view to return the shoppingbag-page """
    return render(request, 'shoppingbag/shoppingbag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})  # Get (or create) bag-variable
    if item_id in list(bag.keys()):
        bag[item_id] += quantity    # Add additional item to bag
    else:
        bag[item_id] = quantity     # Add item to bag

    request.session['bag'] = bag   # Over-write session-bag with updated bag
    return redirect(redirect_url)


def remove_from_bag(request, item_id):
    """ Remove items from shoppingbag """
    bag = request.session.get('bag', {})  # Get bag-variable
    if item_id in list(bag.keys()):
        bag.pop(item_id)                # Remove item from bag-list

    request.session['bag'] = bag    # Over-write session-bag with updated bag
    return redirect('view_shoppingbag')
