import xml.etree.ElementTree as ET
import re
import json
from positivos import positivos
from negativos import negativos
from neutros import neutros
from mensajes import mensajes
class manager():
    def __init__(self):
        self.positivos = []
        self.negativos = []
        self.neutros = []
        self.empresas = []
        self.mensajes = []
    
    def agregardiccioposi(self, palabra):
        new = positivos(palabra)
        self.positivos.append(new)

    def agregardiccionega(self, palabra):
        new = negativos(palabra)
        self.negativos.append(new)

    def agregardiccioneu(self, palabra):
        new = neutros(palabra)
        self.neutros.append(new)

    def agregarempresa(self,)

    def agregarmensaje(self, mensaje):
        new = mensajes(mensaje)
        self.mensajes.append(new)