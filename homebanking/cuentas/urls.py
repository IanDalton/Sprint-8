from django.urls import path

from . import views

app_name = 'cuentas'
urlpatterns = [
    path('', views.CuentaView, name='cuenta'),
    path('actividad/', views.ActividadView, name='actividad'),
    path('perfil/', views.PerfilView.as_view(), name='perfil'),
    path('fondos/', views.FondosView.as_view(), name='fondos'),
    path('transferencias/', views.TransferenciaView, name='transferencia')
]
