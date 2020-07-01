from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51H0CYOByJvwZPZN7qLo2qZkojnZdYptAeypbTG4Co2IIgfFQy78qA4O05RNZjzXGSgVmHbYU7Q5xXSTUug7JMtZc00smPM5N6w',
        'client_secret': 'test',
    }

    return render(request, template, context)
