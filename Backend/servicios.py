class servicios():
    def __init__(self, nombre):
        self.nombre = nombre
        self.alias= []

    def agregaralias(self, alias):
        self.alias.append(alias)