from django.urls import path
from . import views 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('crear_juego/', views.crear_juego, name='crear_juego'),
    path('crear_equipo/', views.crear_equipo, name='crear_equipo'),
    path('lista_juegos/', views.lista_juegos, name='lista_juegos'),
    path('apostar_juego/<int:juego_id>/', views.apostar_juego, name='apostar_juego'),
    path('lista_equipos/', views.lista_equipos, name='lista_equipos'),
    path('historial/', views.historial_apuestas, name='historial_apuestas'),
]




