# [::-1] --> Desde el principio, hasta el final, con salto -1

capicuas = []
for numero in range(1, 500):
    cadena = str(numero)
    reverso = cadena[::-1]
    if cadena == reverso:
        capicuas.append(cadena)

print(capicuas)
