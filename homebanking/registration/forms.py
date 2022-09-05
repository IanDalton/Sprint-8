from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from cuentas.models import Cliente
from django.forms import ModelForm
from django import forms


class CustomRegistrationForm(UserCreationForm):
    dni = forms.CharField(label="DNI", max_length=8)
    date_of_birth = forms.DateField(label='Fecha de Nacimiento' ,input_formats=['%d/%m/%Y'],)
    class Meta:
        model = User
        fields = ('first_name', 'last_name','dni','date_of_birth', 'username', 'email')

class ClienteForm(ModelForm):
    dni = forms.CharField(label="DNI", max_length=8)
    date_of_birth = forms.DateField(label='Fecha de Nacimiento' ,input_formats=['%d/%m/%Y'],)

    class Meta:
        model = Cliente
        fields = ('dni', 'date_of_birth',)
