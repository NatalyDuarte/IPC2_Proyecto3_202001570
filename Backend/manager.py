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
        self.respuestaposi = []
        self.fecha = []

    def agregardiccioposi(self, palabra):
        new = positivos(palabra)
        self.positivos.append(new)

    def agregardiccionega(self, palabra):
        new = negativos(palabra)
        self.negativos.append(new)

    def agregarempresa(self,nombreemp,nombreserv,alias): 
        newempre= Empresa(nombreemp)
        self.empresas.append(newempre)
        newempre.agregarservicio(nombreserv,alias)
        
    def agregarmensaje(self, mensaje):
        luga=re.findall(r'fecha\s*:\s*[\w,\.]+\s*[,]',mensaje,flags=re.I)
        if len(luga) !=0:
            lugar = luga[0]
            lugar=lugar.replace(":","")
            lugar=lugar.replace("fecha","")
            lugar=lugar.replace(",","")
            lugar=lugar.replace(" ","")
        else: 
            pass
        

        contador=0
        patronfech = "(?:(?:(?:(?:0[1-9]|1[0-9]|2[0-8])[\/](?:0[1-9]|1[012]))|(?:(?:29|30|31)[\/](?:0[13578]|1[02]))|(?:(?:29|30)[\/](?:0[4,6,9]|11)))[\/](?:19|[2-9][0-9])\d\d)|(?:29[\/]02[\/](?:19|[2-9][0-9])(?:00|04|08|12|16|20|24|28|32|36|40|44|48|52|56|60|64|68|72|76|80|84|88|92|96))"
        fechi = re.findall(patronfech,mensaje)
        if len(fechi) !=0:
            fecha = fechi[0]
        else: 
            pass

        usu=re.findall(r'usuario\s*:\s*[\w,^(?!\s)\.\@]+[\s]',mensaje,flags=re.I)
        if len(usu) !=0:
            usuarios = usu[0]
            usuarios= usuarios.replace(":","")
            usuarios=usuarios.replace("usuario","")
            usuarios=usuarios.replace(" ","")
            usuarios=usuarios.replace("red","")
        else: 
            pass
        
        red=re.findall(r'social\s*:\s*[\w,\.]+',mensaje,flags=re.I)
        if len(red) !=0:
            redso = red[0]
            redso= redso.replace(":","")
            redso= redso.replace("social","")
            redso= redso.replace(" ","")
            redso= redso.replace(",","")
        else: 
            pass

        mensa=re.findall(redso+"\s*[\w\s,\.]+",mensaje)
        if len(mensa) !=0:
            mensaj = mensa[0]
            mensaj= mensaj.replace(redso,"")
            mensaj= mensaj.replace(".","")
        else: 
            pass

        new = mensajes(lugar,fecha,usuarios,redso,mensaj)
        self.mensajes.append(new)


        
    def fechas(self):
        for i in self.mensajes:
            if len(self.fecha) !=0:
                v = self.verificarfecha(i.fecha)
                if v == False:
                    self.fecha.append(i.fecha)
            else:
                self.fecha.append(i.fecha)
        self.fecha.sort()
        
    def xmlrespuesta(self):
        raiz = ET.Element("lista_respuestas")
        for i in self.fecha:
            respuesta = ET.SubElement(raiz, "respuesta")
            ET.SubElement(respuesta, "fecha").text = i
            fec=self.cantidadFecha(i)
            mens=ET.SubElement(respuesta, "mensajes")
            ET.SubElement(mens, "total").text=str(fec)
            posi=self.cantidadPosi(i)
            #ET.SubElement(mens, "positivos").text

        filexml = ET.ElementTree(raiz)
        filexml.write("Resultado.xml")

    def verificarfecha(self,fec):
        v = False
        for i in self.fecha:
            if i == fec:
                v = True
        return v

    def cantidadFecha(self,fecha):
        contador = 0
        for i in self.mensajes:
            if i.fecha == fecha:
                contador+=1
        return contador

    def cantidadPosi(self,fecha):
        for i in self.mensajes:
            if i.fecha == fecha:
                if len(self.respuestaposi) !=0:
                    j = self.verificarPosi(i.mensaje)
                    '''
                    if j == False:
                        self.datoNitE.append(i.emisor)
                    '''
                else:
                    self.verificarPosi(i.mensaje)
                   # self.datoNitE.append(i.emisor)
        #return len(self.datoNitE)

    def verificarPosi(self,mensaje):
        contadorposi=0
        for posi in self.positivos:
            resu=re.findall(posi.palabra,mensaje)
            if len(resu)!=0:
                contadorposi +=1
            else:
                pass
        contadornega=0
        for nega in self.negativos:
            resu=re.findall(nega.palabra,mensaje)
            if len(resu)!=0:
                contadornega +=1
            else:
                pass
        if contadorposi>contadornega:
            return contadorposi
        else:
            return 0

        
            
        
