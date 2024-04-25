from .models import Categories


def collection(request):
    collection = Categories.objects.all()
    return {'collection': collection}