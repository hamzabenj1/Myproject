from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name="store"),
    path('<slug:category_slug>/', views.store, name="products_by_category"),
    path('product/<product_id>/', views.product_detail, name="product_detail"),
]
