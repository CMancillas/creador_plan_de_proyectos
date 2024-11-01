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
from .forms import RegisterForm, AmbitoProyectoForm, ProjectPlanForm, TaskForm, RestriccionForm
from .models import AmbitoProyecto, Task, ProjectPlan
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

@login_required
def define_project_plan(request, project_id=None):
    # Buscar el proyecto por su ID o crear uno nuevo si no existe
    project_plan = get_object_or_404(ProjectPlan, id=project_id) if project_id else None

    if request.method == 'POST':
        form = ProjectPlanForm(request.POST, instance=project_plan)
        if form.is_valid():
            project = form.save()
            messages.success(request, "El plan de proyecto ha sido definido exitosamente.")
            return redirect('view_project_plan', project_id = project.id)
        # Haciendo pruebas de mejoramiento al codigo
        """else:
            return render(request, 'projects/define_project_plan.html', {'form': form})"""
    else:
        form = ProjectPlanForm(instance=project_plan)

    return render(request, 'projects/define_project_plan.html', {'form': form, 'project_plan':project_plan})



@login_required
def view_project_plan(request, project_id):
    # Haciendo pruebas de mejoramiento al codigo
    """try:
        project_plan = ProjectPlan.objects.get(id=1)  # Cambia '1' por el id o criterio que necesites
    except ProjectPlan.DoesNotExist:
        project_plan = None"""
    project_plan = get_object_or_404(ProjectPlan, id=project_id)

    return render(request, 'projects/view_project_plan.html', {'project_plan': project_plan})

# Prueba, creacion indice!!!!!!!!!!!!!!!!!!###############################
@login_required
def indice(request):
    proyecto_actual = ProjectPlan.objects.order_by('-startDate').first()  # Selecciona el proyecto más reciente o ajusta el criterio
    return render(request, 'projects/indice.html', {'proyecto_actual': proyecto_actual})

#########################################

@login_required
def recent_projects(request):
    # Proyectos más recientes del usuario
    recent_projects = ProjectPlan.objects.filter(employeeName=request.user.username).order_by('-startDate')[:5]
    
    return render(request, 'projects/recent_projects.html', {'recent_projects': recent_projects})
@login_required
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')  # Redirigir a la lista de tareas, por ejemplo
    else:
        form = TaskForm()
    
    return render(request, 'tasks/add_task.html', {'form': form})    
@login_required
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    
    return render(request, 'tasks/edit_task.html', {'form': form, 'task': task})
@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')  # Redirigir a la lista de tareas
    return render(request, 'tasks/delete_task.html', {'task': task})

@login_required
def task_list(request):
    tasks = Task.objects.all()  # Consulta todas las tareas en la base de datos
    return render(request, 'tasks/task_list.html', {'tasks': tasks})  # Renderiza la plantilla 'task_list.html'

@login_required
def agregar_restriccion(request, project_id):
    # Obtener el proyecto o lanzar error 404 si no existe
    proyecto = get_object_or_404(ProjectPlan, id=project_id)
    
    # Manejo de solicitud POST para guardar la restricción
    if request.method == 'POST':
        form = RestriccionForm(request.POST)
        if form.is_valid():
            # Crear la instancia de Restriccion sin guardarla aún
            restriccion = form.save(commit=False)
            # Asignar el proyecto a la restricción
            restriccion.proyecto = proyecto
            # Guardar la restricción en la base de datos
            restriccion.save()
            # Mensaje de éxito para el administrador
            messages.success(request, "La restricción ha sido agregada exitosamente.")
            # Redirigir a la vista del proyecto para revisar la restricción
            return redirect('view_project_plan', project_id=proyecto.id)
    else: 
        #  Inicializar el formulario vacío si la solicitud no es POST
        form = RestriccionForm()
    # Renderizar la plantilla de agregar restricción
    return render(request, 'projects/agregar_restriccion.html', {'form': form, 'proyecto': proyecto})