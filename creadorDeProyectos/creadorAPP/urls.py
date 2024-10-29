from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('protected/', views.ProtectedView.as_view(), name='protected'),
    path('definir-ambito/', views.definir_ambito_proyecto, name='definir_ambito_proyecto'),
    path('ver-ambito/', views.ver_ambito_proyecto, name='ver_ambito_proyecto'),
    # path('proyecto/eliminar/<int:proyecto_id>/', views.eliminar_proyecto, name='eliminar_proyecto'),
    path('define-project-plan/', views.define_project_plan, name='define_project_plan'), # Para crear un nuevo rpoyecto
    path('define-project-plan/<int:project_id>/', views.define_project_plan, name='define_project_plan'), # Para editar un proyecto especifico 
    path('view-project-plan/<int:project_id>/', views.view_project_plan, name='view_project_plan'),
    #### Prueba
    path('indice/', views.indice, name='indice'),
    #######
    path('tasks/add/', views.add_task, name='add_task'),
    path('tasks/edit/<int:task_id>/', views.edit_task, name='edit_task'),
    path('tasks/delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('projects/recent/', views.recent_projects, name='recent_projects'), 
    path('tasks/', views.task_list, name='task_list'),  # Define la URL con el nombre 'task_list'

]