import xml.etree.ElementTree as ET
import re
import json
from servicios import servicios
from positivos import positivos
from negativos import negativos
from mensajes import mensajes
from empresa import Empresa
import webbrowser
import matplotlib 
import matplotlib.pyplot as plt
import numpy as np
from sys import flags
class manager():
    def __init__(self):
        self.positivos = []
        self.negativos = []
        self.empresas = []
        self.mensajes = []
        self.respuestaposi = []
        self.respuestanega = []
        self.respuestaneu = []
        self.fecha = []
        self.contadorempre = 0
        self.contadorservi = 0
        self.mensajeres = []
        self.mensaser = []
        self.cantidadempre = []

    def agregardiccioposi(self, palabra):
        new = positivos(palabra)
        self.positivos.append(new)

    def agregardiccionega(self, palabra):
        new = negativos(palabra)
        self.negativos.append(new)

    def agregarempresa(self,nombreemp): 
        global newempre
        newempre= Empresa(nombreemp)
        self.empresas.append(newempre)

    def agregarservicio(self, nombreserv):
        global newservi
        newservi= servicios(nombreserv)
        newempre.agregarservicio(newservi)

    def agregaralias(self,alias):
        newservi.agregaralias(alias)
        
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
            posi=self.cantidadPosi(i,self.mensajes)
            ET.SubElement(mens, "positivos").text=str(posi)
            nega=self.cantidadNega(i,self.mensajes)
            ET.SubElement(mens, "negativos").text=str(nega)
            neu=self.cantidadNeu(i,self.mensajes)
            ET.SubElement(mens, "neutros").text=str(neu)
            anali=ET.SubElement(respuesta, "analisis")
            nomemp=self.Obempresa(i)
            empre=ET.SubElement(anali,"empresa", nombre=nomemp)
            if nomemp=="No existe":
                mensemp=ET.SubElement(empre, "mensajes")
                ET.SubElement(mensemp, "total").text=str(self.contadorempre)
                if len(self.mensajeres)!=0:         
                    posi1=self.cantidadPosi(i,self.mensajeres)  
                    ET.SubElement(mensemp, "positivos").text=str(0)               
                    nega1=self.cantidadNega(i,self.mensajeres)  
                    ET.SubElement(mensemp, "negativos").text=str(0)                 
                    neu1=self.cantidadNeu(i,self.mensajeres)
                    neu1=posi1+nega1+neu1  
                    ET.SubElement(mensemp, "neutros").text=str(neu1)
            else:
                mensemp=ET.SubElement(empre, "mensajes")
                ET.SubElement(mensemp, "total").text=str(self.contadorempre)
                if len(self.mensajeres)!=0:         
                    posi1=self.cantidadPosi(i,self.mensajeres)  
                    ET.SubElement(mensemp, "positivos").text=str(posi1)               
                    nega1=self.cantidadNega(i,self.mensajeres)  
                    ET.SubElement(mensemp, "negativos").text=str(nega1)                 
                    neu1=self.cantidadNeu(i,self.mensajeres)  
                    ET.SubElement(mensemp, "neutros").text=str(neu1) 
            nomser=self.Obeservi(i)
            servis=ET.SubElement(empre, "servicio", nombre=nomser)
            mensserv=ET.SubElement(servis, "mensajes")
            ET.SubElement(mensserv, "total").text=str(self.contadorservi)
            if len(self.mensaser)!=0:         
                posi2=self.cantidadPosi(i,self.mensaser)  
                ET.SubElement(mensserv, "positivos").text=str(posi2)               
                nega2=self.cantidadNega(i,self.mensaser)  
                ET.SubElement(mensserv, "negativos").text=str(nega2)                 
                neu2=self.cantidadNeu(i,self.mensaser)  
                ET.SubElement(mensserv, "neutros").text=str(neu2) 
        filexml = ET.ElementTree(raiz)
        filexml.write("Resultado.xml",encoding='utf-8')

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

    def Obempresa(self,fecha):
        self.contadorempre=0
        var="No existe"
        for i in self.mensajes:
            if i.fecha == fecha:
                for u in self.empresas:
                    nom=u.nombre
                    nom=nom.replace(",","")
                    nom=nom.replace(";","") 
                    nom=nom.replace(" ","")    
                    nom=nom.replace(".","") 
                    bus=re.findall(nom,i.mensaje)
                    if len(bus)!=0:
                        var=u.nombre
                        self.contadorempre += 1 
                        self.mensajeres.append(mensajes(i.lugar,i.fecha,i.usuario,i.redsocial,i.mensaje))                     
                    else:
                        pass
        return var

    def Obeservi(self,fecha):
        self.contadorempre=0
        var="No existe"
        for i in self.mensajes:
            if i.fecha == fecha:
                for u in self.empresas:
                    servicio=u.getServicios()                
                    for ser in servicio:
                        servi=ser.nombre
                        servi1=servi.nombre
                        servi1=servi1.replace(",","")
                        servi1=servi1.replace(";","") 
                        servi1=servi1.replace(" ","")    
                        servi1=servi1.replace(".","") 
                        resp=re.findall(servi1,i.mensaje)                       
                        if len(resp)!=0:
                            var=servi1
                            self.contadorservi += 1 
                            self.mensaser.append(mensajes(i.lugar,i.fecha,i.usuario,i.redsocial,i.mensaje))                     
                        else:
                            serv=servi.getAlias()
                            for e in serv:
                                resp1=re.findall(e,i.mensaje)
                                if len(resp1)!=0:
                                    var=servi1
                                    self.contadorservi += 1 
                                    self.mensaser.append(mensajes(i.lugar,i.fecha,i.usuario,i.redsocial,i.mensaje))                     
                                else:
                                    pass

        return var
        

    def cantidadPosi(self,fecha,arreglo):
        self.respuestaposi = []
        self.respuestanega = []
        self.respuestaneu = []
        for i in arreglo:
            if i.fecha == fecha:
                j = self.verificarPosi(i.mensaje)
                if j == True:
                    self.respuestaposi.append(i.mensaje)
        return len(self.respuestaposi)

    def verificarPosi(self,mensaje):
        contadorposi=0
        for posi in self.positivos:
            pala=posi.palabra
            pala=pala.replace(",","")
            pala=pala.replace(";","") 
            pala=pala.replace(" ","")    
            pala=pala.replace(".","") 
            resu=re.findall(pala,mensaje)
            if len(resu)!=0:
                contadorposi +=1
            else:
                pass
        contadornega=0
        for nega in self.negativos:
            neg=nega.palabra
            neg=neg.replace(",","")
            neg=neg.replace(";","") 
            neg=neg.replace(" ","")    
            neg=neg.replace(".","") 
            resus=re.findall(neg,mensaje)
            if len(resus)!=0:
                contadornega +=1
            else:
                pass
        if contadorposi>contadornega:
            return True
        else:
            return False

    def cantidadNega(self,fecha,arreglo):
        self.respuestaposi = []
        self.respuestanega = []
        self.respuestaneu = []
        for i in arreglo:
            if i.fecha == fecha:
                j = self.verificarNega(i.mensaje)
                if j == True:
                    self.respuestanega.append(i.mensaje)
        return len(self.respuestanega)

    def verificarNega(self,mensaje):
        contadorposi=0
        contadornega=0
        for posi in self.positivos:   
            pala=posi.palabra
            pala=pala.replace(",","")
            pala=pala.replace(";","") 
            pala=pala.replace(" ","")    
            pala=pala.replace(".","")                          
            resu=re.findall(pala,mensaje)
            if len(resu)!=0:
                contadorposi +=1
            else:
                pass       
        for nega in self.negativos:
            neg=nega.palabra
            neg=neg.replace(",","")
            neg=neg.replace(";","") 
            neg=neg.replace(" ","")    
            neg=neg.replace(".","") 
            resus=re.findall(neg,mensaje)
            if len(resus)!=0:
                contadornega +=1
            else:
                pass
        if contadorposi<contadornega:
            return True
        else:
            return False

    def cantidadNeu(self,fecha,arreglo):
        self.respuestaposi = []
        self.respuestanega = []
        self.respuestaneu = []
        for i in arreglo:
            if i.fecha == fecha:
                j = self.verificarNeu(i.mensaje)
                if j == True:
                    self.respuestaneu.append(i.mensaje)
        return len(self.respuestaneu)

    def verificarNeu(self,mensaje):
        contadorposi=0
        for posi in self.positivos:
            pala=posi.palabra
            pala=pala.replace(",","")
            pala=pala.replace(";","") 
            pala=pala.replace(" ","")    
            pala=pala.replace(".","") 
            resu=re.findall(pala,mensaje)
            if len(resu)!=0:
                contadorposi +=1
            else:
                pass
        contadornega=0
        for nega in self.negativos:
            neg=nega.palabra
            neg=neg.replace(",","")
            neg=neg.replace(";","") 
            neg=neg.replace(" ","")    
            neg=neg.replace(".","") 
            resus=re.findall(neg,mensaje)
            if len(resus)!=0:
                contadornega +=1
            else:
                pass
        if contadorposi==contadornega:
            return True
        elif contadorposi==0 and contadornega==0:
            return True
        else:
            return False
    
    def consultaDatos(self):
        ruta ="Backend/Resultado.xml"
        #valor = self.LeerSalida(ruta)
        webbrowser.open_new_tab('Resultado.xml')

    def LeerSalida(self, objeto) -> str:
        tree = ET.parse(objeto)
        raiz = tree.getroot()
        r = ET.tostring(raiz, encoding='unicode', method='xml')
        return r
    
    def resumenFecha(self,fecha):
        total=0
        positivos=0
        negativos=0
        neutros=0
        tree = ET.parse('Resultado.xml')
        raiz = tree.getroot()
        for elemento in raiz.iter('respuesta'):
            for subelemento in elemento.iter('fecha'):
                fech = subelemento.text
                if fech==fecha:
                    for subselemento in elemento.iter('mensajes'):
                        for ele in subselemento.iter('total'):
                            total = ele.text
                        for ele1 in subselemento.iter('positivos'):
                            positivos= ele1.text
                        for ele2 in subselemento.iter('negativos'):
                            negativos= ele2.text
                        for ele3 in subselemento.iter('neutros'):
                            neutros= ele3.text
                else:
                    pass
        if total!=0:
            arrex=[]
            labels=[]
            labels.append("positivos")
            labels.append("negativos")
            labels.append("neutros")
            arrex.append(float(positivos))
            arrex.append(float(negativos))
            arrex.append(float(neutros))
            colors = plt.get_cmap('Greens')(np.linspace(0.2, 0.7, len(arrex)))
            fig, ax = plt.subplots()
            ax.pie(arrex, colors=colors,labels=labels,autopct=("%1.f%%"))
            #ax.set(xlim=(0, 8), xticks=np.arange(1, 8),ylim=(0, 8), yticks=np.arange(1, 8))
            ax.axis('equal')
            plt.title("Grafica por fecha")
            plt.text(0,0.3,"Total: "+total,fontsize=14)
            plt.text(0,0.2,"Positivos: "+positivos,fontsize=14)
            plt.text(0,0.1,"Negativos: "+negativos,fontsize=14)
            plt.text(0,0,"Neutros: "+neutros,fontsize=14)
            plt.legend()
            plt.savefig("Graficaporfecha.png")
            print("Imagen generada exitosamente")
        else:
            pass
    
    def resumenFechaEmp(self,fecha,empresa):
        total=0
        positivos=0
        negativos=0
        neutros=0
        total1=0
        positivos1=0
        negativos1=0
        neutros1=0
        tree = ET.parse('Resultado.xml')
        raiz = tree.getroot()
        for elemento in raiz.iter('respuesta'):
            for subelemento in elemento.iter('fecha'):
                fech = subelemento.text
                if fech==fecha:
                    for subselemento in elemento.iter('mensajes'):
                        for ele in subselemento.iter('total'):
                            total = ele.text
                        for ele1 in subselemento.iter('positivos'):
                            positivos= ele1.text
                        for ele2 in subselemento.iter('negativos'):
                            negativos= ele2.text
                        for ele3 in subselemento.iter('neutros'):
                            neutros= ele3.text
                    for subselemento1 in elemento.iter('analisis'):
                        for elee in subselemento1.iter('empresa'):
                            nombreempre=elee.attrib['nombre']
                            nombreempre=nombreempre.replace(" ","")
                        if nombreempre == empresa:
                            for elem in subselemento1.iter('mensajes'):
                                for elee11 in elem.iter('total'):
                                    total1= elee11.text
                                for elee1 in elem.iter('positivos'):
                                    positivos1= elee1.text
                                for elee2 in elem.iter('negativos'):
                                    negativos1= elee2.text
                                for elee3 in elem.iter('neutros'):
                                    neutros1= elee3.text
                        else:
                            pass
                else:
                    pass
        if total!=0:
            if total1!=0:
                arrex=[]
                labels=[]
                labels.append("positivos")
                labels.append("negativos")
                labels.append("neutros")
                arrex.append(float(positivos1))
                arrex.append(float(negativos1))
                arrex.append(float(neutros1))
                colors = plt.get_cmap('Oranges')(np.linspace(0.2, 0.7, len(arrex)))
                fig, ax = plt.subplots()
                ax.pie(arrex, colors=colors,labels=labels,autopct=("%1.f%%"))
                #ax.set(xlim=(0, 8), xticks=np.arange(1, 8),ylim=(0, 8), yticks=np.arange(1, 8))
                ax.axis('equal')
                plt.title("Grafica por fecha y empresa")
                plt.text(0,0.3,"Total: "+total1,fontsize=14)
                plt.text(0,0.2,"Positivos: "+positivos1,fontsize=14)
                plt.text(0,0.1,"Negativos: "+negativos1,fontsize=14)
                plt.text(0,0,"Neutros: "+neutros1,fontsize=14)
                plt.legend()
                plt.savefig("GraficaporfechaEmp.png")
                print("Imagen generada exitosamente")
            else:
                pass
        else:
            pass