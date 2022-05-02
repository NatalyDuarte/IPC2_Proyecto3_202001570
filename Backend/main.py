import re
from types import MethodType
from flask import Flask, request, jsonify
from flask_cors import CORS
from xml.etree import ElementTree as ET
from manager import manager

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
            for subelementos in elemento.iter('sentimientos_neutros'):
                for subsubelementos1 in subelementos.iter('palabra'):
                    palabraneutro=subsubelementos1.text
                    manager.agregardiccioneu(palabraneutro)
            for subelemento2 in elemento.iter('empresas_analizar'):
                for subsubelemento2 in subelemento2.iter('nombre'):
                    nombreemp=subsubelemento2.text
                for subsubelemento3 in subelemento2.iter('servicio'):
                    nombreserv=subsubelemento3.attrib['nombre']
                    for subsubsubelemento in subsubelemento3.iter('alias'):
                        alias= subsubsubelemento.text
                        manager.agregarempresa(nombreemp,nombreserv,alias)
    for elemento1 in raiz.iter('lista_mensajes'):
            for subelementop in elemento1.iter('mensaje'):
                mensaje=subelementop.text
                manager.agregarmensaje(mensaje)
    manager.cantimensajes()
    return jsonify({'ok' : True, 'msg':'Archivo leido, y datos creados exitosamente'}), 200

# EJECUTA LA API
if __name__ == '__main__':
    app.run(debug=True, port=5000)