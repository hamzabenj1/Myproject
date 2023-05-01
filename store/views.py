from django.shortcuts import render, get_object_or_404
from store.models import Product
from category.models import Category


def store(request, category_slug=None):
    if category_slug:
        categories = get_object_or_404(Category, category_name=category_slug)
        products = Product.objects.filter(is_available=True, category=categories)
    else:
        products = Product.objects.filter(is_available=True)

    context = {'products': products, 'product_count': products.count()}
    return render(request, 'store/store.html', context)


def product_detail(request, product_id):
    context = {'product': Product.objects.get(id=product_id)}
    return render(request, 'store/product-detail.html', context)
