# Marcelo De La Barrera

def contador(limite):
    for i in range(1, limite+1):
        if i % 2 == 0:
            print("pan")
        if i % 3 == 0:
            print("tu")
        if i % 3 == 0 and i % 2 == 0:
            print("fla")


contador(100)


# A= Conductor
# B= Pasajero 1
# C= Pasajero 2
A = [1, 1]
B = [5, 3]
C = [3, 4]


def calcular_distancia(conductorA, pasajeroB, pasajeroC):

    distancia_AyB = ((pasajeroB[0]-conductorA[0]) **
                     2 + (pasajeroB[1]-conductorA[1])**2)**0.5
    distancia_AyC = ((pasajeroC[0]-conductorA[0]) **
                     2 + (pasajeroC[1]-conductorA[1])**2)**0.5

    if distancia_AyB > distancia_AyC:
        print(
            f"El pasajero mas cercano es el pasajero es C, y se encuentra a una distancia de {distancia_AyC}")
    elif distancia_AyB < distancia_AyC:
        print(
            f"El pasajero mas cercano es el pasajero es B, y se encuentra a una distancia de {distancia_AyB}")

    else:
        print(
            f"Ambos pasajeros estan a la misma distancia y dicha distancia es {distancia_AyC}.")


calcular_distancia(A, B, C)


def calcular_distancia2(A, B, C):
    # A= Conductor /  B= Pasajero 1  /  C= Pasajero 2
    up1 = left1 = right1 = down1 = up2 = left2 = right2 = down2 = 0
    if B[1] > A[1]:
        up1 = B[1]-A[1]
    if B[0] > A[0]:
        right1 = B[0]-A[0]
    if B[1] < A[1]:
        down1 = A[1]-B[1]
    if B[0] < A[0]:
        left1 = A[0]-B[0]
    if C[1] > A[1]:
        up2 = C[1]-A[1]
    if C[0] > A[0]:
        right2 = C[0]-A[0]
    if C[1] < A[1]:
        down2 = A[1]-C[1]
    if C[0] < A[0]:
        left2 = A[0]-C[0]

    distanciaAyB = up1+left1+right1+down1
    distanciaAyC = up2+left2+right2+down2

    if distanciaAyB > distanciaAyC:
        print(
            f"El pasajero mas cercano es el pasajero es C, y se encuentra a una distancia de {distanciaAyC}")
    elif distanciaAyB < distanciaAyC:
        print(
            f"El pasajero mas cercano es el pasajero es B, y se encuentra a una distancia de {distanciaAyB}")
    else:
        print(
            f"Ambos pasajeros estan a la misma distancia y dicha distancia es {distanciaAyC}.")


calcular_distancia2(A, B, C)


# Suponemos carrera 100 metros. Y en un solo plano, ya que no se especifica.

def Carrera(liebre_a_posicion, liebre_a_velocidad, liebre_b_posición, liebre_b_velocidad):
    meta = 100
    puntoDeEncuentro = 0
    se_encontraron = False

    for i in range(1, meta):
        liebre_a_posicion += liebre_a_velocidad
        liebre_b_posición += liebre_b_velocidad
        print(liebre_a_posicion)
        print(liebre_b_posición)

        if liebre_a_posicion == liebre_b_posición:
            puntoDeEncuentro = liebre_a_posicion
            se_encontraron = True
            print(
                f"Ambas liebres se encuentran a los {puntoDeEncuentro} metros")

        if liebre_a_posicion >= meta and se_encontraron != False:
            print(
                f"Liebre A gana la carrera y ambas liebres se encuentran a los {puntoDeEncuentro} metros.")
            break

        elif liebre_b_posición >= meta and se_encontraron != False:
            print(
                f"Liebre B gana la carrera y se encuentran a los {puntoDeEncuentro} metros.")
            break

        elif liebre_a_posicion >= meta and se_encontraron == False:
            print(f"Liebre A gana la carrera y no se encontraron")
            break

        elif liebre_b_posición >= meta and se_encontraron == False:
            print(f"Liebre B gana la carrera y no se encontraron")
            break


Carrera(0, 5, 9, 2)
