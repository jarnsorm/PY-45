
from django.conf import settings
from django.http import HttpRequest

from showcase.models import Products

CART_SESSION_ID = 'cart'

class Cart(object):
    def __init__(self, request: HttpRequest):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product_id: int, quantity: int=1):
        product_id = str(product_id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0, 'price': str(Products.objects.get(pk=product_id).price)}
        self.cart[product_id]['quantity'] += quantity
        self.save()

    def remove(self, product_id: int):
        product_id = str(product_id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True

    def save(self):
        self.session.modified = True

    @property
    def total_quantity(self) -> int:
        return sum(item['quantity'] for item in self.cart.values())

    @property
    def total_price(self) -> float:
        return sum(
            Products.objects.get(pk=product_id).price * item['quantity']
            for product_id, item in self.cart.items()
        )

    @property
    def items(self) -> list:
        product_ids = self.cart.keys()
        products = Products.objects.filter(pk__in=product_ids)
        return [
            {'product': product, 'quantity': self.cart[str(product.pk)]['quantity']}
            for product in products
        ]
