from django.shortcuts import render, HttpResponse
from .models import Post
from xml.etree import ElementTree as ET
from app.forms import FileForm
from django.http import request, response, FileResponse
from proyecto.settings import PDF_FILES_FOLDER

# Create your views here.
endpoint = 'http://127.0.0.1:5000/'
def app(request):
    blogs = Post.objects.all()
    return render(request,"app/inicio.html",{"blogs":blogs})

def archivocar(request):
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
                ctx['response'] = 'Archivo XML cargado corrrectamente'
            else:
                ctx['response'] = 'El archivo se envio, pero hubo un error en el servidor'
    else:
        return render(request, 'app/archivo.html')
    return render(request, 'app/archivo.html', ctx)

def ayuda(request):
    blogs = Post.objects.all()
    return render(request,"app/ayuda.html",{"blogs":blogs})

def estudiante(request):
    blogs = Post.objects.all()
    return render(request,"app/datos.html",{"blogs":blogs})

def documentacion(request): 
    pdf = open(PDF_FILES_FOLDER +'202001570_Ensayo.pdf', 'rb')
    return FileResponse(pdf)

def peticiones(request):
    blogs = Post.objects.all()
    return render(request,"app/peticiones.html",{"blogs":blogs})