def total_shopping_cart(request):
    total = 0
    if request.user.is_authenticated:
        for key, value in request.session['shopping_cart'].items():
            total = total+(float(value['price'])*value['quantity'])
    return {'total_shopping_cart': total}