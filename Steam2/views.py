from django.shortcuts import render
from django.db.models import Q,F,Prefetch
from django.db.models import Avg,Max,Min
from .models import Usuario,Carrito,Biblioteca,Puntos,Distribuidora,Juego,Perfil,Tienda,Amigos,Coleccion,ColeccionBibliotecaJuego
from django.shortcuts import get_object_or_404, render

# Create your views here.
def index(request):
    return render(request, 'index.html') 

# Obtiene un perfil de usuario a partir del alias proporcionado y muestra la información relacionada.
def listar_perfil(request, alias):
    perfil = get_object_or_404(Perfil, alias=alias)  # Obtener el perfil por alias
    # Opcional: Obtener información del usuario relacionado
    usuario = perfil.usuario  # Acceder al usuario relacionado con el perfil
    return render(request, 'listar_perfil.html', {'perfil': perfil, 'usuario': usuario})

# Vista que lista todos los juegos disponibles en la tienda.
def listar_juegos(request):
    juegos = Juego.objects.all()  # Obtener todos los juegos
    return render(request, 'listar_juegos.html', {'juegos': juegos})  # Pasar los juegos al contexto

def listar_amigos(request, usuario_id):
    amigos = Amigos.objects.all()  # Obtener todos los juegos
    return render(request, 'listar_amigos.html', {'amigos': amigos}) 