from ManejadorClientes import manejadorC
from ManejadorReparaciones import manejadorR


if __name__ == "__main__":
    cliente = manejadorC()
    reparacion = manejadorR()
    cliente.cargarListaC()
    reparacion.cargaListaR()
    print("Listado  cliente")
    cliente.mostrarListaC()
    print("Listado reparaciones")
    reparacion.mostrarListaR()
    print("INCISO 1\n")
    dni = input("Ingrese dni\n")
    cliente.inciso1(dni, reparacion)
    print ("INCISO 2\n")
    patente = input("Ingrese una patente\n")
    reparacion.inciso2(patente, cliente)
    print ("INCISO 3\n")
    reparacion.inciso3(cliente)
    print ("INCISO 4\n")
    cliente.inciso4()




