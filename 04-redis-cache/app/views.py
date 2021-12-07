from django.shortcuts import render, redirect
from django.core.cache import cache
from .models import Product


def productList(request):
  if cache.get('products'):
    products = cache.get('products')
    print("data from: CACHE")
  else:
    products = Product.objects.all()
    cache.set('products', products, timeout=120)
    print("data from: DB")
  return render(request, 'app/list.html', context={'products': products})


def productView(request, id):
  if cache.get(id):
    product = cache.get(id)
    print("data from: CACHE")
  else:
    try:
      product = Product.objects.get(pk=id)
      cache.set(id, product, timeout=120)
      print("data from: DB")
    except Product.DoesNotExist:
      return redirect("/")
  return render(request, 'app/product.html', context={'product': product})
