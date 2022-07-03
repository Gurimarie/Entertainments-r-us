""" Views for shoppingbag-app, from Project Ado, Code Institute... """

from django.shortcuts import render, redirect


def view_shoppingbag(request):
    """ A view to return the shoppingbag-page """

    return render(request, 'shoppingbag/shoppingbag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')

    """ Get bag-variable if it exists, or create it if it doesn't """
    bag = request.session.get('bag', {})

    """ Add item to bag, or update quantity if its already there """
    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    """ over-write the session-bag with new, updated version"""
    request.session['bag'] = bag
    return redirect(redirect_url)
