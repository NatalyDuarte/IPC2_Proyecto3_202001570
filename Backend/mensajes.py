class mensajes():
    def __init__(self, lugar,fecha,usuario,redsocial,mensaje):
        self.mensaje= mensaje
        self.lugar = lugar
        self.fecha = fecha
        self.usuario = usuario
        self.redsocial = redsocial
    
    def getmensaje (self):
        return self.mensaje

    def setmensaje (self, mensaje):
        return self.mensaje == mensaje

    def impri(self):
        print("mensaje:" +self.mensaje)