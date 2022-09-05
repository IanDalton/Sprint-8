from datetime import datetime
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy
from .forms import PrestamoForm
from .models import Prestamo
from cuentas.models import Cliente,Cuenta,TipoCuenta,Movimientos
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse

class PrestamosViews(LoginRequiredMixin, TemplateView):
    template_name = 'prestamos/prestamos.html'

class PrestamosForm(generic.CreateView):
    form_class = PrestamoForm
    success_url = reverse_lazy('prestamos:prestamos')
    template_name = 'prestamos/prestamos.html'
    def form_valid(self, form):

        type = form.cleaned_data.get('loan_type')
        date = form.cleaned_data.get('loan_date')
        total =form.cleaned_data.get('loan_total')
        
        usr_id = Cliente.objects.all().filter(customer_username=self.request.user).first()
        print(usr_id)
        
        p = Prestamo(loan_type =type,loan_date = date,loan_total = total,customer_id =usr_id)
        
        plata = Cuenta.objects.all().filter(customer=usr_id,account_type = TipoCuenta.objects.all().filter(type_id=1).first()).first()
        print(plata)
        plata.balance += total
        
        trans = Movimientos(account_number=usr_id,amount =total,reason ='Prestamo ITBANK',operation_type ='Prestamo Pre-aprobado',status ='Recibido',date=datetime.now())
        trans.save()
        p.save()
        plata.save()
        return HttpResponseRedirect(reverse('cuentas:cuenta'))
