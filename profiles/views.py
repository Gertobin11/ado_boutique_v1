from django.shortcuts import render


def profile(request):
    # A view to return the users profile page
    template = "profiles/profile.html"
    context = {}

    return render(request, template, context)
