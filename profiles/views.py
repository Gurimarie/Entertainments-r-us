from django.shortcuts import render, get_object_or_404

from .models import UserProfile


def customer_profile(request):
    """ display the users profile """
    customer_profile = get_object_or_404(UserProfile, user=request.user)
    template = 'profiles/customer_profile.html'
    context = {
        'customer_profile': customer_profile,
    }

    return render(request, template, context)
