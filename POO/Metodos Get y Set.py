
class Cuenta():
    # Constructor
    def __init__(self, pro, sal, mon):
        self.__propietario = pro
        self.__salario = sal
        self.__moneda = mon

    # Metodos Get y Set sirven para leer y modificar propiedades dentro de una clase, que pudieran estar encapsuladas.

    # Con property se puede acceder al metodo GET como si fuera un atributo, por lo cual al hacerle un print se llama como atributo y no como metodo.
    @property
    def gs_propietario(self):
        return self.__propietario

    def getSaldo(self):
        return self.__salario

    def getMoneda(self):
        return self.__moneda

    def setMoneda(self, mone):
        self.__moneda = mone

    # Con .setter se puede acceder al metodo set como si fuera atributo... Requiere tener mismo nombre del metodo get.
    @gs_propietario.setter
    def gs_propietario(self, prop):
        self.__propietario = prop


nombre = input("Ingrese su nombre:")
saldo = int(input("Ingrese saldo: "))
moneda = input("Ingrese moneda: ")
cuenta1 = Cuenta(nombre, saldo, moneda)
# cuenta1.__moneda Esta instruccion arrojaria error ya que no se puede acceder al atributo al estar encapsulado.

# Llamada al metodo gs_propietario como atributo gracias a property
print(cuenta1.gs_propietario)
print(cuenta1.getSaldo())
print(cuenta1.getMoneda())
cuenta1.setMoneda("Dolares")
print(cuenta1.getMoneda())
cuenta1.gs_propietario = "Ratoon"
print(cuenta1.gs_propietario)
