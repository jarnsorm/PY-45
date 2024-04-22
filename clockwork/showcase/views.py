from django.shortcuts import render

from showcase.models import Products, Categories
from django.views.generic import ListView, DetailView, TemplateView

menu = [
    {'title': 'About Us', 'url_name': 'showcase:about'},
    {'title': 'Contact', 'url_name': 'showcase:contact'},
    # {'title': 'Cart', 'url_name': 'cart:cart'},
    {'title': 'DEV', 'url_name': 'admin:index'},
    # {'title': 'My Account', 'url_name': 'login'},
]

categories = Categories.objects.all()

class Catalog(ListView):
    model = Products
    template_name = 'showcase/catalog.html'
    context_object_name = 'goods'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'ClockWork'
        context['menu'] = menu
        context['collection'] = categories
        context['col_selected'] = 0
        return context


class Collection(ListView):
    model = Products
    template_name = 'showcase/catalog.html'
    context_object_name = 'goods'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = str(f"{context['goods'][0].brand} {context['goods'][0].category}")
        context['menu'] = menu
        context['collection'] = categories
        context['col_selected'] = context['goods'][0].category
        return context

    def get_queryset(self):
        return Products.objects.filter(category__slug=self.kwargs['col_slug'])


class Brand(ListView):
    model = Products
    template_name = 'showcase/catalog.html'
    context_object_name = 'goods'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = str(context['goods'][0].brand)
        context['menu'] = menu
        context['collection'] = categories
        context['brand_selected'] = context['goods'][0].brand
        return context

    def get_queryset(self):
        return Products.objects.filter(brand=self.kwargs['brand'])


class Product(DetailView):
    model = Products
    template_name = 'showcase/product.html'
    slug_url_kwarg = 'p_slug'
    context_object_name = 'product'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f"{context['product'].brand} {context['product'].name}"
        context['menu'] = menu
        context['collection'] = categories
        return context

    def get_queryset(self):
        return Products.objects.filter(slug=self.kwargs['p_slug'])

    def get(self, request, *args, **kwargs):
        product_slug = kwargs.get('p_slug')
        viewed_products = request.session.get('viewed_products', [])
        if product_slug not in viewed_products:
            viewed_products.append(product_slug)
        viewed_products = viewed_products[-3:]
        request.session['viewed_products'] = viewed_products
        print(product_slug)
        return super().get(request, *args, **kwargs)


class About(TemplateView):
    template_name = 'showcase/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'About Us'
        context['menu'] = menu[1:]
        context['collection'] = categories
        context['content'] = "The watch store 'ClockWork' website is an educational project by JarnSorm"
        return context


class Contact(TemplateView):
    template_name = 'showcase/contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Contact'
        context['menu'] = menu
        context['collection'] = categories
        context['content'] = {'ref': 'https://github.com/jarnsorm', 'kword': 'My GitHub profile'}
        return context
