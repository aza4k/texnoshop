from django.shortcuts import render
from .models import Product, Category

def home(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'texnoshop/home.html', context)

def products(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'texnoshop/products.html', context)

def category_products(request, category_id):
    category = Category.objects.get(id=category_id)
    products = Product.objects.filter(category=category)
    context = {
        'category': category,
        'products': products
    }
    return render(request, 'texnoshop/category.html', context)


def detail(request, pk):
    product = Product.objects.get(id=pk)
    context = {
        'product': product
    }
    return render(request, 'texnoshop/detail.html', context)

def about(request):
    return render(request, 'texnoshop/about.html')

def base(request):
    return render(request, 'texnoshop/base.html')
