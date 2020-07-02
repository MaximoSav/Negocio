from django.contrib import admin
from System.models import *

class ClienteSup(admin.ModelAdmin):
    class EntryInLines(admin.TabularInline):
        model = Venta
    inlines = [EntryInLines,]
    list_display = ['RUT', 'nombre', 'telefono']

class ProveedorSup(admin.ModelAdmin):
    class EntryInLines(admin.TabularInline):
        model = Producto
    inlines = [EntryInLines,] 
    list_filter = ['nombre', 'RUT',]

class ProductoSup(admin.ModelAdmin):    
    fieldsets = (
        ('Descripcion', {
            'fields': ('RUT', 'nombre')
        }),
        ('Variables', {
            'fields': ('precio', 'stock',)
        }),
    )

class VentaSup(admin.ModelAdmin):
    class EntryInLines(admin.TabularInline):
        model = Producto
    inlines = [EntryInLines,]
    list_display = ['RUT', 'Descuento_Venta']

# Register your models here.

admin.site.register(Direccion)
admin.site.register(Cliente, ClienteSup)
admin.site.register(Venta, VentaSup)
admin.site.register(Producto, ProductoSup)
admin.site.register(Categoria)
admin.site.register(Proveedor, ProveedorSup)
