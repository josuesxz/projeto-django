from django.shortcuts import render

def home(request):
    return (render(request, 'index.html'))

def pag2(request):
    return (render(request, 'pag2.html')) #links das rotas
