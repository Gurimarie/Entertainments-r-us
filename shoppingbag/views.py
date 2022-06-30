from django.shortcuts import render

def view_shoppingbag(request):
    """ A view to return the shoppingbag-page """

    return render(request, 'shoppingbag/shoppingbag.html')
