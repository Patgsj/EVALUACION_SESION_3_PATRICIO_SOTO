from django.shortcuts import render
from django.http import HttpResponse
from .models import Persona  # Asegúrate de importar el modelo


def index(request):
    return HttpResponse("¡Bienvenido a la página principal de Evaluación Sesión 3!")


def about(request):
    return HttpResponse("Esta es la página About de mi proyecto.")


def lista_personas(request):
    personas = Persona.objects.all()
    return render(request, 'app_django/lista_personas.html', {'personas': personas})




# Create your views here.
