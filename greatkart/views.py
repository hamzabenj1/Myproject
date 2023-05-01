from django.shortcuts import render
from store.models import Product


def home(request):
    context = {'products': Product.objects.all()}
    return render(request, 'home.html', context)
