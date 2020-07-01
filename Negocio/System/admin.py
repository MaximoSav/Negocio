from django.contrib import admin
from System.models import *

#class EntryInLines(admin.TabularInLine):
#   model



# Register your models here.

admin.site.register(Direccion)
admin.site.register(Cliente)
admin.site.register(Venta)
admin.site.register(Producto)
admin.site.register(Categoria)
admin.site.register(Proveedor)
