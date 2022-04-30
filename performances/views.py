""" Docstring """
from django.shortcuts import render
from .models import Performances

# Create your views here.


def all_performances(request):
    """ A view to return the all_performances, including sorting and searching """

    performances = Performances.objects.all()

    context = {
        'performances': performances,
    }
    
    return render(request, 'performances/performances.html', context)
