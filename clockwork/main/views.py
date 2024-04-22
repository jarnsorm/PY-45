from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from showcase.models import Categories


def index(request) -> HttpResponse:
    categories = Categories.objects.all()
    title = 'ClockWork'
    context = {
        'title': title,
        'categories': categories
    }
    return render(request, 'main/catalog.html', context)


class About(TemplateView):
    template_name = 'main/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'About Us'
        context['content'] = "The watch store 'ClockWork' website is an educational project by JarnSorm"
        return context


class Contact(TemplateView):
    template_name = 'main/contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Contact'
        context['content'] = {'ref': 'https://github.com/jarnsorm', 'kword': 'My GitHub profile'}
        return context


def cart(request) -> HttpResponse:
    return HttpResponse('Cart: Work In Progress')