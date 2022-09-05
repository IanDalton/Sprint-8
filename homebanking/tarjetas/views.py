from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class TarjetasView(LoginRequiredMixin, TemplateView):
    template_name = 'Tarjetas/tarjetas.html'
