from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def inicio(request):
    return render(request, "App/inicio.html")

def ver_socios(request):
    return render(request,"App/socios.html")

def ver_actividades(request):
    return render(request,"App/actividades.html")

def ver_sucursales(request):
    return render(request,"App/sucursales.html")

from App.models import socios, actividades, sucursales
from App.forms import SociosForm
from App.forms import ActividadesForm
from App.forms import BuscaSocioForm, SucursalesForm ,BuscarActividades, BuscarSucursales

def socios_formulario(request):
    if request.method == 'POST':
        form = SociosForm(request.POST)

        if form.is_valid():
            informacion = form.cleaned_data

            nuevo_socio = socios(nombre=informacion["nombre"], apellido=informacion["apellido"], dni=informacion["dni"], email=informacion["email"], telefono=informacion["telefono"])
            nuevo_socio.save()

            return render(request, "App/inicio.html")
    else:
        form= SociosForm()

    return render(request, 'App/socios_formulario.html', {'form': form})



def buscar_socio(request):
    if request.method == "POST":
        mi_formulario = BuscaSocioForm(request.POST)  # Aquí recibimos los datos del formulario

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data

            # Buscar socios según los datos ingresados en el formulario
            socios_filtrados = socios.objects.all()

            if informacion.get("nombre"):
                socios_filtrados = socios_filtrados.filter(nombre__icontains=informacion["nombre"])

            if informacion.get("apellido"):
                socios_filtrados = socios_filtrados.filter(apellido__icontains=informacion["apellido"])

            return render(request, "App/mostrar_socios.html", {"socios": socios_filtrados})
    else:
        mi_formulario = BuscaSocioForm()

    return render(request, "App/buscar_socio.html", {"mi_formulario": mi_formulario})


def actividades_formulario(request):
    if request.method == 'POST':
        form = ActividadesForm(request.POST)

        if form.is_valid():
            informacion = form.cleaned_data

            nueva_actividad = actividades(
                nombre=informacion["nombre"], 
                horario=informacion["horario"], 
                profesor=informacion["profesor"], 
                descripcion=informacion["descripcion"]
                )
            nueva_actividad.save()

            return render(request, "App/inicio.html")
    else:
        form= ActividadesForm()

    return render(request, 'App/actividades_formulario.html', {'form': form})


def sucursales_formulario(request):
    if request.method == 'POST':
        form = SucursalesForm(request.POST)

        if form.is_valid():
            informacion = form.cleaned_data

            nueva_sucursal = sucursales(
                nombre=informacion["nombre"], 
                direccion=informacion["direccion"], 
                )
            nueva_sucursal.save()

            return render(request, "App/inicio.html")
    else:
        form= SucursalesForm()

    return render(request, 'App/sucursales_formulario.html', {'form': form})


def buscar_actividades(request):
    if request.method == "POST":
        mi_formulario = BuscarActividades(request.POST)  # Aquí recibimos los datos del formulario

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data

            # Buscar socios según los datos ingresados en el formulario
            actividades_filtrados = actividades.objects.all()

            if informacion.get("nombre"):
                actividades_filtrados = actividades_filtrados.filter(nombre__icontains=informacion["nombre"])


            return render(request, "App/mostrar_actividades.html", {"actividades": actividades_filtrados})
    else:
        mi_formulario = BuscarActividades()

    return render(request, "App/buscar_actividades.html", {"mi_formulario": mi_formulario})


def buscar_sucursales(request):
    if request.method == "POST":
        mi_formulario = BuscarSucursales(request.POST)  # Aquí recibimos los datos del formulario

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data

            # Buscar socios según los datos ingresados en el formulario
            sucursales_filtrados = sucursales.objects.all()

            if informacion.get("nombre"):
                sucursales_filtrados = sucursales_filtrados.filter(nombre__icontains=informacion["nombre"])


            return render(request, "App/mostrar_sucursales.html", {"sucursales": sucursales_filtrados})
    else:
        mi_formulario = BuscarSucursales()

    return render(request, "App/buscar_sucursales.html", {"mi_formulario": mi_formulario})

