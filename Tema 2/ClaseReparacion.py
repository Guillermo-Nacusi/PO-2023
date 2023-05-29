class Reparacion:
    __patente = ""
    __reparacion = ""
    __precioRepuesto = 0
    __precioManodeObra = 0
    __estado = ""
    
    def __init__(self, pat, rep, price, precio, est):
        self.__patente = pat
        self.__reparacion = rep
        self.__precioRepuesto= price
        self.__precioManodeObra = precio
        self.__estado = est
    
    def getPat(self):
        return self.__patente
    def getReparacion(self):
        return self.__reparacion
    def getPrecioRepuesto(self):
        return self.__precioRepuesto
    def getPrecioManodeObra(self):
        return self.__precioManodeObra
    def getEst(self):
        return self.__estado
    