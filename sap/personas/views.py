from django.shortcuts import render, get_object_or_404, redirect
from django.forms import modelform_factory
from personas.models import Persona
from personas.forms import PersonaForm
# Create your views here.

def detallePersona(request, id):
    persona = get_object_or_404(Persona, pk=id)
    return render(request, 'personas/detalle.html', {'persona': persona})

def nuevaPersona(request):
    if request.method == 'POST':
       formaPersona = PersonaForm(request.POST)
       if formaPersona.is_valid():
           formaPersona.save() 
           return redirect('index')
    else:
        formaPersona = PersonaForm()

    return render(request, 'personas/nuevo.html', {'formaPersona': formaPersona})

def editarPersona(request, id):
    persona = get_object_or_404(Persona, pk=id)
    return render(request, 'personas/detalle.html', {'persona', persona})