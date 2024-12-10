
from django.shortcuts import render, redirect
from .forms import JuegoForm
from .models import Juego, Apuesta
from django.shortcuts import render, get_object_or_404
from django.utils.text import slugify
import random
from .models import Equipo
from django.utils.text import slugify
from .forms import EquipoForm


def crear_juego(request):
    if request.method == 'POST':
        form = JuegoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_juegos')  # Redirigir a la lista de juegos
    else:
        form = JuegoForm()
    return render(request, 'crear_juego.html', {'form': form})




def apostar_juego(request, juego_id):
    juego = get_object_or_404(Juego, id=juego_id)
    if request.method == 'POST':
        equipo_seleccionado = request.POST.get('equipo')
        if equipo_seleccionado:
            ganador = random.choice([juego.equipo1, juego.equipo2])
            resultado = ganador.id == int(equipo_seleccionado)
            Apuesta.objects.create(
                usuario=request.user,
                juego=juego,
                equipo_apostado_id=equipo_seleccionado,
                resultado=resultado
            )
            imagen_ganador = f'imagenes_equipos/{slugify(ganador.nombre)}.png'
            return render(request, 'resultado_apuesta.html', {
                'juego': juego,
                'resultado': 'ganaste' if resultado else 'perdiste',
                'ganador': ganador,
                'imagen_ganador': imagen_ganador
            })
    return render(request, 'apostar_juego.html', {'juego': juego})


def lista_juegos(request):
    juegos = Juego.objects.all()
    juegos_sin_apostar = [
        juego for juego in juegos
        if not Apuesta.objects.filter(usuario=request.user, juego=juego).exists()
    ]
    juegos_con_imagenes = [
        {
            'equipo1': juego.equipo1,
            'equipo2': juego.equipo2,
            'imagen_equipo1': f'imagenes_equipos/{slugify(juego.equipo1.nombre)}.png',
            'imagen_equipo2': f'imagenes_equipos/{slugify(juego.equipo2.nombre)}.png',
            'id': juego.id
        }
        for juego in juegos_sin_apostar
    ]
    return render(request, 'lista_juegos.html', {'juegos': juegos_con_imagenes})


def crear_equipo(request):
    if request.method == 'POST':
        form = EquipoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_equipos')
    else:
        form = EquipoForm()
    return render(request, 'crear_equipo.html', {'form': form})

def lista_equipos(request):
    equipos = Equipo.objects.all()
    equipos_con_imagenes = [
        {
            'nombre': equipo.nombre,
            'pais': equipo.pais,
            'imagen': f'imagenes_equipos/{slugify(equipo.nombre)}.png'
        }
        for equipo in equipos
    ]
    return render(request, 'lista_equipos.html', {'equipos': equipos_con_imagenes})

def historial_apuestas(request):
    apuestas = Apuesta.objects.filter(usuario=request.user)
    return render(request, 'historial_apuestas.html', {'apuestas': apuestas})

