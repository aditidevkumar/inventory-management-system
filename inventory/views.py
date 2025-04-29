from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductForm
from collections import defaultdict
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'inventory/product_form.html', {'form': form})

@login_required
def product_list(request):
    products = Product.objects.all()
    category_stock = defaultdict(int)
    for product in products:
        category_stock[product.category] += product.stock

    context = {
        'products': products,
        'category_stock': dict(category_stock),
    }
    return render(request, 'inventory/product_list.html', context)

def product_update(request, pk): 
    product = get_object_or_404(Product, pk=pk)

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect("product_list")  
    else:
        form = ProductForm(instance=product)

    products = Product.objects.all()
    category_stock = defaultdict(int)
    for prod in products:
        category_stock[prod.category] += prod.stock

    return render(request, "inventory/product_form.html", {
        "form": form,
        "category_stock": dict(category_stock),
    })

def category_stock(request):
    products = Product.objects.all()
    category_stock = defaultdict(int)

    for product in products:
        category_stock[product.category] += product.stock

    return JsonResponse({'category_stock': dict(category_stock)})

def decrease_stock(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if product.stock > 0:
        product.stock -= 1
        product.save()
        messages.success(request, f"Reduced stock of {product.name}. Remaining: {product.stock}")
    else:
        messages.warning(request, f"{product.name} is already out of stock!")
    return redirect('product_list')

def custom_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('product_list')  
        else:
            messages.error(request, "Invalid username or password")
    
    return render(request, "inventory/login.html")

def custom_logout(request):
    logout(request)  
    return redirect('login') 

def dashboard(request):
    products = Product.objects.all()
    return render(request, 'inventory/dashboard.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'inventory/product_detail.html', {'product': product})

