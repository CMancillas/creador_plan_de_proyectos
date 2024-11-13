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
from .forms import RegisterForm, AmbitoProyectoForm, ProjectPlanForm, TaskForm, RestriccionForm,  ResourceForm, ProjectRisksForm, WorkTeamMemberForm
from .models import AmbitoProyecto, Task, ProjectPlan, Resource, ProjectRisks, WorkTeamMember, Restriccion
from django.contrib import messages
# Importa HttpResponse de Django para enviar una respuesta HTTP al navegador.
from django.http import HttpResponse
# Importa render_to_string para convertir una plantilla HTML en una cadena de texto.
from django.template.loader import render_to_string
# Importa HTML de WeasyPrint, que convierte el HTML en un PDF.
#from weasyprint import HTML

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

@login_required
def definir_ambito_proyecto(request, project_id):
    project_plan = get_object_or_404(ProjectPlan, id=project_id)
    form = AmbitoProyectoForm(request.POST or None)

    if form.is_valid():
        ambito = form.save(commit=False)
        ambito.project = project_plan
        ambito.save()
        return redirect('ver_ambito_proyecto', project_id=project_plan.id)

    return render(request, 'projects/definir_ambito.html', {'form': form, 'project_plan': project_plan})

@login_required
def editar_ambito_proyecto(request, project_id):
    project_plan = get_object_or_404(ProjectPlan, id=project_id)
    ambito_proyecto = get_object_or_404(AmbitoProyecto, project=project_plan)

    # Carga el formulario con los datos del ámbito existente
    form = AmbitoProyectoForm(request.POST or None, instance=ambito_proyecto)

    if form.is_valid():
        form.save()
        return redirect('ver_ambito_proyecto', project_id=project_plan.id)

    return render(request, 'projects/editar_ambito.html', {'form': form, 'project_plan': project_plan})

@login_required
def ver_ambito_proyecto(request, project_id):
    project_plan = get_object_or_404(ProjectPlan, id=project_id)
    ambito_proyecto = AmbitoProyecto.objects.filter(project=project_id).first()
    #context = {'ambito_proyecto': ambito_proyecto, 'project_plan': project_plan}
    return render(request, 'projects/ver_ambito.html',{'ambito_proyecto': ambito_proyecto,'project_plan': project_plan})

@login_required
def define_project_plan(request):
    project_plan = None

    if request.method == 'POST':
        form = ProjectPlanForm(request.POST)
        if form.is_valid():
            project_plan = form.save(commit=False)
            project_plan.created_by = request.user
            project_plan.save()
            messages.success(request, "El plan de proyecto ha sido definido exitosamente.")
            return redirect('view_project_plan', project_id=project_plan.id)  # Redirige al nuevo proyecto
        else:
            return render(request, 'projects/define_project_plan.html', {'form': form})
    else:
        form = ProjectPlanForm()

    return render(request, 'projects/define_project_plan.html', {'form': form})


'''
@login_required
def view_project_plan(request, project_id):
    try:
        project_plan = ProjectPlan.objects.get(id=project_id)  # Obtiene el proyecto por su ID
    except ProjectPlan.DoesNotExist:
        project_plan = None

    return render(request, 'projects/view_project_plan.html', {'project_plan': project_plan})
'''
@login_required
def view_project_plan(request, project_id):
    # Obtiene el proyecto principal o devuelve un error 404 si no existe
    project_plan = get_object_or_404(ProjectPlan, id=project_id)
    
    # Filtra y obtiene datos relacionados del proyecto
    ambito = AmbitoProyecto.objects.filter(project_id=project_id)
    tasks = Task.objects.filter(project_id=project_id)
    team = WorkTeamMember.objects.filter(project_id=project_id)
    resources = Resource.objects.filter(project_id=project_id)
    restrictions = Restriccion.objects.filter(proyecto_id=project_id)
    risks = ProjectRisks.objects.filter(project_plan_id=project_id)

    # Agrega todos los datos al contexto
    context = {
        'project_plan': project_plan,
        'ambito': ambito,
        'tasks': tasks,
        'team': team,
        'resources': resources,
        'restrictions': restrictions,
        'risks': risks
    }
    
    # Renderiza la plantilla con todos los datos
    return render(request, 'projects/view_project_plan.html', context)

@login_required
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

@login_required
def indice(request, project_id):
    project_plan = ProjectPlan.objects.get(id=project_id)  # Obtiene el proyecto por su ID
    return render(request, 'projects/indice.html', {'project_plan': project_plan})


