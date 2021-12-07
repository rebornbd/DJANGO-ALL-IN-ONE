from django.urls import path
from . import views

urlpatterns = [
    path('', views.productList, name="product-list"),
    path('product/<id>', views.productView, name="product"),
]
