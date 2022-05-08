""" Docstring """
from django.shortcuts import render
from .models import Performance

# Create your views here.


def all_performances(request):
    """ A view to return the all_performances, incl. sorting and searching"""

    performances = Performance.objects.all()

    context = {
        'performances': performances,
    }
    
    return render(request, 'performances/performances.html', context)
