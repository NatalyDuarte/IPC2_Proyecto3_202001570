class mensajes():
    def __init__(self, mensaje):
        self.mensaje= mensaje
    
    def getmensaje (self):
        return self.mensaje

    def setmensaje (self, mensaje):
        return self.mensaje == mensaje

    def impri(self):
        print("mensaje:" +self.mensaje)