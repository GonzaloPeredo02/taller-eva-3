from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from rest_framework.reverse import reverse_lazy
from django.views.generic import CreateView
# importar SuccessMessageMixin para mandar mensajes desde la vista
from django.contrib.messages.views import SuccessMessageMixin
#importar decorador para que para que solicite logearse
from django.contrib.auth.decorators import login_required


# Create your views here.
#IMPORTANTE esto puede ayudar en nuestro proyecto 
#cuando quiera apostar solicite obligatoriamente estar logeado
#osea que cuano quiera apostar y dirigirse a la pagina de apuestas requiera logearse
def index(request): #ir al path y cambiar a index 
    return render(request,'index.html')



#crear clase, metodo o funciones
#dar argumento antes se usaba request. ahora create view
class SignUpView(SuccessMessageMixin,CreateView): #se esta extendiendo de create view COLOCAR SUCCESS ANTES O NO FUCNIONA
    form_class = UserCreationForm #se utiliza por def la plantilla que registra los user
    success_url = reverse_lazy('login') #nos redirige a la pag login
    template_name = 'registration/signup.html'   
    success_message = '¡usuario registrado correctamente!' #configurar en login
    #la mayoria de estos metodo vienen por defectos como se ven en las importaciones

def gestor_usuarios(request):
    return render(request, 'gestorUser/gestorUsuarios.html')

def perfil_usuario(request):
    return render(request, 'gestorUser/perfil.html')