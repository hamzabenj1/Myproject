from django.shortcuts import render, get_object_or_404
from store.models import Product
from category.models import Category
from carts.models import CartItem
from carts.views import _cart_id
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


def store(request, category_slug=None):
    if category_slug:
        categories = get_object_or_404(Category, category_name=category_slug)
        products = Product.objects.filter(is_available=True, category=categories)
        paginator = Paginator(products, 3)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
    else:
        products = Product.objects.filter(is_available=True)
        paginator = Paginator(products, 3)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)

    context = {'products': paged_products, 'product_count': products.count()}
    return render(request, 'store/store.html', context)


def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    in_cart = CartItem.objects.filter(cart__cart_id=_cart_id(request), product=product).exists()
    context = {'product': product, 'in_cart': in_cart}
    return render(request, 'store/product-detail.html', context)
