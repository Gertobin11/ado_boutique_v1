from django.shortcuts import render


def view_bag(request):
    # A view that returns the shopping bag page
    return render(request, "bag/bag.html")
