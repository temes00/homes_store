from django.urls import path
from . import views

urlpatterns = [
	path('', views.root, name='root'),
	path('products/<str:slug>', views.products_item, name='products_item'),
	path('order/<str:product_slug>', views.order, name='order'),
	path('order/create/', views.order_create, name='order_create'),
]