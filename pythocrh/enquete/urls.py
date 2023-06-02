from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index, name='index') #lista que detalha o caminho e atrela uma url a esse caminho 
]