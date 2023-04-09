from django.urls import path
from . import views

urlpatterns = [
    path('', views.posts, name='Blog'),
    path('category/<int:category_id>/', views.category, name='category'),
]