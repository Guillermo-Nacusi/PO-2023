import csv
from ClaseCliente import Cliente

class manejadorC:
    __listaC: list

def __init__(self):
    self.__listaC = []

def cargarListaC(self):
    archivo = open("clientes.csv")
    reader = csv.reader(archivo, delimiter=";")
    next(reader)
    for fila in reader:
        unCliente = Cliente(fila[0], fila[1], fila[2], fila[3], fila[4], fila[5], fila[6])
        self.__listaC.append(unCliente)
    archivo.close()

def mostrarListaC(self):
    for i in range (len(self.listaC)):
        print("Apellido: {}, Nombre: {}, Dni: {}, Telefono: {}, Patente: {}, Vehiculo: {}, Estado: {}".format(self.__listaC[i].getApellido(), self.__listaC[i].getNombre(), self.__listaC[i].getDni(), self.__listaC[i].getTelefono(), self.__listaC[i].getPatente(), self.__listaC[i].getVehiculo(), self.__listaC[i].getEstado()))

def inciso1(self, dni, reparacion):
    i=0
    while i < len(self.__listaC):
        if self.__getDni() == dni:
            print ("Dni: {}, \tApellido y Nombre: {}".format(self.__listaC[i].getDni(), self.__listaC[i].getAyN()))
            print ("Patente: {}, \tVehiculo: {}".format(self.__listaC[i].getPatente(), self.__listaC[i].getVehiculo()))
            patente = self.__listaC[i].getPatente()
            reparacion.listarPatente(patente)
        i+=1

def Comparar1(self, patente, estado):
    for i in range (len(self.__listaC)):
        if patente == self.__listaC[i].getPatente():
            if self.__listaC[i].getEstado() != estado:
                self.__listaC[i].setEstado(estado)

def Comparar2(self, estado):
    for i in range (len(self.__listaC)):
        if self.__listaC[i].getEstado() == estado:
            print ("Apellido y Nombre: {}, \tTelefono: {}".format(self.__listaC[i].getAyN(), self.__listaC[i].getTelefono()))
            print ("Patente: {}, \tVehiculo: {}".format(self.__listaC[i].getPatente(), self.__listaC[i].getVehiculo()))
            
def inciso4 (self):
    for i in range (len(self.__listaC)-1):
        if self.__listaC[i] == self.listaC[i+1]:
             print ("DNI: {}, Apellido y Nombre: {}, Telefono: {}, Patente: {}, Vehiculo: {}".format(self.__listaC[i].getDni(), self.__listaC[i].getAyN(), self.__listaC[i].getTelefono(), self.__listaC[i].getPatente(), self.__listaC[i].getVehiculo()))

