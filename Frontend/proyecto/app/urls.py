from urllib.parse import urlparse
from django.urls import URLPattern, path
from . import views

urlpatterns =[
    path("",views.app, name="app"),
    path("cargar/", views.archivocar, name="cargararchivo"),
]