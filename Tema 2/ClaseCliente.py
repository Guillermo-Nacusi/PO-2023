class Cliente:
    __dni = ""
    __apellido = ""
    __nombre = ""
    __telefono = ""
    __patente = ""
    __vehiculo= ""
    __estado = ""
    
    def __init__(self, dni, ape, nom, tel, pat, veh, est):
        self.__dni = dni
        self.__apellido = ape
        self.__nombre= nom
        self.__telefono = tel
        self.__patente = pat
        self.__vehiculo= veh
        self.__estado = est

    
    def getDni(self):
        return self.__dni
    def getApellido(self):
        return self.__apellido
    def getNombre(self):
        return self.__nombre
    def getTelefono(self):
        return self.__telefono
    def getPatente(self):
        return self.__patente
    def getVehiculo(self):
        return self.__vehiculo
    def getEstado(self):
        return self.__estado
    def getAyN(self):
        return self.__apellido + " " + self.__nombre
    def setEstado(self, estado):
        self.__estado = estado
        return self.__estado
    
    def __eq__ (self, otro):
        return (self.__dni == otro.__dni) and (self.getAyN() == otro.getAyN()) and (self.__telefono == otro.__telefono)
    
    def setEstado(self, estado):
        self.__estado = estado
        return self.__estado