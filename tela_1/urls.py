from django.urls import path
#from . import views
from tela_1.views import home, pag2

urlpatterns = [
    path('', home, name='home'),
    path('pag2/', pag2, name='pag2')
]