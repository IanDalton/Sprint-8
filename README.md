# Sprint8

## Dependencias

- Python3: https://www.python.org/downloads/

- VirtualEnv: https://virtualenv.pypa.io/en/latest/#

- Django: https://www.djangoproject.com/start/overview/

## Ejecución del programa

1. Activar el entorno virtual
    -   Windows: env/Scripts/activate
    -   Mac: source env/bin/activate
2. En caso de crear un nuevo entorno virtual, en Lib/rest_framework/permissions.py
   Insertar 
   
   class Sologet(BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS)
            
## Autores del Proyecto

- Ian Dalton
- Jose Miserendino
- Santiago Ance
- Ignacio Brandán
- Cesar Benitez

USUARIOS PARA TESTEO:
Empleado (staff)
User: randus
pass: passwordrand
Cliente (no-staff)
user: randus2
pass: passwordrand
user: Usuario509
pass: passwordrand

ACCESOS: RequiereN del envio de la request junto con el user y password de un usuario registrado

OBTENER DATOS DE UN CLIENTE
http://127.0.0.1:8000/api/cliente/

OBTENER SALDO DE CUENTA DE UN CLIENTE
http://127.0.0.1:8000/api/cuenta/

OBTENER MONTO DE PRESTAMOS DE UN CLIENTE
http://127.0.0.1:8000/api/prestamo/
(el usuario "randus" no tiene prestamos, el usuario randus2 si, el usuario "Usuario509" tambien)

OBTENER MONTO DE PRESTAMOS DE UNA SUCURSAL
http://127.0.0.1:8000/api/prestamo/<PK>
<PK>: Corresponde al ID de la sucursal de la cual se solicita la request
Requiere usuario staff (Empleado)

