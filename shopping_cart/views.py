from django.shortcuts import render, redirect
from .shopping_cart import ShoppingCart
from store.models import Product


def add_product(request, product_id):
    shopping_cart = ShoppingCart(request)
    product = Product.objects.get(id=product_id)
    shopping_cart.add(product)
    return redirect('store')


def remove_product(request, product_id):
    shopping_cart = ShoppingCart(request)
    product = Product.objects.get(id=product_id)
    shopping_cart.remove(product)
    return redirect('store')


def decrement_product(request, product_id):
    shopping_cart = ShoppingCart(request)
    product = Product.objects.get(id=product_id)
    shopping_cart.decrement(product)
    return redirect('store')


def clear_cart(request):
    shopping_cart = ShoppingCart(request)
    shopping_cart.clear()
    return redirect('store')