from django import forms

# creating a form


class InputForm(forms.Form):
    monto = forms.FloatField()
    destinatario = forms.CharField()
    motivo = forms.CharField()
