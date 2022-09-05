from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = "clientes/index.html"

class AyudaView(TemplateView):
    template_name = "clientes/ayuda.html"

class DivisasView(TemplateView):
    template_name = "clientes/divisas.html"