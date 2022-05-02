import xml.etree.ElementTree as ET
import re
import json
from servicios import servicios
from positivos import positivos
from negativos import negativos
from neutros import neutros
from mensajes import mensajes
from empresa import Empresa
class manager():
    def __init__(self):
        self.positivos = []
        self.negativos = []
        self.neutros = []
        self.empresas = []
        self.mensajes = []
        self.contador = 0
        self.contamensajes = 0

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
        newempre= Empresa(nombreemp)
        self.empresas.append(newempre)
        newempre.agregarservicio(nombreserv,alias)
        
    def agregarmensaje(self, mensaje):
        contador=0
        patronfech = "(?:(?:(?:(?:0[1-9]|1[0-9]|2[0-8])[\/](?:0[1-9]|1[012]))|(?:(?:29|30|31)[\/](?:0[13578]|1[02]))|(?:(?:29|30)[\/](?:0[4,6,9]|11)))[\/](?:19|[2-9][0-9])\d\d)|(?:29[\/]02[\/](?:19|[2-9][0-9])(?:00|04|08|12|16|20|24|28|32|36|40|44|48|52|56|60|64|68|72|76|80|84|88|92|96))"
        fechi = re.findall(patronfech,mensaje)
        if len(fechi) !=0:
            fecha = fechi[0]
        else: 
            pass
        for posi in self.positivos:
            palabra = re.findall(posi.palabra,mensaje)
            for pala in palabra:
                if pala == posi.palabra: 
                    contador +=1
                    self.contador +=1
        new = mensajes(mensaje)
        self.mensajes.append(new)
        
    def cantimensajes(self):
        self.contamensajes= len(self.mensajes)
        print(self.contamensajes)