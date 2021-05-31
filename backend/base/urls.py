from django.urls import path
from . import views

urlpatterns = [
    path('api/products/', views.getProduct, name="products"),
    path('api/products/<str:pk>/', views.product, name="product")
]
