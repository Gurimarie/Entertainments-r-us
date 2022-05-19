""" views for products-app  """
from django.shortcuts import render
from .models import Product

# Create your views here.


def all_products(request):
    """ A view to return the all_products-page, + sorting and searching """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)
