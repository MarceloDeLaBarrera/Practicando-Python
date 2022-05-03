def three_number_sum(array, suma_objetivo):
    # Paso 1, ordenar arreglo.

    array.sort()
    cumplen_condicion = []

    # Se hace hasta len-2 porque se debe considerar los ultimos dos valores en caso de que toque, para los punteros y asi armar triplete.
    for numero_actual in range(len(array)-2):
        puntero_izquierdo = numero_actual+1
        puntero_derecho = len(array)-1

        # Los punteros se iran moviendo mientras se cumplan las condiciones dentro del ciclo while, hasta que el izquierdo sea mayor al derecho, terminando el primer while.
        # Luego empieza la siguiente vuelta del ciclo for con el segundo valor, y se entra nuevamente al while.
        while puntero_izquierdo < puntero_derecho:
            suma_actual = array[numero_actual] + \
                array[puntero_derecho]+array[puntero_izquierdo]
            if suma_actual == suma_objetivo:
                cumplen_condicion.append(
                    [array[numero_actual], array[puntero_izquierdo], array[puntero_derecho]])
                puntero_izquierdo += 1
                puntero_derecho -= 1
            elif suma_actual < suma_objetivo:
                # Al estar ordenados, se debe mover puntero izquierdo para que de un numero mayor, si se mueve el derecho, daria un numero aun menor.
                puntero_izquierdo += 1
            elif suma_actual > suma_objetivo:
                puntero_derecho -= 1

    return cumplen_condicion


print(three_number_sum([-7, -1, 8, -10, 6, 4, -8, 1, 7], 0))
