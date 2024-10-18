# To handle views and redirects
from django.shortcuts import render, redirect, get_object_or_404
# To Import auth functions from Django
from django.contrib.auth import authenticate, login, logout
# The login_required decorator to protect views
from django.contrib.auth.decorators import login_required
# For class-based views [CBV]
from django.contrib.auth.mixins import LoginRequiredMixin
# For class-based views [CBV]
from django.views import View
# Import the User class (model)
from django.contrib.auth.models import User
# Import the RegisterForm from forms.py
from .forms import RegisterForm
from .models import AmbitoProyecto
from .forms import AmbitoProyectoForm
from django.contrib import messages
# from .models import Proyecto  # Asumiendo que el modelo del proyecto es 'Proyecto'


# Create your views here.
def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = User.objects.create_user(username=username, password=password)
            login(request,user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form':form})


def login_view(request):
    error_message = None
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            next_url = request.POST.get('next') or request.GET.get('next') or 'home'
            return redirect(next_url)
        else:
            error_message = "Invalid credentials"
    return render(request, 'accounts/login.html', {'error': error_message})


def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect('login')
    else:
        return redirect('home')
    
# Home View
# Using the decorator
@login_required
def home_view(request):
    return render(request, 'home/home.html')

# Protected View
class ProtectedView(LoginRequiredMixin, View):
    login_url = '/login/'
    # 'next' - to redirect URL
    redirect_field_name = 'redirect_to'

    def get(self, request):
        return render(request, 'registration/protected.html')

@login_required
def definir_ambito_proyecto(request):
    try:
        ambito_proyecto = AmbitoProyecto.objects.get(id=1)
    except AmbitoProyecto.DoesNotExist:
        ambito_proyecto = None

    if request.method == 'POST':
        form = AmbitoProyectoForm(request.POST, instance=ambito_proyecto)
        if form.is_valid():
            form.save()
            return redirect('ver_ambito_proyecto')
        else:
            return render(request, 'definir_ambito.html', {'form': form})
    else:
        form = AmbitoProyectoForm(instance=ambito_proyecto)

    return render(request, 'accounts/definir_ambito.html', {'form': form})

@login_required
def ver_ambito_proyecto(request):
    try:
        ambito_proyecto = AmbitoProyecto.objects.get(id=1)
    except AmbitoProyecto.DoesNotExist:
        ambito_proyecto = None

    return render(request, 'accounts/ver_ambito.html', {'ambito_proyecto': ambito_proyecto})

'''
# Para cuando esté el proyecto a eliminar
@login_required
def eliminar_proyecto(request, proyecto_id):
    proyecto = get_object_or_404(Proyecto, id=proyecto_id)

    if request.method == 'POST':
        proyecto.delete()
        messages.success(request, "El proyecto ha sido eliminado exitosamente.")
        return redirect('lista_proyectos')  # Redirigir a una lista de proyectos u otra página

    return render(request, 'accounts/eliminar_proyecto.html', {'proyecto': proyecto})
'''
