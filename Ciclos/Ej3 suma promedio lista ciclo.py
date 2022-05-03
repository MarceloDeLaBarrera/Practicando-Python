
lista = []

cant = int(input("Ingrese cantidad: "))

for i in range(cant):
    v = int(input(f"Ingrese el valor {i+1}: "))
    lista.append(v)
    # tambien puede ser: v+=v para tener la suma de los 3 valores directamente.

prom = sum(lista)/cant

# round por si solo, redondea a int, si se le añade una coma con un valor, redondea a esa cantidad de decimales.
print(f"El promedio es: {round(prom,2)}")
