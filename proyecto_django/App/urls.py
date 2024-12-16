
from django.urls import path
from App import views

urlpatterns = [
    path("", views.inicio, name = "inicio"),
    path("socios/", views.ver_socios, name = "socios"),
    path("actividades/", views.ver_actividades, name = "actividades"),
    path("sucursales/", views.ver_sucursales, name = "sucursales")
]

forms_api = [
    path('socios-formulario/', views.socios_formulario, name='socios_formulario'),
    path('buscar-socio/', views.buscar_socio, name="buscar_socio"),
    path('actividades-formulario/', views.actividades_formulario, name='actividades_formulario'),
    path('sucursales-formulario/', views.sucursales_formulario, name= 'sucursales_formulario'),
    path('buscar-actividades/', views.buscar_actividades, name="buscar_actividades"),
    path('buscar-sucursales/', views.buscar_sucursales, name= 'buscar_sucursales')
]

clases_basadas_vistas = [
    path('socios-lista/', views.SociosListView.as_view(), name = "ListaSocios"),
    path('socios-ver/<pk>/', views.SociosDetailView.as_view(), name= "DetalleSocio"),
    path('socios-nuevo/', views.SociosCreateView.as_view(), name = "NuevoSocio"),
    path('socios-editar/<pk>/', views.SociosUpdateView.as_view(), name = "EditarSocio"),  
    path('socios-borrar/<pk>/', views.SociosDeleteView.as_view(), name = "BorrarSocio")        
]

urlpatterns += forms_api + clases_basadas_vistas