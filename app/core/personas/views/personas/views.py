from django.shortcuts import render
from core.personas.models import Persona
from django.views.generic import ListView

class PersonaListView(ListView):
    model = Persona
    template_name = 'persona/list.html'

