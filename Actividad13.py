class Repartidor:
    def __init__(self,nombre,paquetes,zona):
        self.nombre = nombre
        self.paquetes = paquetes
        self.zona = zona

    def __str__(self):
        return f"{self.nombre} - {self.paquetes} - zona: {self.zona}"

