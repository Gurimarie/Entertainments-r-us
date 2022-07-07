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
        'stripe_public_key': 'pk_test_51LIu9aCFXUpNVFsYi309aAwN2SKq9X0BujhSqDbQxkNYhAKeA7PljWYzaY9VvKoruVN70aNHD5lRKQMpfYeqeR3500zReOn6ao',
        'client_secret': 'test_client_secret',
    }

    return render(request, template, context)
