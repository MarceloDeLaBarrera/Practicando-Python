# random permite generar cosas aleatorias

import random
from werkzeug.security import generate_password_hash

minus = "abcdefghijklmnopqrstuvwxyz"
mayus = minus.upper()
numeros = "1234567890"
simbolos = "@()[]{}*.,;/-_¿?.¡!$<>#&+%="
base = minus+mayus+numeros+simbolos
longitud_pass = 12

# Sample se refiere a la muestra que ha de generarse de forma aleatoria, y toma como parametros lo que se usara como muestra y la longitud que tendra la misma. Almacena cada valor segun longitud en una lista.
# generate_password_hash permite permite encriptar un string en sha256 gracias al paquete werkzeug.


def genera_password():
    muestra = random.sample(base, longitud_pass)
    password = "".join(muestra)
    pass_encriptado = generate_password_hash(password)
    print(pass_encriptado)


for i in range(1, 11):
    genera_password()
