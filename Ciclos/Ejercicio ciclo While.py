"""Condicionales + Ciclo While Ejercicio 3: 
Hacer un programa que pida un carácter e indique si es una vocal o no."""

# Ciclo Do While simulacion
while True:
    letra = input("Ingrese un caracter: ").lower()
    largo = len(letra)
    if largo == 1:
        break  # Break rompe el ciclo solo si se cumple la condicion superior.

if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
    print(f"{letra} es una vocal")

else:
    print(f"{letra} es consonante")


# Ciclo While
letra = input("Ingrese un caracter: ").lower()
largo = len(letra)
while largo != 1:
    letra = input("Ingrese un caracter: ").lower()
    largo = len(letra)

if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
    print(f"{letra} es una vocal")

else:
    print(f"{letra} es consonante")
