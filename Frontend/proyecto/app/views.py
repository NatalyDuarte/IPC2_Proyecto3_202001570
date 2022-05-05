from django.shortcuts import render, HttpResponse
from .models import Post
from xml.etree import ElementTree as ET
from app.forms import FileForm

# Create your views here.
endpoint = 'http://127.0.0.1:5000/'
def app(request):
    blogs = Post.objects.all()
    return render(request,"app/inicio.html",{"blogs":blogs})

def cargaMasiva(request):
    ctx = {
        'content':None,
        'response':None
    }
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            f = request.FILES['file']
            xml_binary = f.read()
            xml = xml_binary.decode('utf-8')
            ctx['content'] = xml
            response = request.post(endpoint + 'add', data=xml_binary)
            if response.ok:
                raiz = ET.parse("../Backend/Resultado.xml")
                raiz=raiz.getroot()
                cadenaXML = ET.tostring(raiz, encoding='unicode', method='xml')
                ctx['response'] = cadenaXML
            else:
                ctx['response'] = 'El archivo se envio, pero hubo un error en el servidor'
    else:
        return render(request, 'app/index.html')
    return render(request, 'app/index.html', ctx)
