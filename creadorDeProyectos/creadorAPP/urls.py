from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name="home"),
    path('login/', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('protected/', views.ProtectedView.as_view(), name='protected'),
    path('definir-ambito/', views.definir_ambito_proyecto, name='definir_ambito_proyecto'),
    path('ver-ambito/', views.ver_ambito_proyecto, name='ver_ambito_proyecto'),
    # path('proyecto/eliminar/<int:proyecto_id>/', views.eliminar_proyecto, name='eliminar_proyecto'),
]