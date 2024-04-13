from django.http import HttpResponse
from django.shortcuts import render
from showcase.models import Products, Categories


def catalog(request) -> HttpResponse:
    selected_category = request.GET.get('category', 'ALL')
    selected_brand = request.GET.get('brand')
    if request.GET.get('order_by') is None:
        selected_sorting = 'Random'
    else:
        selected_sorting = request.GET.get('order_by')

    sorting_list = {
        'Random': '?',
        'Asc Price': 'price',
        'Dec Price': '-price',
        'Name': 'name',
        'Brand': 'brand'
    }

    if selected_category == 'ALL':
        goods = Products.objects.all().order_by(sorting_list[selected_sorting])
        title = 'All products'
    else:
        goods = Products.objects.filter(category__name=selected_category).order_by(sorting_list[selected_sorting])
        title = selected_category

    if selected_brand is not None:
        goods = Products.objects.filter(brand=selected_brand).order_by(sorting_list[selected_sorting])
        title = selected_brand

    categories = Categories.objects.all()

    context = {
        "title": title,
        "goods": goods,
        "categories": categories,
        "selected_category": selected_category,
        "sorting_list": sorting_list,
        "order_by": selected_sorting

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