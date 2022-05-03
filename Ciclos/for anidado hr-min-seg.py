import os
import time

# os.system("cls") limpia pantalla
# time.sleep(1) hace que la instruccion anterior dure 1 segundo antes de hacer el os.system("cls")

for hora in range(24):
    for minuto in range(60):
        for segundo in range(60):
            os.system("cls")
            print(f"{hora}:{minuto}:{segundo}")
            time.sleep(1)
