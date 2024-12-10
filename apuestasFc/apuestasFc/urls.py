"""
URL configuration for apuestasFc project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include #agregar include
from django.views.generic.base import TemplateView #agregar ruta que permite 
#llamar por defecto la vsita de template y cargarlo 
# de manera directa en la ruta que uno quiera
#sin tener que pasarpor el archivo view

#importar index
from gestionUsuarios.views import index


urlpatterns = [
    path('admin/', admin.site.urls),
    #ruta en la que se va a poder ingresar a login log out register etc.
    #todas las urls de autenticacion 
    path('accounts/', include('django.contrib.auth.urls')),
    path('', index, name='home'),
    #otras formas de llamar
    path('usuarios/', include('gestionUsuarios.urls')),
    path('apuestas/', include('gestionApuestas.urls')),

]