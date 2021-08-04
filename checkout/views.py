from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, 'There is currently no items in your bag')
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51JKobYIGPHoH1QniNlPnhqpgPmxJr2BYs1nt4lxXIOcW1JBy8WRqdJlYeAt3tFZ9iXW2ux2OEBVQvmNBsH59QonG00Qb8OphmZ',
        'client_secret': 'test client secret'
    }

    return render(request, template, context)
