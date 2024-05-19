from showcase.models import Products, Brands
from django.views.generic import ListView, DetailView, TemplateView


class Catalog(ListView):
    model = Products
    template_name = 'showcase/catalog.html'
    context_object_name = 'goods'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.order_by('?')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'ClockWork'
        context['col_selected'] = 0
        context['brands'] = Brands.objects.all()
        return context


class Collection(ListView):
    model = Products
    template_name = 'showcase/catalog.html'
    context_object_name = 'goods'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = str(f"{context['goods'][0].brand} {context['goods'][0].category}")
        context['col_selected'] = context['goods'][0].category
        context['brands'] = Brands.objects.all()
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
        context['brand_selected'] = context['goods'][0].brand
        context['brands'] = Brands.objects.all()
        return context

    def get_queryset(self):
        return Products.objects.filter(brand__slug=self.kwargs['brand_slug'])


class Product(DetailView):
    model = Products
    template_name = 'showcase/product.html'
    slug_url_kwarg = 'p_slug'
    context_object_name = 'product'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f"{context['product'].brand} {context['product'].name}"
        context['brands'] = Brands.objects.all()
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
        return super().get(request, *args, **kwargs)


class About(TemplateView):
    template_name = 'showcase/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'About Us'
        context['content'] = "The watch store 'ClockWork' website is an educational project by JarnSorm"
        return context


class Contact(TemplateView):
    template_name = 'showcase/contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Contact'
        context['content'] = {'ref': 'https://github.com/jarnsorm', 'kword': 'My GitHub accounts'}
        return context
