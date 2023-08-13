from django.urls import path
from .views import home, products, about, detail, category_products, sale_create, sale_delete, sale_update

urlpatterns = [
    path('',home , name='home'),
    path('products/', products, name='products'),
    path('products/<pk>/', detail, name='detail'),
    path('product/<int:product_id>/delete/', sale_delete, name='sale_delete'),
    path('product/<int:product_id>/update/', sale_update, name='sale_update'),
    path('about/', about, name='about'),
    path('categories/<int:category_id>/',category_products , name='category_products'),
    path('create/', sale_create, name='create')
]