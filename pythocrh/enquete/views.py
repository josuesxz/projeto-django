from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1><u>Ola mundo</u></h1>") #o que aparecerá no site deve ser refeeciado na urls
