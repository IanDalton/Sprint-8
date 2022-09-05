from django.urls import path

from . import views

app_name = 'registration'
urlpatterns = [
    path('signup/', views.SignUp.as_view() , name='signup'),
    path('cliente/', views.ClienteRegistration.as_view() , name='registroCliente'),
]
