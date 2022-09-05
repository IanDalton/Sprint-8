from django.urls import path

from . import views

app_name = 'tarjetas'
urlpatterns = [
    path('', views.TarjetasView.as_view(), name='tarjetas'),
]