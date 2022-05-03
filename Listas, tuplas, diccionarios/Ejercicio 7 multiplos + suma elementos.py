# Determinar la sumatoria de los multiplos de 3 o de 5 menores que 1000.

lista = []
suma = 0
for i in range(1, 1000):
    if i % 3 == 0 or i % 5 == 0:
        lista.append(i)

for i in lista:
    suma = suma+i
print(suma)
