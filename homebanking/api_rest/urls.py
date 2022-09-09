from django.urls import path, include
from rest_framework.routers import DefaultRouter
from tarjetas.models import Tarjeta, MarcasTarjeta
from prestamos.models import Prestamo
from cuentas.models import Cuenta, Direccion, Cliente, AuditoriaCuenta, Sucursal, DireccionCliente, Empleado, Movimientos, TipoCliente, TipoCuenta
from .views import CuentaViewSet, DireccionViewSet, ClienteViewSet, AuditoriaCuentaViewSet, SucursalViewSet, DireccionClienteViewSet, EmpleadoViewSet, MovimientosViewSet, TipoClienteViewSet, TipoCuentaViewSet, PrestamoViewSet, TarjetaViewSet, MarcasTarjetaViewSet

router = DefaultRouter()
router.register(r'cliente', ClienteViewSet,basename=Cliente) # Obtener datos de un cliente
router.register(r'cuenta', CuentaViewSet,basename=Cuenta) # Obtener saldo de cuenta de un cliente
router.register(r'prestamo', PrestamoViewSet,basename=Prestamo) # Obtener monto de un prestamo y total del prestamo
router.register(r'tarjeta', TarjetaViewSet,basename=Tarjeta)
router.register(r'marcas_tarjeta', MarcasTarjetaViewSet,basename=MarcasTarjeta)
router.register(r'auditoria_cuenta', AuditoriaCuentaViewSet,basename=AuditoriaCuenta)
router.register(r'direccion_cliente', DireccionClienteViewSet,basename=DireccionCliente)
router.register(r'empleado', EmpleadoViewSet,basename=Empleado)
router.register(r'movimientos', MovimientosViewSet,basename=Movimientos)
router.register(r'tipo_cliente', TipoClienteViewSet,basename=TipoCliente)
router.register(r'tipo_cuenta', TipoCuentaViewSet,basename=TipoCuenta)
router.register(r'direccion', DireccionViewSet,basename=Direccion) # Modificar Direccion de un cliente
router.register(r'sucursal', SucursalViewSet,basename=Sucursal) # Listado de todas las sucursales

urlpatterns = [
    path('', include(router.urls)),
]