from django.contrib import admin

# Register your models here.
from App.models import socios, actividades, sucursales

admin.site.register(socios)
admin.site.register(actividades)
admin.site.register(sucursales)