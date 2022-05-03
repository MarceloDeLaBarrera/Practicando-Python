# Sintaxis

# Crear clase
class Coche():

    variable_clase = "Hola"

    # Constructor de la clase
    def __init__(self):
        # Atributos
        self.largo = 0
        self.ancho = 0
        # Anteponer dos guion bajo a la variable permite encapsularla, y evita que el valor de la variable pueda ser modificado desde fuera. Esto tambien se puede hacer a metodos.
        self.__ruedas = 0
        self.__enmarcha = False

    # Metodos
    def arrancar(self, arrancamos):
        # Con self, el metodo recibe por parametro al propio objeto. Self es muy similar al "this" de otros lenguajes.
        self.__enmarcha = arrancamos

        if self.__enmarcha == True:
            chequeo = self.__chequeointerno

        if self.__enmarcha and chequeo:  # ==True
            return "El auto esta en marcha"

        elif self.__enmarcha == True and chequeo == False:
            return "No se puede arrancar, algo ha salido mal en chequeo"

        else:
            return "El auto esta detenido"

        # self.enmarcha=True , y sin usar parametro.

    def __chequeointerno(self):
        self.gasolina = "ok"
        self.puertas = "cerradas"
        if self.gasolina == "ok" and self.puertas == "cerradas":
            return True
        else:
            return False

    # Metodo estatico, no requiere self, no se instancia objeto para ser utilizado, pero luego de ser instanciado, puede utilizarse.
    @staticmethod
    def metodoestatico():
        print(Coche.variable_clase)


# Instanciar la clase, creacion del objeto.
coche1 = Coche()
coche1.largo = 2
print(coche1.largo)
print(coche1.arrancar(False))

# Creando otro objeto
coche2 = Coche()
print(coche2.arrancar(True))
print(coche1.variable_clase)
print(Coche.variable_clase)
Coche.metodoestatico()
coche1.metodoestatico()
