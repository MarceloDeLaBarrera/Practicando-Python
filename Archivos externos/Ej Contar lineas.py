txt = open(
    "D:\\Documentos\\Universidad\\Ing en Informatica\\PracticandoPython\\quijote.txt", "r", encoding="utf-8")


lista = txt.readlines()
#textoentero = txt.read()


contador = 1
for linea in lista:
    contador += 1
print(contador)

print(len(lista)+1)


# O tambien se puede hacer directo al archivo txt.
"""
n = 1
for linea in txt:
    n += 1
print(n)

"""

# O recorrer a partir de metodo read.
"""
cont = 1
for caracter in textoentero:
    if caracter == "\n":
        cont += 1

print(cont)
"""
