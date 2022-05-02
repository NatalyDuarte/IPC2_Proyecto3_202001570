import xml.etree.ElementTree as ET
import re
import json
from servicios import servicios
from positivos import positivos
from negativos import negativos
from neutros import neutros
from mensajes import mensajes
from empresa import empresa
from alias import alias
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

    def agregarempresa(self,nombreemp,nombreserv,alias):
        newempre = alias(alias)
        newempre1= servicios(nombreserv,newempre)
        newempre2= empresa(nombreemp,newempre1)
        self.empresas.append(newempre2)

    def agregarmensaje(self, mensaje):
        new = mensajes(mensaje)
        self.mensajes.append(new)