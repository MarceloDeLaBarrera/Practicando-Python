# Los archivos externos permiten la persistencia de los datos, es decir, que no se pierdan independiente que se termine la ejecución del programa.
# La informacion puede ser guardada en archivos externos o en bases de datos.
# Stream= Flujos de datos que permiten trabajar con archivos externos desde el programa hacia afuera y desde fuera hacia el programa.


from os import read, write
from pathlib import Path
import os


# Open permite leer archivos externos. Abrirlos. Se le pasan dos parametros, la ruta y el modo en que se abrira el archivo.
# Se puede abrir en modo lectura con "r". En modo escritura con "w" para escribir sobre archivo vacio. "r+" permite leer y escribir a la vez. En modo "a" de append para agregar info a un archivo que ya tiene escritura en su interior.
# Si archivo no existe, lo crea.

"""Opcionalmente se puede usar try y finally para asegurarse de que el fichero realmente se cierre puesto que en codigos mas extensos a veces no se cierra"""

# Formas de Acceder a la ruta completa del fichero
complete_path = Path(__file__).resolve()
aa = os.path.abspath(__file__)

# Ir subiendo directorios u obtener el directorio de la ruta absoluta del archivo actual:
aaa = os.path.dirname(aa)
aaaa = os.path.dirname(aaa)

# Si se añaden .parent, se va escalando en directorios.
BASE_PATH = Path(__file__).resolve().parent.parent


# Unir directorios. Se pueden añadir mas de 2, basta con poner entre comillas sin slash, y la union se hace automaticamente generando la ruta completa.
also_complete_path = os.path.join(aaaa, 'Archivos externos', 'Intro.py')

# Crear directorio. Se le pasa como parametro la ruta donde se quiere crear, exist_ok.
os.makedirs(aaa, exist_ok=True)

# Listar archivos de un directorio y guardarlos en un array
os.listdir(aaa)


# Abrir archivo en modo escritura
txt = open(os.path.join(BASE_PATH, 'archivo.txt'), "w")

frase = "Estupendo dia para estudiar Python \nBuenas noches"

# Write permite escribir sobre un archivo.
txt.write(frase)
txt.close()

# Abrir archivo en modo lectura
txt = open(
    os.path.join(BASE_PATH, 'archivo.txt'), "r")
Read = txt.read()
txt.close()
print(Read)


# Abrir archivo pero almacenando cada linea en una lista.
txt = open(
    "D:\\Documentos\\Universidad\\Ing en Informatica\\PracticandoPython\\archivo.txt", "r")
List_of_text = txt.readlines()
listaformateada = []
txt.close()
print(List_of_text)

for elemento in List_of_text:
    linea = elemento.strip("\n")
    listaformateada.append(linea)
print(listaformateada)


# Abrir archivo en modo append para añadir info.
txt = open(
    "D:\\Documentos\\Universidad\\Ing en Informatica\\PracticandoPython\\archivo.txt", "a")

frase2 = "\nBuenos dias"
txt.write(frase2)
txt.close


# Script para crear varios txt en una ruta en particular
"""
Se define inicialmente dentro de un ciclo, el nombre de los archivos, se crea una ruta que une la ruta base + el nombre, 
y finalmente se usa with open para crear cada archivo, en cada vuelta del ciclo.

for i in range(1, 6):
    name = f"Texto {i}.txt"
    file_path = os.path.join(aaa, name)
    if os.path.exists(file_path):
        print("file skipped")
        continue

    with open(file_path, 'w') as file:
        file.write("Hola")
"""
