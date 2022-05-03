# Para ver documentación, se utiliza  help o __doc__ y se le pasa como parametro la funcion de la que se desea ver la documentacion... Para documentar se usa triple comilla.
"""
help(funcion)
print(f"Funcion Eliminar Cursos: {funcion.__doc__}")
help(clase.funcion)

"""

# Modulo doctest permite hacer pruebas de una funcion o una parte del codigo, sin tener que ejecutar todo el codigo.

import doctest
doctest.testmod()
