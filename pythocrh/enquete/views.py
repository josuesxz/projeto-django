from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Ola mundo") #o que aparecerá no site deve ser refeeciado na urls
