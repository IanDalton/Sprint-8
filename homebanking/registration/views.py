from django.views import generic
from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from .forms import CustomRegistrationForm,ClienteForm
from cuentas.models import Cliente,Cuenta,TipoCuenta


class SignUp(generic.CreateView):
    form_class = CustomRegistrationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        super(SignUp, self).form_valid(form)
        username, password = form.cleaned_data.get('username'), form.cleaned_data.get('password1')
        new_user = authenticate(username=username, password=password)
        dni,dob,name,surname = form.cleaned_data.get('dni'),form.cleaned_data.get('date_of_birth'),form.cleaned_data.get('first_name'),form.cleaned_data.get('last_name')
        login(self.request, new_user)
        c = Cliente(customer_username=self.request.user,customer_name=name,customer_surname=surname,customer_dni=dni,dob=dob)
        c.save()
        cuenta = Cuenta(customer=c,balance=0,iban='FI5598296752114394',account_type=TipoCuenta.objects.all().first())
        cuenta.save()
        return HttpResponseRedirect(reverse('cuentas:cuenta'))

class Registo(generic.CreateView):
    form_class = ClienteForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class ClienteRegistration(generic.CreateView):
    form_class = ClienteForm
    success_url = reverse_lazy('registration:signup')
    template_name = 'registration/registro_cliente.html'
