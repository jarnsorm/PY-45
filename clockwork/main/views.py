from django.db.models import Q
from django.shortcuts import render
from showcase.models import Products


def search_view(request):
    query = request.GET.get('q')
    results = Products.objects.filter(
        Q(name__icontains=query) |
        Q(description__icontains=query) |
        Q(brand__name__icontains=query) |
        Q(category__name__icontains=query)
    )

    context = {'title': f'You searched for: {query}'}
    if not results:
        context['message'] = "Sorry, but we didn't find anything matching your request, please try again"
    else:
        context['results'] = results

    return render(request, 'main/search.html', context)

