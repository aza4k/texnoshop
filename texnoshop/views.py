from django.shortcuts import render, redirect
from .models import Product, Category
from .forms import ProductForm, ProductUpdateForm

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


def sale_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('products')
    else:
        form = ProductForm()
    
    context = {
        'form': form
    }
    return render(request, 'texnoshop/create.html', context)

def sale_delete(request, product_id):
    product = Product.objects.get(id=product_id)

    if request.method == 'POST':
        product.delete()
        return redirect('products')  # Redirect to the list of products

    context = {
        'product': product
    }
    return render(request, 'texnoshop/sale_delete.html', context)


def sale_update(request, product_id):
    product = Product.objects.get(id=product_id)

    if request.method == 'POST':
        form = ProductUpdateForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('products')
    else:
        form = ProductUpdateForm(instance=product)

    context = {
        'form': form,
        'product': product
    }
    return render(request, 'texnoshop/sale_update.html', context)
