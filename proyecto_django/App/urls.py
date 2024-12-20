
from django.urls import path
from App import views

urlpatterns = [
    path("", views.inicio, name = "inicio"),
    path("socios/", views.ver_socios, name = "socios"),
    path("actividades/", views.ver_actividades, name = "actividades"),
    path("sucursales/", views.ver_sucursales, name = "sucursales"),
    path("about/", views.about, name="about")
]


clases_basadas_vistas = [
    path('socios-lista/', views.SociosListView.as_view(), name = "ListaSocios"),
    path('socios-ver/<pk>/', views.SociosDetailView.as_view(), name= "DetalleSocio"),
    path('socios-nuevo/', views.SociosCreateView.as_view(), name = "NuevoSocio"),
    path('socios-editar/<pk>/', views.SociosUpdateView.as_view(), name = "EditarSocio"),  
    path('socios-borrar/<pk>/', views.SociosDeleteView.as_view(), name = "BorrarSocio"),
    path('actividades-lista/', views.ActividadesListView.as_view(), name = "ListaActividades"),
    path('actividades-ver/<pk>/', views.ActividadesDetailView.as_view(), name= "DetalleActividad"),
    path('actividades-nuevo/', views.ActividadesCreateView.as_view(), name = "NuevaActividad"),
    path('actividades-editar/<pk>/', views.ActividadesUpdateView.as_view(), name = "EditarActividad"),  
    path('actividades-borrar/<pk>/', views.ActividadesDeleteView.as_view(), name = "BorrarActividad"),
    path('sucursales-lista/', views.SucursalesListView.as_view(), name = "ListaSucursales"),
    path('sucursales-ver/<pk>/', views.SucursalesDetailView.as_view(), name= "DetalleSucursal"),
    path('sucursales-nuevo/', views.SucursalesCreateView.as_view(), name = "NuevaSucursal"),
    path('sucursales-editar/<pk>/', views.SucursalesUpdateView.as_view(), name = "EditarSucursal"),  
    path('sucursales-borrar/<pk>/', views.SucursalesDeleteView.as_view(), name = "BorrarSucursal")
]

urlpatterns += clases_basadas_vistas