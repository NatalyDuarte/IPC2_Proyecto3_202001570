import re
from types import MethodType
from flask import Flask, request, jsonify
from flask_cors import CORS
from xml.etree import ElementTree as ET
from manager import manager
import webbrowser
app = Flask(__name__)
CORS(app)

manager = manager()

@app.route('/')
def home():
    return '<B><H1>[IPC2]PROYECTO#3</H1></B><br><H3><B>NOMBRE:</B> Nataly Saraí Guzmán Duarte <BR> <B>CARNÉ:</B> 202001570</H3></B> '

@app.route('/add', methods = ['POST'])
def carga():
    xml = request.data.decode('utf-8')
    xml = xml.lower()
    raiz = ET.XML(xml)
    for elemento in raiz.iter('diccionario'):
            for subelemento in elemento.iter('sentimientos_positivos'):
                for subsubelemento in subelemento.iter('palabra'):
                    palabraposi=subsubelemento.text
                    manager.agregardiccioposi(palabraposi)
            for subelemento1 in elemento.iter('sentimientos_negativos'):
                for subsubelemento1 in subelemento1.iter('palabra'):
                    palabranega=subsubelemento1.text
                    manager.agregardiccionega(palabranega)
            for subelemento2 in elemento.iter('empresas_analizar'):
                for subsubelemento2 in subelemento2.iter('empresa'):
                    for subsubelemento22 in subsubelemento2.iter('nombre'):
                        nombreemp=subsubelemento22.text
                        manager.agregarempresa(nombreemp)
                    for subsubelemento33 in subsubelemento2.iter('servicio'):
                        nombreserv=subsubelemento33.attrib['nombre']
                        manager.agregarservicio(nombreserv)
                        for subsubsubelemento in subsubelemento33.iter('alias'):
                            alias= subsubsubelemento.text
                            manager.agregaralias(alias)
                           
    for elemento1 in raiz.iter('lista_mensajes'):
            for subelementop in elemento1.iter('mensaje'):
                mensaje=subelementop.text
                manager.agregarmensaje(mensaje)
    manager.fechas()
    manager.xmlrespuesta()
    v=manager.LeerSalida('Resultado.xml')
    return jsonify({'ok' : True, 'msg':'Archivo leido, y datos creados exitosamente'}), 200

@app.route('/consulta')
def consulta():
    manager.consultaDatos() 
    return jsonify({'ok' : True, 'msg':'Consulta de datos correcta'})

@app.route('/resumenfecha/<fecha>', methods=['GET'])
def resumen(fecha):
    fech=str(fecha).replace("-","/")
    ob=manager.resumenFecha(fech)
    return jsonify({'ok' : True, 'msg':'Todo correcto'})

@app.route('/resumenfecha/<fecha>/<empresa>', methods=['GET'])
def resumenempre(fecha,empresa):
    fech=str(fecha).replace("-","/")
    ob=manager.resumenFechaEmp(fech,empresa)
    return jsonify({'ok' : True, 'msg':'Todo correcto'})

@app.route('/ayudaop1', methods=['GET'])
def ayudaop1():
   return 'NOMBRE:Nataly Saraí Guzmán Duarte \n CARNÉ:202001570'

@app.route('/ayudaop2', methods=['GET'])
def ayudaop2():
   webbrowser.open_new_tab('202001570_Ensayo.pdf')
   return jsonify({'ok' : True, 'msg':'Todo correcto'})


# EJECUTA LA API
if __name__ == '__main__':
    app.run(debug=True, port=5000)