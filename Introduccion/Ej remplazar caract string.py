# Programa que recoge todas las palabras de un texto y las almacena en una lista, escluyendo comas, puntos, espacios.

texto = "Hola. Me gusta comer pizza,    todas las mañanas!. Si quieres mas, chupa la que cuelga."
quitar = ",;:.\n!\"'"

for caracter in quitar:
    texto = texto.replace(caracter, "")
print(texto)

l = texto.split(" ")
print(l)

copial = list(l)
for letra in copial:
    if letra == "":
        l.remove(letra)
print(l)
