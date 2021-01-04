from django.shortcuts import render, redirect
from django.http import HttpResponse
# from personas.models import Persona

# Create your views here.
def index(request):
    return render(request, 'list.html', {})

#def tablas(request):
#   num_personas = Persona.objects.count()
#  personas = Persona.objects.order_by('id')

#    diccionario = {
 #       'num_personas': num_personas,
  #      'personas': personas
   # }

    #return render(request, 'tabla.html', diccionario)
 
def dashboard(request):
    return render(request, 'dashboard.html', {})
