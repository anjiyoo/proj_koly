from django.urls import path
from . import views

app_name = 'seller'

urlpatterns = [
    path('/', views.seller_index, name='products_index'),
    path('add_products/', views.add_products, name='add_products'),  # 상품 등록 url
    path('products_detail/<int:pk>/', views.products_detail, name='products_detail'),  # 상품 상세 url
    path('delete_products/<int:pk>/', views.delete_products, name='delete_products'),  # 상품 삭제 url
]
