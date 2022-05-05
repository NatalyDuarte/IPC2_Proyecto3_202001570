from django.shortcuts import render, HttpResponse
from .models import Post

# Create your views here.
def app(request):
    blogs = Post.objects.all()
    return render(request,"app/inicio.html",{"blogs":blogs})
