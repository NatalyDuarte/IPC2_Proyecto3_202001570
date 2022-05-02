from django.http import HttpResponse
from django.shortcuts import render

endpoint ='http://127.0.0.1:5000'
def inicio(request):
    return HttpResponse("Bienvenido")

def home(request):
    return render (request,'C:/Users/Nataly/OneDrive/Documentos/lab IPC2/Proyectoscodigo/IPC2_Proyecto3_202001570/Frontend/Proyecto3/Proyecto3/plantillas/index.html')
