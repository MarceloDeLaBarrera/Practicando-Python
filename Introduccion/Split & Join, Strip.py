# String a splitear/cortar

problems = "I, have, a, big, problem"
print(problems)


# Se corta un string indicando el caracter de corte, y se guarda cada corte dentro de una lista
p = problems.split(", ")
print(p)

# Sintaxis para unir los elementos de una lista en un string. Lo que va entre comillas seria el "como" se uniran
joined = "-".join(p)
print(joined)

# Strip elimina los caracteres que esten al comienzo y final de la cadena. Ej:
txt = "hola,"
print(txt.strip(","))
