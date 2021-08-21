from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404
)
from django.contrib import messages

from products.models import Product


# Create your views here.
def view_cart(request):
    """ return cart contents page """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ add 1 of the specified product to the cart """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
        messages.success(request, f'Added "{product.name}" to your bag')
    else:
        cart[item_id] = quantity
        messages.success(request, f'Added "{product.name}" to your bag')

    request.session['cart'] = cart
    return redirect(redirect_url)


def adjust_cart(request, item_id):
    """ adjust quantity of specified product in cart to a specified amount from cart.html """

    product = Product.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] = quantity
        messages.success(request, f'Updated "{product.name}" quantity to [{item_id}]')
    else:
        cart[item_id] = quantity
        messages.success(request, f'Updated "{product.name}" quantity to [{item_id}]')


    request.session['cart'] = cart
    return redirect(reverse("view_cart"))


def remove(request, item_id):

    product = get_object_or_404(Product, pk=item_id)

    """ remove all of specified item from the cart """
    try:
        cart = request.session.get('cart', {})

        cart.pop(item_id)
        
        messages.info(request, f'Removed "{product.name}" from bag')

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)