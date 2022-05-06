from django.shortcuts import render, HttpResponse
from .models import Post
from xml.etree import ElementTree as ET
from app.forms import FileForm

# Create your views here.
endpoint = 'http://127.0.0.1:5000/'
def app(request):
    blogs = Post.objects.all()
    return render(request,"app/inicio.html",{"blogs":blogs})

def archivocar(request):
    blogs = Post.objects.all()
    return render(request,"app/archivo.html",{"blogs":blogs})