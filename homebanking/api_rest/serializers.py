from rest_framework import serializers
from tarjetas.models import Tarjeta, MarcasTarjeta
from prestamos.models import Prestamo
from cuentas.models import Cuenta, Direccion, Cliente, AuditoriaCuenta, Sucursal, DireccionCliente, Empleado, Movimientos, TipoCliente, TipoCuenta

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ('customer_id', 'customer_username', 'customer_name', 'customer_surname', 'customer_dni', 'dob', 'branch_id')

class CuentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cuenta
        fields = ('account_id', 'customer_id', 'balance', 'account_type')

class PrestamoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prestamo
        fields = ('loan_id', 'loan_type', 'loan_date', 'loan_total', 'customer_id','branch')

class MovimientosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movimientos
        fields = ('movement_id', 'account_number', 'amount', 'operation_type', 'hora')

class DireccionClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = DireccionCliente
        fields = ('address_client_id', 'address_type_client')

class DireccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direccion
        fields = ('address_id', 'address_street', 'address_street_number', 'address_city', 'address_country')
    
class AuditoriaCuentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuditoriaCuenta
        fields = ('audit_id','old_id','new_id','old_balance','new_balance', 'old_iban', 'new_iban', 'old_type', 'new_type', 'user_action', 'created_at')

class TipoClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoCliente
        fields = ('client_id','type_client')

class TipoCuentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoCuenta
        fields = ('type_id', 'type_account')

class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = ('employee_id', 'employee_name', 'employee_surname', 'employee_hire_date','employee_dni','branch_id')


class TarjetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarjeta
        fields = ('card_id', 'card_number', 'card_cvv', 'card_gived', 'card_expiration', 'card_type', 'card_brand')

class MarcasTarjetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarcasTarjeta
        fields = ('brand_id', 'type_brand')

class SucursalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sucursal
        fields = ('branch_id', 'branch_number', 'branch_name', 'branch_address_id')
