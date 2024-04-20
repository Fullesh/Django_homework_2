from django.conf import settings
from django.core.cache import cache

from catalog.models import Product


def get_category_from_cache():
    if not settings.CACHE_ENABLED:
        return Product.objects.all()
    key = 'proudcts_list'
    product = cache.get(key)
    if product is not None:
        return product
    product = Product.objects.all()
    cache.set(key, product)
    return product