from django.urls import path

from .views import index, product_detail, order_add

urlpatterns = [
    path('products/<slug:slug>/', product_detail, name='product_detail'),
    path('', index, name='index'),
    path('product/add/<int:product_id>', order_add, name='order_add'),

]