@login_required
def recent_projects(request):
    # Proyectos más recientes del usuario
    recent_projects = ProjectPlan.objects.filter(created_by=request.user)
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
def edit_task(request, task_id, project_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list', project_id)
    else:
        form = TaskForm(instance=task)
    
    return render(request, 'tasks/edit_task.html', {'form': form, 'task': task, 'project_id': project_id})

@login_required
def delete_task(request, task_id, project_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list', project_id)  # Redirigir a la lista de tareas
    return render(request, 'tasks/delete_task.html', {'task': task, 'project_id': project_id})

@login_required
def task_list(request, project_id):
    
    tasks = Task.objects.filter(project = project_id)  # Consulta todas las tareas asociadas al proyecto
    return render(request, 'tasks/task_list.html', {'tasks': tasks, 'project_id':project_id})  # Renderiza la plantilla 'task_list.html'

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

@login_required
def resumen_proyecto(request,project_id):
    # Se obtiene el objeto ProjectPlan con su id correspondiente.
    # Si no existe, se devuelve una pagina de error 404.
    proyecto = get_object_or_404(ProjectPlan, id=project_id)
    
    # Se obtiene todas las restricciones asociadas al proyecto.
    restricciones = proyecto.restricciones.all()
    
    # Se obtiene todas las tareas asociadas al proyecto.
    tareas = proyecto.tasks.all()

    # Se obtiene todos los riesgos asociados al proyecto.
    riesgos = proyecto.risks.all()

    # Se renderiza la plantilla 'resumen_proyecto.html', pasando como contexto:
    # el proyecto, las restricciones y las tareas, para su visualizacion en el HTML.
    return render(request, 'projects/resumen_proyecto.html', {
        'proyecto': proyecto,
        'restricciones': restricciones,
        'tareas': tareas,
        'riesgos':riesgos,  
    })

@login_required
def descargar_resumen_pdf(request, project_id):
    # Se obtiene el objeto ProjectPlan con su id correspondiente.
    # Si no existe, se devuelve una pagina de error 404.
    proyecto = get_object_or_404(ProjectPlan, id=project_id)
    
    # Se obtiene todas las restricciones asociadas al proyecto.
    restricciones = proyecto.restricciones.all()
    
    # Se obtiene todas las tareas asociadas al proyecto.
    tareas = proyecto.tasks.all()    

    # Se obtiene todos los riesgos asociados al proyecto.
    riesgos = proyecto.risks.all()

    # Renderiza la plantilla HTML en una cadena de texto.
    html_string = render_to_string('projects/resumen_proyecto.html', {
        'proyecto': proyecto,
        'restricciones': restricciones,
        'tareas': tareas,
        'riesgos': riesgos,
    })

    # Crea la respuesta HTTP como un archivo PDF.
    response = HttpResponse(content_type='application/pdf')
    
    # Configura la respuesta para que el PDF se descargue con un nombre de archivo basado en el titulo del proyecto.
    response['Content-Disposition'] = f'attachment; filename="Resumen_Proyecto_{proyecto.title}.pdf"'

    # Usa WeasyPrint para convertir el HTML en un PDF y escribirlo en la respuesta.
    HTML(string=html_string).write_pdf(response)

    # Retorna la respuesta con el PDF, permitiendo que el navegador descargue el archivo.
    return response


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
def edit_resource(request, project_id, resource_id):
    project_plan = get_object_or_404(ProjectPlan, id=project_id)
    resource = get_object_or_404(Resource, id=resource_id, project=project_plan)

    if request.method == 'POST':
        form = ResourceForm(request.POST, instance=resource)
        if form.is_valid():
            form.save()
            messages.success(request, "El recurso ha sido actualizado exitosamente.")
            return redirect('view_resources', project_id=project_id)

    else:
        form = ResourceForm(instance=resource)

    return render(request, 'projects/edit_resource.html', {
        'form': form,
        'project_plan': project_plan,
        'resource': resource
    })

@login_required
def view_resources(request, project_id):
    project_plan = get_object_or_404(ProjectPlan, id=project_id)

    resources = project_plan.resources.all()

    return render(request, 'projects/view_resources.html', {
        'project_plan': project_plan,
        'resources': resources
    })


@login_required
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

@login_required
def define_work_team(request, project_id):
    project = get_object_or_404(ProjectPlan, id=project_id)
    team_members = project.team_members.all()
    if request.method == 'POST':
        form = WorkTeamMemberForm(request.POST)
        if form.is_valid():
            team_member = form.save(commit=False)
            team_member.project = project
            team_member.save()
            messages.success(request, "El miembro del equipo ha sido añadido exitosamente.")
            return redirect('view_work_team', project_id=project.id)
        else:
            messages.error(request, "Error al añadir el miembro del equipo. Por favor, corrige los errores.")
    else:
        form = WorkTeamMemberForm()

    return render(request, 'work_team/define_work_team.html', {'form': form, 'project': project, 'team_members': team_members})


@login_required
def edit_work_team_member(request, project_id, member_id):
    project_plan = get_object_or_404(ProjectPlan, id=project_id)
    team_member = get_object_or_404(WorkTeamMember, id=member_id)

    if request.method == 'POST':
        form = WorkTeamMemberForm(request.POST, instance=team_member)
        if form.is_valid():
            form.save()
            messages.success(request, "El rol del miembro ha sido actualizado.")
            return redirect('view_work_team', project_id=project_id)
    else:
        form = WorkTeamMemberForm(instance=team_member)
    
    return render(request, 'work_team/edit_work_team_member.html', {'form': form, 'project_plan': project_plan, 'team_member': team_member})


@login_required
def delete_work_team_member(request, project_id, member_id):
    team_member = get_object_or_404(WorkTeamMember, id=member_id)
    team_member.delete()

    messages.success(request, "El miembro del equipo ha sido eliminado.")

    return redirect('view_work_team', project_id=project_id)


@login_required
def view_work_team(request, project_id):
    project_plan = get_object_or_404(ProjectPlan, id=project_id)
    team_members = project_plan.team_members.all()

    return render(request, 'work_team/view_work_team.html', {'project_plan': project_plan, 'team_members': team_members})

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

def ver_restricciones(request, project_id):
    restricciones = Restriccion.objects.filter(proyecto = project_id)
    return render(request, 'projects/ver_restriccion.html', {'restricciones': restricciones, 'project_id': project_id})

def view_risks(request, project_id):
    project_risks = ProjectRisks.objects.filter(project_plan = project_id)
    return render(request, 'projects/view_risks.html', {'project_risks': project_risks, 'project_id': project_id})