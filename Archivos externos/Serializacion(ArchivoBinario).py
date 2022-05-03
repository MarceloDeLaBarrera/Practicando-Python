# Serializacion: Consiste en guardar en un fichero externo una coleccion, diccionario, objetos, pero codificado en codigo binario. Para guardar objetos dentro de un fichero/lista, es la unica forma, ya que tienen metadatos.

import pickle  # Biblioteca necesaria par serializar

nombres = ["marcelo", "pedro", "juan", "jorge"]

# wb= write binary
fichero_binario = open(
    "D:\\Documentos\\Universidad\\Ing en Informatica\\PracticandoPython\\serializacion", "wb")
# Guardado de lista en fichero con dump
pickle.dump(nombres, fichero_binario)
fichero_binario.close()

fichero_binario = open(
    "D:\\Documentos\\Universidad\\Ing en Informatica\\PracticandoPython\\serializacion", "rb")

# Load permite cargar el codigo binario del fichero. Para mostrarlo o revelarlo se puede almacenar en una variable de tipo lista.
lista = pickle.load(fichero_binario)
fichero_binario.close()
print(lista)
