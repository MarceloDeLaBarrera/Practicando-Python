"""Ejercicio 5: 
Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber cuánto deberá pagar finalmente por su compra."""

monto = int(input("Ingrese el monto de compra: "))
descuento = monto*0.15
pagar = round(monto-descuento)
print(f"Deberá pagar: {pagar}")
