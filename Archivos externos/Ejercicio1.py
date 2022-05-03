class fichero():

    # Constructor
    def __init__(self, ruta):
        self.ruta = ruta

    # Metodos

    def readd(self):

        txt = open(self.ruta, "r")
        texto = txt.read()
        txt.close()
        return texto

    def writee(self, frase):
        self.frase = frase
        txt = open(self.ruta, "w")
        txt.write(self.frase)
        txt.close()
