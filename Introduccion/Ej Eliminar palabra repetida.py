frase1 = "hola jose hola señor si quiere chupar tula puede chupar"

# Eliminar palabras sin seguir orden
frase1 = set(frase1.split())
print(frase1)
frase1 = list(frase1)
frase1 = " ".join(frase1)
print(frase1)

# Eliminar y tambien ordenar palabras
paises = "Barcelona, Madrid, España, Cataluña, Ibiza, Madrid, España , Madrid"
lista = [i.strip() for i in paises.split(", ")]
lista = ", ".join(sorted(list(set(lista))))
print(lista)

# Eliminar siguiendo orden:


def eliminar_palabras(frase):
    d = []
    for palabra in frase.split():
        if palabra not in d:
            d.append(palabra)

    new_frase = " ".join(d)
    return new_frase


print(eliminar_palabras(
    "Hola mama te gusta chupar la que cuelga mama yo se que si te gusta"))
