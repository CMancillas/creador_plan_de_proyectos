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
    path('define-project-plan/', views.define_project_plan, name='define_project_plan'),
    path('view_project_plan/<int:project_id>/', views.view_project_plan, name='view_project_plan'),
    path('edit_project_plan/<int:project_id>/', views.edit_project_plan, name='edit_project_plan'),
    path('project/<int:project_id>/define-resources/', views.define_resources, name='define_resources'),
    path('project/<int:project_id>/resources/', views.view_resources, name='view_resources'),
    path('project/<int:project_id>/define-risks/', views.define_risks, name='define_risks'),
    path('indice/<int:project_id>/', views.indice, name='indice'),
    path('tasks/add/<int:project_id>/', views.add_task, name='add_task'),
    path('tasks/edit/<int:task_id>/', views.edit_task, name='edit_task'),
    path('tasks/delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('view-project-plan/<int:project_id>/tasks/', views.task_list, name='task_list'),
    path('delete/project/<int:project_id>/', views.delete_project_plan, name='delete_project_plan'),
    
]