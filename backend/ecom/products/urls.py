from django.urls import path
from .views import ProductDetailView,ProductListView

urlpatterns = [
    path('product/list/',ProductListView.as_view()),
    path('product/details/<pk>/',ProductDetailView)
]
