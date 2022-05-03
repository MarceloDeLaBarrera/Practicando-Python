def diferencia_minima(array):
    array.sort()
    diferencia_minima = array[1]-array[0]
    pares = []
    a = 0
    b = 0
    for element in array:
        for otherelement in array[::-1]:
            diferencia_actual = element-otherelement
            if diferencia_actual < 0:
                diferencia_actual = diferencia_actual*-1
                if diferencia_actual < diferencia_minima:
                    pares = []

                if diferencia_actual <= diferencia_minima:
                    a = element
                    b = otherelement
                    pares.append([a, b])
                    diferencia_minima = diferencia_actual
            # Si se quiere capturar todos los pares, incluidos inversos, añadir:
            """
            elif diferencia_actual > 0:
                if diferencia_actual < diferencia_minima:
                    pares = []

                if diferencia_actual <= diferencia_minima:
                    a = element
                    b = otherelement
                    pares.append([a, b])
                    diferencia_minima = diferencia_actual
            """
    return pares


print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
print(diferencia_minima([6, 2, 4, 10]))
print(diferencia_minima([3, 8, 30, 2, 20, 10, 5, 15, 21, 31]))
print(diferencia_minima([8, 30, 2, 20, 10, 5, 15, 21, 31]))
print(diferencia_minima([10, 20, 30, 40, 50, 60, 55, 65]))


def diferencia_minima2(array):
    array.sort()
    diferencia_minima = array[1]-array[0]
    resultado = []
    for i in range(len(array)-1):
        diferencia_actual = array[i+1] - array[i]
        if diferencia_actual < diferencia_minima:
            resultado = []
        if(diferencia_actual <= diferencia_minima):
            resultado.append([array[i], array[i+1]])
            diferencia_minima = diferencia_actual
    return resultado


print(diferencia_minima2([6, 2, 4, 10]))
print(diferencia_minima2([3, 8, 30, 2, 20, 10, 5, 15, 21, 31]))
print(diferencia_minima2([8, 30, 2, 20, 10, 5, 15, 21, 31]))
print(diferencia_minima([10, 20, 30, 40, 50, 60, 55, 65]))
