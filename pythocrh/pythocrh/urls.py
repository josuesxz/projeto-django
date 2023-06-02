from django.contrib import admin
from django.urls import path
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('enquete/', include('enquete.urls')), #no final disso tudo é toda uma rota até o que aparecerá na tela
    path('admin/', admin.site.urls),
]
