from django.http import HttpResponse
from django.shortcuts import render

from showcase.models import Categories


def index(request) -> HttpResponse:
    categories = Categories.objects.all()
    title = 'ClockWork'
    context = {
        'title': title,
        'categories': categories
    }
    return render(request, 'main/index.html', context)


def about_us(request) -> HttpResponse:
    info = "The watch store 'ClockWork' website is an educational project by JarnSorm"
    return HttpResponse(info)


def contact_us(request) -> HttpResponse:
    contact = '<a href="https://github.com/jarnsorm">My GitHub profile</a>'
    return HttpResponse(contact)


def cart(request) -> HttpResponse:
    return HttpResponse('Cart')