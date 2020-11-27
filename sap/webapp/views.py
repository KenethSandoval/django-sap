from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def bienvenido(request):
    mensajes = {
        'msg1': 'Valor mensaje 1'
    }
    return render(request, 'bienvenida.html', mensajes)

def contacto(request):
    return HttpResponse('Email: kenetrha.74@gmail.com\n Telefono: 51296960')