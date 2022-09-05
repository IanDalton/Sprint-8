from django.urls import path

from . import views


app_name = 'clientes'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('ayuda/', views.AyudaView.as_view(), name='ayuda'),
    path('divisas/', views.DivisasView.as_view(), name='divisas'),
]
