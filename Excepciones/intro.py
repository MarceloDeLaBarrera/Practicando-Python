# Son errores que ocurren durante la ejecuccion del programa, inesperadamente sin que hayan errores dentro de la sintaxis del codigo. Al ocurrir una, el resto del programa deja de ejecutarse.
# Lo anterior puede ocurrir por ejemplo, cuando se quiere dividir por 0.

# Para arreglarlo se usa el control de excepciones con try y except.

# Sintaxis.

try:
    pass  # Aca va codigo
except ValueError:  # u otro
    pass  # Aca un print quizas
except ZeroDivisionError:
    pass

# Intenta algo, si no funciona, pasa a la excepcion con codigo de error, e imprime lo que este dentro.

# Tambien se puede usar una excepcion general para no estar colocando muchas excepciones:

try:
    pass
except:
    pass

# Cuando se quiere que una linea de codigo se ejecute siempre, se puede colocar dentro de un "finally"

try:
    pass
except:
    pass
finally:
    pass

# Imprimir las excepciones para saber qué está fallando exactamente en un except:

# Con esto, estamos almacenando el error en la variable e, e imprimiendolo para que se muestre.
try:
    a = float("ayy")
except ValueError as e:
    print(e)