#vistas basadas en clases 

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


#socios
class SociosListView(LoginRequiredMixin, ListView):
    model = socios
    context_object_name = "socios"
    template_name = "App/socios_lista.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        # Obtener el parámetro de búsqueda desde la URL
        dni = self.request.GET.get('dni', None)
        
        # Si el DNI está presente, filtrar los socios por DNI
        if dni:
            queryset = queryset.filter(dni=dni)
        
        return queryset


class SociosDetailView(LoginRequiredMixin, DetailView):
    model = socios
    template_name = "App/socios_detalle.html"


class SociosCreateView(LoginRequiredMixin, CreateView):
    model = socios
    template_name = "App/socios_crear.html"
    success_url = reverse_lazy("ListaSocios")
    fields = ["nombre", "apellido", "dni", "email", "telefono"]


class SociosUpdateView(LoginRequiredMixin, UpdateView):
    model = socios
    template_name = "App/socios_editar.html"
    success_url = reverse_lazy("ListaSocios")
    fields = ["nombre", "apellido", "dni", "email", "telefono"]


class SociosDeleteView(LoginRequiredMixin, DeleteView):
    model = socios
    template_name = "App/socios_borrar.html"
    success_url = reverse_lazy("ListaSocios")


# actividades

class ActividadesListView(LoginRequiredMixin, ListView):
    model = actividades
    context_object_name = "actividades"
    template_name = "App/actividades_lista.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        # Obtener el parámetro de búsqueda desde la URL (por ejemplo, búsqueda por nombre)
        nombre = self.request.GET.get('nombre', None)
        
        # Si el nombre está presente, filtrar las actividades por nombre
        if nombre:
            queryset = queryset.filter(nombre__icontains=nombre)  # Busca por nombre de forma parcial
        
        return queryset
    
class ActividadesDetailView(LoginRequiredMixin, DetailView):
    model = actividades
    template_name = "App/actividades_detalle.html"


class ActividadesCreateView(LoginRequiredMixin, CreateView):
    model = actividades
    template_name = "App/actividades_crear.html"
    success_url = reverse_lazy("ListaActividades")  
    fields = ["nombre", "horario", "profesor", "descripcion"]  


class ActividadesUpdateView(LoginRequiredMixin, UpdateView):
    model = actividades
    template_name = "App/actividades_editar.html"
    success_url = reverse_lazy("ListaActividades")  
    fields = ["nombre", "horario", "profesor", "descripcion"]  

class ActividadesDeleteView(LoginRequiredMixin, DeleteView):
    model = actividades
    template_name = "App/actividades_borrar.html"
    success_url = reverse_lazy("ListaActividades")

# sucursales 
class SucursalesListView(LoginRequiredMixin, ListView):
    model = sucursales
    context_object_name = "sucursales"
    template_name = "App/sucursales_lista.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        # Obtener el parámetro de búsqueda desde la URL (por ejemplo, búsqueda por nombre)
        nombre = self.request.GET.get('nombre', None)
        
        # Si el nombre está presente, filtrar las sucursales por nombre
        if nombre:
            queryset = queryset.filter(nombre__icontains=nombre)  # Busca por nombre de forma parcial
        
        return queryset
    
class SucursalesDetailView(LoginRequiredMixin, DetailView):
    model = sucursales
    template_name = "App/sucursales_detalle.html"
   


class SucursalesCreateView(LoginRequiredMixin, CreateView):
    model = sucursales
    template_name = "App/sucursales_crear.html"
    success_url = reverse_lazy("ListaSucursales")  
    fields = ["nombre", "direccion"]  


class SucursalesUpdateView(LoginRequiredMixin, UpdateView):
    model = sucursales
    template_name = "App/sucursales_editar.html"
    success_url = reverse_lazy("ListaSucursales")  
    fields = ["nombre", "direccion"]  

class SucursalesDeleteView(LoginRequiredMixin, DeleteView):
    model = sucursales
    template_name = "App/sucursales_borrar.html"
    success_url = reverse_lazy("ListaSucursales")


def about(request):
    return render(request, "App/about.html")



