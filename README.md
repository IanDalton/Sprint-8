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
