from django.urls import path
from .views import home, products, about, detail, category_products

urlpatterns = [
    path('',home , name='home'),
    path('products/', products, name='products'),
    path('products/<pk>/', detail, name='detail'),
    path('about/', about, name='about'),
    path('categories/<int:category_id>/',category_products , name='category_products'),
]