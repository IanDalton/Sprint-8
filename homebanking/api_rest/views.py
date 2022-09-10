import re
from rest_framework import viewsets
from .serializers import TarjetaSerializer, MarcasTarjetaSerializer, CuentaSerializer, DireccionSerializer, ClienteSerializer, AuditoriaCuentaSerializer, SucursalSerializer, DireccionClienteSerializer, EmpleadoSerializer, MovimientosSerializer, TipoClienteSerializer, TipoCuentaSerializer, PrestamoSerializer
from tarjetas.models import Tarjeta, MarcasTarjeta
from prestamos.models import Prestamo
from cuentas.models import Cuenta, Direccion, Cliente, AuditoriaCuenta, Sucursal, DireccionCliente, Empleado, Movimientos, TipoCliente, TipoCuenta
#from django.contrib.auth.models import User
#from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class CuentaViewSet(viewsets.ModelViewSet):
    serializer_class = CuentaSerializer
    permission_classes = [permissions.Sologet]

    def get_queryset(self, *args, **kwargs):
        current_user = self.request.user
        datoscuenta = Cuenta.objects.filter(customer_id=current_user.id)
        return datoscuenta

class DireccionViewSet(viewsets.ModelViewSet):
    queryset = Direccion.objects.all()
    serializer_class = DireccionSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    serializer_class = ClienteSerializer
    permission_classes = [permissions.Sologet]

    def get_queryset(self, *args, **kwargs):
        current_user = self.request.user
        datoscliente = Cliente.objects.filter(customer_id=current_user.id)
        return datoscliente

class AuditoriaCuentaViewSet(viewsets.ModelViewSet):
    queryset = AuditoriaCuenta.objects.all()    
    serializer_class = AuditoriaCuentaSerializer

class SucursalViewSet(viewsets.ModelViewSet):
    serializer_class = SucursalSerializer

    def get_queryset(self, *args, **kwargs):
        datossucursal = Direccion.objects.all()
        return datossucursal

class DireccionClienteViewSet(viewsets.ModelViewSet):
    queryset = DireccionCliente.objects.all()
    serializer_class = DireccionClienteSerializer

class EmpleadoViewSet(viewsets.ModelViewSet):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer

class MovimientosViewSet(viewsets.ModelViewSet):
    queryset = Movimientos.objects.all()
    serializer_class = MovimientosSerializer

class TipoClienteViewSet(viewsets.ModelViewSet):
    queryset = TipoCliente.objects.all()
    serializer_class = TipoClienteSerializer

class TipoCuentaViewSet(viewsets.ModelViewSet):
    queryset = TipoCuenta.objects.all()
    serializer_class = TipoCuentaSerializer

class PrestamoViewSet(viewsets.ModelViewSet):
    serializer_class = PrestamoSerializer

    def get_queryset(self, *args, **kwargs):
        current_user = self.request.user
        datosprestamo = Prestamo.objects.filter(customer_id = current_user.id,)

        return datosprestamo
    
    def retrieve(self, request, *args, **kwargs):
        current_user = self.request.user
        if current_user.is_staff == True:
            parametro = kwargs
            prestamoquery = Prestamo.objects.filter(branch_id = parametro['pk'])
            serializer = PrestamoSerializer(prestamoquery, many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response("El Usuario no posee los permisos para realizar esta consulta",status=status.HTTP_306_RESERVED)

    def create(self, request, *args, **kwargs):
        current_user = self.request.user
        if current_user.is_staff == True:
            serializer = PrestamoSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()                
                usuario_id = serializer.data.get('customer_id')
                monto = serializer.data.get('loan_total')
                usuario = Cuenta.objects.get(customer = usuario_id)
                usuario.balance = usuario.balance + monto
                usuario.save()

                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response("El Usuario no posee los permisos para realizar esta request",status=status.HTTP_306_RESERVED)

    

        


class TarjetaViewSet(viewsets.ModelViewSet):
    serializer_class = TarjetaSerializer
    permission_classes = [permissions.Sologet]

    def get_queryset(self, *args, **kwargs):
        current_user = self.request.user
        datostarjeta = Tarjeta.objects.filter(client = current_user.id,)

        return datostarjeta

    def retrieve(self, request, *args, **kwargs):
        current_user = self.request.user
        if current_user.is_staff == True:
            parametro = kwargs
            tarjetaquery = Tarjeta.objects.filter(client = parametro['pk'])
            serializer = TarjetaSerializer(tarjetaquery, many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response("El Usuario no posee los permisos para realizar esta consulta",status=status.HTTP_306_RESERVED)

class MarcasTarjetaViewSet(viewsets.ModelViewSet):
    queryset = MarcasTarjeta.objects.all()
    serializer_class = MarcasTarjetaSerializer