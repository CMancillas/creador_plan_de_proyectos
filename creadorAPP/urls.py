from django.urls import path
from . import views

urlpatterns = [
    path('', views.recent_projects, name='home'), 
    path('login/', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('protected/', views.ProtectedView.as_view(), name='protected'),
    path('definir-ambito/<int:project_id>/', views.definir_ambito_proyecto, name='definir_ambito_proyecto'),
    path('ver-ambito/<int:project_id>/', views.ver_ambito_proyecto, name='ver_ambito_proyecto'),
    path('define-project-plan/', views.define_project_plan, name='define_project_plan'), # Para crear un nuevo rpoyecto
    path('define-project-plan/<int:project_id>/', views.define_project_plan, name='define_project_plan'), # Para editar un proyecto especifico 
    path('view-project-plan/<int:project_id>/', views.view_project_plan, name='view_project_plan'),
    path('edit_project_plan/<int:project_id>/', views.edit_project_plan, name='edit_project_plan'),
    path('project/<int:project_id>/define-resources/', views.define_resources, name='define_resources'),
    path('project/<int:project_id>/resources/', views.view_resources, name='view_resources'),
    path('project/<int:project_id>/define-risks/', views.define_risks, name='define_risks'),
    path('view-project-plan/<int:project_id>/tasks/', views.task_list, name='task_list'),
    path('delete/project/<int:project_id>/', views.delete_project_plan, name='delete_project_plan'),
    path('work_team/<int:project_id>/team/', views.define_work_team, name='define_work_team'),
    path('work_team/<int:project_id>/team/view/', views.view_work_team, name='view_work_team'),
    path('work_team/<int:project_id>/team/edit/<int:member_id>/', views.edit_work_team_member, name='edit_work_team_member'),
    path('work_team/<int:project_id>/team/delete/<int:member_id>/', views.delete_work_team_member, name='delete_work_team_member'),
    path('indice/<int:project_id>/', views.indice, name='indice'),
    path('tasks/add/<int:project_id>/', views.add_task, name='add_task'),
    path('tasks/edit/<int:task_id>/', views.edit_task, name='edit_task'),
    path('tasks/delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('agregar-restriccion/<int:project_id>/', views.agregar_restriccion, name='agregar_restriccion'),  
    path('resumen-proyecto/<int:project_id>/', views.resumen_proyecto, name='resumen_proyecto'),
    path('descargar-resumen/<int:project_id>/', views.descargar_resumen_pdf, name='descargar_resumen_pdf'),
    path('cronograma/<int:project_id>/agregar/', views.agregar_evento, name='agregar_evento'),
    path('cronograma/<int:project_id>/', views.ver_cronograma, name='ver_cronograma'),
    path('proyecto/<int:project_id>/agregar_esfuerzo/', views.agregar_esfuerzo, name='agregar_esfuerzo'),
    path('proyecto/<int:project_id>/esfuerzo/', views.consultar_esfuerzo, name='consultar_esfuerzo'),
    path('proyecto/<int:project_id>/consultar_costo/', views.consultar_costo, name='consultar_costo'),
    

]