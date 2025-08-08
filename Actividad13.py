from tokenize import maybe


class Repartidor:
    def __init__(self,nombre,paquetes,zona):
        self.nombre = nombre
        self.paquetes = paquetes
        self.zona = zona

    def __str__(self):
        return f"{self.nombre} - {self.paquetes} - zona: {self.zona}"

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
        self.repartidores