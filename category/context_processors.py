from .models import Category


def menu_links(request):
    return dict(links=Category.objects.all())
