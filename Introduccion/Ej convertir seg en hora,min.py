
def convertir_segundos(s):
    minutos_enteros = s//60
    segundos_resto = s % 60

    horas = minutos_enteros//60
    minutos_resto = minutos_enteros % 60

    return horas, minutos_resto, segundos_resto


h = ""
m = ""
s = ""
segundos = int(input("Ingrese segundos: "))
tiempo = convertir_segundos(segundos)
if tiempo[0] < 9:
    h = "0", str(tiempo[0])
    h = f"{h[0]}{h[1]}"
else:
    h = tiempo[0]

if tiempo[1] < 9:
    m = "0", str(tiempo[1])
    m = f"{m[0]}{m[1]}"
else:
    m = tiempo[1]

if tiempo[2] < 9:
    s = "0", str(tiempo[2])
    s = f"{s[0]}{s[1]}"
else:
    s = tiempo[2]

print(f"Tiempo= {h}:{m}:{s}")
