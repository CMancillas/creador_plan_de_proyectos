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
from .forms import RegisterForm, AmbitoProyectoForm, ProjectPlanForm, TaskForm, ResourceForm, ProjectRisksForm
from .models import AmbitoProyecto, Task, ProjectPlan, Resource, ProjectRisks
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
    
# Protected View
class ProtectedView(LoginRequiredMixin, View):
    login_url = '/login/'
    # 'next' - to redirect URL
    redirect_field_name = 'redirect_to'

    def get(self, request):
        return render(request, 'registration/protected.html')

def add_task(request, project_id):
    project = get_object_or_404(ProjectPlan, id=project_id)
    form = TaskForm(request.POST or None)

    if form.is_valid():
            task = form.save(commit=False)
            task.project = project  # Associate the task with the project
            task.save()
            return redirect('task_list', project_id=project.id)

    return render(request, 'tasks/add_task.html', {'form': form, 'project': project})  
@login_required
def definir_ambito_proyecto(request, project_id):
    project_plan = get_object_or_404(ProjectPlan, id=project_id)
    form = AmbitoProyectoForm(request.POST or None)

    if form.is_valid():
        ambito = form.save(commit=False)
        ambito.project = project_plan
        ambito.save()
        return redirect('ver_ambito_proyecto', project_id=project_plan.id)

    return render(request, 'accounts/definir_ambito.html', {'form': form, 'project_plan': project_plan})
@login_required
def ver_ambito_proyecto(request, project_id):
    project_plan = get_object_or_404(ProjectPlan, id=project_id)
    ambito_proyecto = AmbitoProyecto.objects.filter(project = project_id)
    #context = {'ambito_proyecto': ambito_proyecto, 'project_plan': project_plan}
    return render(request, 'accounts/ver_ambito.html',{'ambito_proyecto': ambito_proyecto,'project_plan': project_plan})
@login_required
def recent_projects(request):
    # Proyectos más recientes del usuario
    recent_projects = ProjectPlan.objects.all()
    context = {'recent_projects': recent_projects}
    return render(request, 'home/home.html', context)
@login_required
def delete_project_plan(request, project_id):
    # Obtén el proyecto o muestra una página 404 si no existe
    project_plan = get_object_or_404(ProjectPlan, id=project_id) 

    if request.method == 'POST':
        project_plan.delete()
        messages.success(request, "El proyecto ha sido eliminado exitosamente.")
        return redirect('home') 

    # Renderiza la página de confirmación de eliminación
    return render(request, 'projects/delete_project_plan.html', {'project_plan': project_plan})

@login_required
def define_project_plan(request):
    project_plan = None

    if request.method == 'POST':
        form = ProjectPlanForm(request.POST)
        if form.is_valid():
            project_plan = form.save()  # Guarda el nuevo proyecto y obtén la instancia
            messages.success(request, "El plan de proyecto ha sido definido exitosamente.")
            return redirect('view_project_plan', project_id=project_plan.id)  # Redirige al nuevo proyecto
        else:
            return render(request, 'projects/define_project_plan.html', {'form': form})
    else:
        form = ProjectPlanForm()

    return render(request, 'projects/define_project_plan.html', {'form': form})


@login_required
def view_project_plan(request, project_id):
    try:
        project_plan = ProjectPlan.objects.get(id=project_id)  # Obtiene el proyecto por su ID
    except ProjectPlan.DoesNotExist:
        project_plan = None

    return render(request, 'projects/view_project_plan.html', {'project_plan': project_plan})


def edit_project_plan(request, project_id):
    project = get_object_or_404(ProjectPlan, id=project_id)
    
    if request.method == 'POST':
        form = ProjectPlanForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            messages.success(request, "El proyecto ha sido actualizado exitosamente.")
            # Redirige a la vista de detalle del proyecto usando el nombre de la URL y pasando el project_id
            return redirect('view_project_plan', project_id=project.id)
    else:
        form = ProjectPlanForm(instance=project)
    
    return render(request, 'projects/edit_project_plan.html', {'form': form, 'project': project})



# Prueba, creacion indice!!!!!!!!!!!!!!!!!!###############################
@login_required
def indice(request, project_id):
    try:
        project_plan = ProjectPlan.objects.get(id=project_id)  # Obtiene el proyecto por su ID
    except ProjectPlan.DoesNotExist:
        project_plan = None
    return render(request, 'projects/indice.html', {'project_plan': project_plan})
#########################################

@login_required
def recent_projects(request):
    # Proyectos más recientes del usuario
    recent_projects = ProjectPlan.objects.all()
    context = {'recent_projects': recent_projects}
    return render(request, 'home/home.html', context)
@login_required
def add_task(request, project_id):
    project = get_object_or_404(ProjectPlan, id=project_id)
    form = TaskForm(request.POST or None)

    if form.is_valid():
            task = form.save(commit=False)
            task.project = project  # Associate the task with the project
            task.save()
            return redirect('task_list', project_id=project.id)

    return render(request, 'tasks/add_task.html', {'form': form, 'project': project})  
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
def task_list(request, project_id):
    
    tasks = Task.objects.filter(project = project_id)  # Consulta todas las tareas en la base de datos
    return render(request, 'tasks/task_list.html', {'tasks': tasks})  # Renderiza la plantilla 'task_list.html'


@login_required
def define_resources(request, project_id):
    project = get_object_or_404(ProjectPlan, id=project_id)  # Obtén el proyecto al que se están agregando recursos

    if request.method == 'POST':
        form = ResourceForm(request.POST)  # Cambia a tu formulario de recursos
        if form.is_valid():
            resource = form.save(commit=False)  # No guardes aún, asigna el proyecto
            resource.project = project  # Asigna el proyecto
            resource.save()  # Guarda el recurso

            messages.success(request, "El recurso ha sido agregado exitosamente.")
            return redirect('define_resources', project_id=project.id)  # Redirige a la misma URL

    else:
        form = ResourceForm()

    return render(request, 'projects/define_resources.html', {'form': form, 'project_id': project_id})


@login_required
def view_resources(request, project_id):
    project_plan = get_object_or_404(ProjectPlan, id=project_id)

    resources = project_plan.resources.all()

    return render(request, 'projects/view_resources.html', {
        'project_plan': project_plan,
        'resources': resources
    })


def define_risks(request, project_id):
    project_plan = get_object_or_404(ProjectPlan, id=project_id)

    if request.method == 'POST':
        form = ProjectRisksForm(request.POST)
        if form.is_valid():
            risk = form.save(commit=False)
            risk.project_plan = project_plan  # Asocia el riesgo con el proyecto actual
            risk.save()
            messages.success(request, "El riesgo ha sido registrado exitosamente.")
            return redirect('define_risks', project_id=project_id)  # Redirige a la misma URL para seguir añadiendo riesgos
        else:
            return render(request, 'projects/define_risks.html', {'form': form, 'project_plan': project_plan})
    else:
        form = ProjectRisksForm()

    return render(request, 'projects/define_risks.html', {'form': form, 'project_plan': project_plan})

