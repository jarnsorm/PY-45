from django.http import JsonResponse
from django.template.loader import render_to_string
from django.urls import reverse
from django.shortcuts import redirect
from django.views import View
from django.views.generic import TemplateView

from showcase.models import Products
from .forms import CartAddProductForm


class CartAddAjaxView(View):
    def post(self, request):
        form = CartAddProductForm(request.POST)
        if form.is_valid():
            product_id = form.cleaned_data['product_id']
            quantity = form.cleaned_data['quantity']
            update = form.cleaned_data['update']
            # product = Products.objects.get(pk=product_id)
            cart = request.session.get('cart', {})
            if str(product_id) in cart:
                if update:
                    cart[str(product_id)]['quantity'] = quantity
                else:
                    cart[str(product_id)]['quantity'] += quantity
            else:
                cart[str(product_id)] = {'quantity': quantity}
            request.session['cart'] = cart
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False})


class CartRemoveView(View):
    def post(self, request, product_id):
        cart = request.session.get('cart', {})
        if str(product_id) in cart:
            if cart[str(product_id)]['quantity'] > 1:
                cart[str(product_id)]['quantity'] -= 1
            else:
                del cart[str(product_id)]
            request.session['cart'] = cart
        return redirect(reverse('cart:cart_detail'))


class CartDetailView(TemplateView):
    template_name = 'cart/cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart = self.request.session.get('cart', {})
        cart_items = []
        total_price = 0
        for product_id, item in cart.items():
            product = Products.objects.get(pk=int(product_id))
            item_total = product.price * item['quantity']
            total_price += item_total
            cart_items.append({
                'product': product,
                'quantity': item['quantity'],
                'item_total': item_total
            })
        context['title'] = 'Your Cart'
        context['cart_items'] = cart_items
        context['total_price'] = total_price
        return context

def update_cart(request):
    cart = request.session.get('cart', {})  # Ваши данные о корзине
    context = {'cart': cart}
    cart_html = render_to_string('cart/cart.html', context)
    return JsonResponse({'cart_html': cart_html})