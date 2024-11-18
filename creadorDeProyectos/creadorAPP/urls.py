from django.urls import path
from . import views

urlpatterns = [
    path('', views.recent_projects, name='home'), 
    path('login/', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('protected/', views.ProtectedView.as_view(), name='protected'),
    path('project-plan/<int:project_id>/definir-ambito/', views.definir_ambito_proyecto, name='definir_ambito_proyecto'),
    path('project-plan/<int:project_id>/editar-ambito/', views.editar_ambito_proyecto, name='editar_ambito_proyecto'),
    path('project-plan/<int:project_id>/ver-ambito/', views.ver_ambito_proyecto, name='ver_ambito_proyecto'),
    path('define-project-plan/', views.define_project_plan, name='define_project_plan'), # Para crear un nuevo rpoyecto
    path('project-plan/<int:project_id>/', views.view_project_plan, name='view_project_plan'),
    path('project-plan/<int:project_id>/edit/', views.edit_project_plan, name='edit_project_plan'),
    path('project-plan/<int:project_id>/define-resources/', views.define_resources, name='define_resources'),
    path('project-plan/<int:project_id>/edit-resource/<int:resource_id>/', views.edit_resource, name='edit_resource'),
    path('project-plan/<int:project_id>/resources/', views.view_resources, name='view_resources'),
    path('project-plan/<int:project_id>/define-risks/', views.define_risks, name='define_risks'),
    path('project-plan/<int:project_id>/tasks/', views.task_list, name='task_list'),
    path('project-plan/<int:project_id>/delete/', views.delete_project_plan, name='delete_project_plan'),
    path('project-plan/<int:project_id>/define-team/', views.define_work_team, name='define_work_team'),
    path('project-plan/<int:project_id>/team/', views.view_work_team, name='view_work_team'),
    path('project-plan/<int:project_id>/team/edit/<int:member_id>/', views.edit_work_team_member, name='edit_work_team_member'),
    path('project-plan/<int:project_id>/team/delete/<int:member_id>/', views.delete_work_team_member, name='delete_work_team_member'),
    path('project-plan/<int:project_id>/indice/', views.indice, name='indice'),
    path('project-plan/<int:project_id>/tasks/add/', views.add_task, name='add_task'),
    path('project-plan/<int:project_id>/tasks/edit/<int:task_id>/', views.edit_task, name='edit_task'),
    path('project-plan/<int:project_id>/tasks/delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('project-plan/<int:project_id>/agregar-restriccion/', views.agregar_restriccion, name='agregar_restriccion'),  
    path('project-plan/<int:project_id>/resumen-proyecto/', views.resumen_proyecto, name='resumen_proyecto'),
    path('project-plan/<int:project_id>/descargar-resumen/', views.descargar_resumen_pdf, name='descargar_resumen_pdf'),
    path('project-plan/<int:project_id>/ver-restriccion/', views.ver_restricciones, name='ver_restriccion'),
    path('project-plan/<int:project_id>/view-risks/', views.view_risks, name='view_risks'),
    path('search-results/', views.search_results, name='search_results'),
    path('search/', views.search, name='search'),
    path('project-plan/<int:project_id>/descargar-plan-completo/', views.descargar_plan_completo_pdf, name='descargar_plan_completo'),

]