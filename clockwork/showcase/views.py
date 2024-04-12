from django.http import HttpResponse
from django.shortcuts import render
from showcase.models import Products, Categories


def catalog(request) -> HttpResponse:
    selected_category = request.GET.get('category', 'ALL')
    selected_brand = request.GET.get('brand')

    if selected_category == 'ALL':
        goods = Products.objects.all().order_by('?')
        title = 'All products'
    else:
        goods = Products.objects.filter(category__name=selected_category).order_by('?')
        title = selected_category

    if selected_brand is not None:
        goods = Products.objects.filter(brand=selected_brand).order_by('?')
        title = selected_brand

    categories = Categories.objects.all()

    context = {
        "title": title,
        "goods": goods,
        "categories": categories,
        "selected_category": selected_category

    }
    return render(request, "showcase/catalog.html", context)


def product(request) -> HttpResponse:
    selected_product = request.GET.get('name')

    item = Products.objects.get(name=selected_product)
    title = f'{item.brand} {item.name}'

    context = {
        "title": title,
        "product": item,

    }
    return render(request, "showcase/product.html", context)