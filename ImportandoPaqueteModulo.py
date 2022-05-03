# Los paquetes son directorios donde se almacenaran modulos relacionados entre si.
# Los modulos son los archivos .py que se importaran entre si para hacer uso de sus clases, funciones, metodos, variables, etc.
# Para importar modulos, deben estar ambos modulos en la misma carpeta.

# Para crear un paquete, se debe crear una carpeta, y en su interior colocar un archivo con nombre "" __init__.py ""

"""
#Importando modulos

import FuncionesMatematicas
FM = FuncionesMatematicas

print(FM.elevar(2, 3))
print(FM.restar(5, 8))
print(FM.dividir(4, 1))



from FuncionesMatematicas import*

print(elevar(2, 3))
print(restar(5, 8))
print(dividir(4, 1))

"""

# Importar modulo desde paquete:

from paquetesModulos.FuncionesMatematicas import multiplicar


print(multiplicar(5, 2))


# Crear paquete distribuible:
"""Se crea un archivo con nombre setup.py en el directorio raiz... Luego se debe rellenar con los sgtes datos:

from setuptools import setup

setup(
    name= "Nombre del paquete",
    version= "Numero de la version",
    description="Descrp del paquete",
    author="nombre autor",
    author_email="email autor",
    packages= ["PaquetesModulos","PaquetesModulos.carpeta_directorio_que_es_paquete"]  #Aca va la ruta del paquete. El primer campo, seria la carpeta principal del paquete. Y si se quiere acceder a un subpaquete, el segundo campo, seria el nombre del paquete principal "." nombre del subpaquete. 
)

-------------------------------------------------------------------------------------------------------------

Una vez hecho lo anterior, se abre el cmd, y se coloca en carpeta directorio raiz, en este caso "Pracitando Python", y estando ahi se usa la isntrccuion:
python setup.py sdist

sdist= Paquete distribuible.

Lo anterior creara una carpeta con extension .egg-info, y una carpeta llamada "dis", donde dentro de ella, se encontrara el paquete distribuible dentro de un rar con extension .tar.gz

"""
# Como instalar Paquetes:
""" Siguiendo lo anterior, dentro del cmd, se debe ubicar en el directorio "dis", y colocar la instruccion:
pip3 install <nombre_paquete (Archivo rar)>
"""
# Para desisntalar:
"""
pip3 uninstall <nombre_paquete (Ojo solo el nombre, todo lo que va hasta antes del guion de la version)>
"""
