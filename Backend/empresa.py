from servicios import servicios
class Empresa():
    def __init__(self, nombre):
        self.nombre = nombre
        self.servicios = []

    def getNombre (self):
        return self.nombre

    def agregarservicio(self,servicio):
        new= servicios(servicio)
        self.servicios.append(new)
    
    def getServicios(self):
        return self.servicios
