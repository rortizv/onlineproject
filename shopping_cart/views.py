from django.shortcuts import render, redirect
from .shopping_cart import ShoppingCart
from store.models import Product


def add_product(request, product_id):
    shopping_cart = ShoppingCart(request)
    product = Product.objects.get(id=product_id)
    shopping_cart.add(product=product)
    return redirect('Store')


def remove_product(request, product_id):
    shopping_cart = ShoppingCart(request)
    product = Product.objects.get(id=product_id)
    shopping_cart.remove(product=product)
    return redirect('Store')


def decrement_product(request, product_id):
    shopping_cart = ShoppingCart(request)
    product = Product.objects.get(id=product_id)
    shopping_cart.decrement(product=product)
    return redirect('Store')


def clear_cart(request):
    shopping_cart = ShoppingCart(request)
    shopping_cart.clear_cart()
    return redirect('Store')