from django.urls import path
from . import views

app_name = 'shopping_cart'


urlpatterns = [
    path('add/<int:product_id>/', views.add_product, name='add'),
    path('remove/<int:product_id>/', views.remove_product, name='remove'),
    path('decrement/<int:product_id>/', views.decrement_product, name='decrement'),
    path('clear/', views.clear_cart, name='clear'),
]