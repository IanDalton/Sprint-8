from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CuentaViewSet, DireccionViewSet, ClienteViewSet, AuditoriaCuentaViewSet, SucursalViewSet, DireccionClienteViewSet, EmpleadoViewSet, MovimientosViewSet, TipoClienteViewSet, TipoCuentaViewSet, PrestamoViewSet, TarjetaViewSet, MarcasTarjetaViewSet

router = DefaultRouter()
router.register(r'cliente', ClienteViewSet) # Obtener datos de un cliente
router.register(r'cuenta', CuentaViewSet) # Obtener saldo de cuenta de un cliente
router.register(r'prestamo', PrestamoViewSet) # Obtener monto de un prestamo y total del prestamo
router.register(r'tarjetas', TarjetaViewSet)
router.register(r'marcas_tarjeta', MarcasTarjetaViewSet)
router.register(r'auditoria_cuenta', AuditoriaCuentaViewSet)
router.register(r'direccion_cliente', DireccionClienteViewSet)
router.register(r'empleado', EmpleadoViewSet)
router.register(r'movimientos', MovimientosViewSet)
router.register(r'tipo_cliente', TipoClienteViewSet)
router.register(r'tipo_cuenta', TipoCuentaViewSet)
router.register(r'direccion', DireccionViewSet) # Modificar Direccion de un cliente
router.register(r'sucursal', SucursalViewSet) # Listado de todas las sucursales

urlpatterns = [
    path('', include(router.urls)),
]