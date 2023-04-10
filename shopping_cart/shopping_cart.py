class ShoppingCart:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        shopping_cart = self.session.get('shopping_cart')
        if not shopping_cart:
            shopping_cart = self.session['shopping_cart'] = {}
        else:
            self.shopping_cart = shopping_cart


    def add(self, product):
        product_id = str(product.id)
        if product_id not in self.shopping_cart.keys():
            self.shopping_cart[product_id] = {
                'product_id': product.id,
                'name': product.name,
                'price': str(product.price),
                'quantity': 1,
                'image': product.image.url
            }
        else:
            for key, value in self.shopping_cart.items():
                if key == product_id:
                    value['quantity'] = value['quantity'] + 1
                    break
        self.save()


    def save(self):
        self.session['shopping_cart'] = self.shopping_cart
        self.session.modified = True


    def remove(self, product):
        product.id = str(product.id)
        if product.id in self.shopping_cart:
            del self.shopping_cart[product_id]
            self.save()

    
    def decrement(self, product):
        product.id = str(product.id)
        if product.id in self.shopping_cart:
            for key, value in self.shopping_cart.items():
                if key == product.id:
                    value['quantity'] = value['quantity'] - 1
                    if value['quantity'] < 1:
                        self.remove(product)
                    break
            self.save()


    def clear(self):
        self.session['shopping_cart'] = {}
        self.session.modified = True