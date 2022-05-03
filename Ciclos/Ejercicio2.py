# Ingresar mail por teclado y reconocer si lleva un caracter en particular

mail = (input("Ingrese su email: "))
mail = mail.lower()

count = 0
for i in mail:
    if i == "a":
        count += 1
print(f"La cantidad de letras 'a' es de {count}")

# O usando metodo count.

print("El numero de letras 'a' es de", mail.count("a"))
