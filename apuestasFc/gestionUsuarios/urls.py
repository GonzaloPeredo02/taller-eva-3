from django.urls import path
from . import views
from gestionUsuarios.views import SignUpView

urlpatterns = [
    #ruta para hacer la llamada al registro de usuarios
    path('signup/', SignUpView.as_view(),name='signup'),
    path('gestor_usuarios/', views.gestor_usuarios, name='gestor_usuarios'),
    path('perfil_usuarios/', views.perfil_usuario, name='perfil_usuarios'),
    #fijarse cuandos se llama a una clase se llama de distinta manera.
]
