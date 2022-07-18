from django.urls import path
from . import views # views are controllers in express

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
     # route for cats index
    path('cats/', views.cats_index, name='index')
]