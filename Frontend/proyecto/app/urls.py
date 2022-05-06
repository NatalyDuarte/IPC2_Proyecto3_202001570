from urllib.parse import urlparse
from django.urls import URLPattern, path
from . import views

urlpatterns =[
    path("",views.app, name="app"),
    path("cargar/", views.archivocar, name="cargar"),
    path("ayuda/", views.ayuda, name="ayuda"),
    path("datos/", views.estudiante, name="estudiante"),
    path("docu/", views.documentacion, name="docu"),
    path("peticiones/", views.peticiones, name="peticiones"),
]