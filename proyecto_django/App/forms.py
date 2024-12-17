from django import forms
from .models import socios,actividades

class SociosForm (forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    dni = forms.CharField()
    email = forms.EmailField()
    telefono = forms.CharField()



class BuscaSocioForm(forms.Form):
    nombre = forms.CharField(required=False, label="Nombre", max_length=100)
    apellido = forms.CharField(required=False, label="Apellido", max_length=100)


class ActividadesForm(forms.Form):
    nombre = forms.CharField()
    horario = forms.TimeField()
    profesor = forms.CharField()
    descripcion = forms.CharField(widget= forms.Textarea)


class SucursalesForm(forms.Form):
    nombre = forms.CharField()
    direccion = forms.CharField()


class BuscarActividades(forms.Form):
    nombre= forms.CharField()


class BuscarSucursales(forms.Form):
    nombre= forms.CharField()


    



