""" views for checkout-app """
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm


def checkout(request):
    """ get bag-content (or errormessage if empty) """
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(
            request, "There's nothing in your shoppingbag at the moment")
        return redirect(reverse('performances'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
    }

    return render(request, template, context)
