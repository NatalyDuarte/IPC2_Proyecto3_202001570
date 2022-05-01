class negativos():
    def __init__(self, palabra):
        self.palabra= palabra
    
    def getPalabra (self):
        return self.palabra

    def setPalabra (self, palabra):
        return self.palabra == palabra

    def impri(self):
        print("Palabra:" +self.palabra)