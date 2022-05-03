from servicios import servicios
class empresares():
    def __init__(self,nombre, totalmens,mensposi,mensnega,mensneu):
        self.nombre = nombre
        self.totalmens = totalmens
        self.mensposi = mensposi
        self.mensnega = mensnega
        self.mensneu = mensneu
        self.servicios = []

    def getNombre (self):
        return self.nombre

    def agregarservicio(self,servicio,alias):
        new= servicios(servicio)
        self.servicios.append(new)
        new.agregaralias(alias)