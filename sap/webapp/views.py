from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def bienvenido(request):
    return HttpResponse('Hola mundo desde Django')

def contacto(request):
    return HttpResponse('Email: kenetrha.74@gmail.com\n Telefono: 51296960')