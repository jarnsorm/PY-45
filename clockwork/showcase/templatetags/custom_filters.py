from django import template
from showcase.models import Products

register = template.Library()


@register.filter
def get_product_from_slug(product_slug):
    try:
        return Products.objects.get(slug=product_slug)
    except Products.DoesNotExist:
        return None