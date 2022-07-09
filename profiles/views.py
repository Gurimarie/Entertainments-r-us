from django.shortcuts import render

def customer_profile(request):
    """ display the users profile """
    template = 'profiles/customer_profile.html'
    context = {}

    return render(request, template, context)
