from django.forms import ModelForm
from django import forms
from datetime import datetime
from .models import Prestamo


PRESTAMOS_CHOICES= [
('personal', 'Prestamo Personal'),
('hipotecario', 'Prestamo Hipotecario'),
('prendario', 'Prestamo Prendario'),
]

class PrestamoForm(ModelForm):
    class Meta:
        model = Prestamo
        fields = ['loan_type','loan_date', 'loan_total']
        labels  = {
            'loan_type':'Tipo del prestamo', 
            'loan_date':'Fecha del Prestamo', 
            'loan_total':'Total', 
        }
        widgets = {
                'loan_type':forms.RadioSelect(choices=PRESTAMOS_CHOICES),
                'loan_date': forms.DateInput(attrs={'value': datetime.now().strftime("%d-%m-%Y"), 'min': datetime.now().strftime("%d-%m-%Y")}),
                'loan_total': forms.NumberInput(attrs={'min': 1, 'value': '1'})
        }
