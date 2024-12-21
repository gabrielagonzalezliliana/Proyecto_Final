from django.contrib import admin

# Register your models here.
from App.models import socios, actividades, sucursales


@admin.register(socios)
class sociosAdmin (admin.ModelAdmin):
    list_display = ["id", "nombre", "apellido", "dni", "email", "telefono"]
    ordering = ["apellido"]
    search_fields = ["nombre", "apellido", "dni"]
    list_editable = [ "nombre", "apellido", "dni", "email", "telefono"]
    list_filter = ( "apellido",)


@admin.register(actividades)
class actividadesAdmin (admin.ModelAdmin):
    list_display = [ "id", "nombre", "horario", "profesor", "descripcion"]
    ordering = ["id"]
    search_fields = ["nombre", "profesor"]
    list_editable = [ "nombre", "horario", "profesor", "descripcion"]
    list_filter = ("nombre", "profesor")



@admin.register(sucursales)
class sucursalesAdmin (admin.ModelAdmin):
    list_display = ["id", "nombre", "direccion"]
    ordering = ["id"]
    search_fields = ["nombre", "direccion"]
    list_editable = [ "nombre", "direccion"]
    list_filter = ("nombre",)
