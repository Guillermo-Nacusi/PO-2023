import csv
from ClaseReparacion import Reparacion

class manejadorR:
    __listaR: list
    
    def __init__(self):
        self.__listaR = []
    
    def cargaListaR(self):
        archivo= open("reparaciones.csv")
        reader= csv.reader(archivo, delimiter=";")
        next (reader)
        for fila in reader:
            unaReparacion = Reparacion(fila[0], fila[1], int( fila[2]), int(fila[3]), fila[4])
            self.__listaR.append(unaReparacion)
        archivo.close()
    
    def mostrarListaR(self):
        i=0
        for i in range (len(self.__listaR)):
            print("Patente: {}, Reparacion: {}, PrecioRepuesto: {}, PrecioManodeObra: {}, Estado: {}".format(self.__listaR[i].getPat(),self.__listaR[i].getReparacion(), self.__listaR[i].getPrecioRepuesto(), self.__listaR[i].getPrecioManodeObra(), self.__listaR[i].getEst()))
   
    def listarPatente(self, patente):
        subtotal= 0
        acum= 0
        for i in range (len(self.__listaR)):
           if patente == self.__listaR[i].getPat():
            subtotal = self.__listaR[i].getPrecioRepuesto() + self.__listaR[i].getPrecioManodeObra()
            acum+= subtotal
            print("Reparacion: {}, \tPrecio Repuesto: {}, \t\tPrecio Mano de Obra: {}, \t\t\tSubtotal: {}".format(self.__listaR[i].getReparacion(), self.__listaR[i].getPrecioRepuesto(), self.__listaR[i].getPrecioManodeObra(), subtotal, acum))
        print ("\t\t\t\tTotal a Pagar: {}".format(acum))
    
    def insciso2 (self, patente, cliente):
        i=0
        while i < len(self.__listaR):
            if patente == self.__listaR[i].getPat():
                if self.__listaR[i].getEst() == "T":
                    est = self.__listaR[i].getEst()
                    cliente.Comparar(patente, est)
            i+=1

    def inciso3 (self, cliente):
        for i in range (len(self.__listaR)):
             if self.__listaR[i].getEst() == "P":
                estado = self.__listaR[i].getEst()
                cliente.Comparar2(estado)
                print ("Reparacion: {}".format(self.__listaR[i].getReparacion()))
