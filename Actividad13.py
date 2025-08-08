from tokenize import maybe


class Repartidor:
    def __init__(self,nombre,paquetes,zona):
        self.nombre = nombre
        self.paquetes = paquetes
        self.zona = zona

    def __str__(self):
        return f"{self.nombre} - {self.paquetes} paquetes - zona: {self.zona}"

class Mensajeria:
    def __init__(self):
        self.repartidores = []

    def AgregarRepartidor(self,repartidor):
        for i in self.repartidores:
            if i.nombre() == repartidor.nombre():
                print("Ya existe. ")
                return
        self.repartidores.append(repartidor)


    def quick_sort(self,lista):
        if len(lista) <=1:
            return lista

        pivote = lista[0]
        menores = [i  for i in  lista[1:] if i.paquetes < pivote.paquetes]
        iguales = [i  for i in  lista[1:] if i.paquetes == pivote.paquetes]
        mayores = [i  for i in  lista[1:] if i.paquetes > pivote.paquetes]
        return  self.quick_sort(menores) + iguales + self.quick_sort(mayores)

    def OrdenarPaquetes(self):
        self.repartidores = self.quick_sort(self.repartidores)

    def BuscarRepartidor(self,nombre):
        for i in self.repartidores:
            if i.nombre.lower() == nombre.lower():
                return i
        return None
    def MostrarRanking(self):
        for i in self.repartidores:
            print(i)

Empresa = Mensajeria()
print("\n*******LOGISTICA EXPRESS*******")
print("----Control de rendimiento----")
cantidad = int(input("Cuantos repartidores desea ingresar: "))
for i in range(cantidad):
    print(f"\nIngrese datos del repartidor {i + 1}: ")
    nombre = input("Nombre: ")
    paquetes = int(input("Paquetes: "))
    zona = input("Zona: ")
    Empresa.AgregarRepartidor(Repartidor(nombre, paquetes, zona))

print("\n****Lista original****")
Empresa.MostrarRanking()

Empresa.OrdenarPaquetes()
print("\n****Ranking****")
Empresa.MostrarRanking()

print("\n***BUSCAR REPARTIDOR***")
Buscado = input("Ingrese el nombre del repartidor que desea buscar: ")
resultado = Empresa.BuscarRepartidor(Buscado)
if resultado:
    print(resultado)
else:
    print("Repartidor no encontrado")