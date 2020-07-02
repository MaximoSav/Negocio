from django.db import models

# Create your models here.

class Direccion(models.Model):
    calle = models.CharField(max_length = 50)
    numero = models.PositiveIntegerField()
    comuna = models.CharField(max_length = 50)
    ciudad = models.CharField(max_length = 50)

    def __str__(self):
        return ("{}:{}".format(self.calle, self.numero, self.comuna, self.ciudad))

class Cliente(models.Model):
    nombre =  models.CharField(max_length = 50)
    RUT = models.PositiveIntegerField(primary_key=True)
    telefono = models.IntegerField()
    direccion = models.ForeignKey('Direccion', on_delete = models.CASCADE, null = True)

    def __str__(self):
        return ("{}:{}".format(self.nombre, self.RUT, self.telefono, self.direccion))

class Venta(models.Model):
    RUT = models.PositiveIntegerField(primary_key=True)
    fecha = models.DateField() 
    monto_final = models.IntegerField()
    descuento = models.BooleanField(default = True)
    cliente = models.ForeignKey('Cliente', on_delete = models.CASCADE, null = True)

    def Descuento_Venta(self):
        return (self.descuento,)
    #Descuento_Venta.boolean = False
    Descuento_Venta.short_description = 'Descuento de Venta'

    def __str__(self):
        return ("{}:{}".format(self.RUT, self.fecha, self.monto_final, self.descuento, self.cliente))

class Proveedor(models.Model):
    web = models.CharField(max_length = 50)
    nombre =  models.CharField(max_length = 50)
    RUT = models.PositiveIntegerField(primary_key=True)
    direccion = models.ForeignKey('Direccion', on_delete = models.CASCADE, null = True)

    def __str__(self):
        return ("{}:{}".format(self.RUT, self.nombre, self.web, self.direccion))

class Producto(models.Model):
    RUT = models.PositiveIntegerField(primary_key=True)
    nombre =  models.CharField(max_length = 50)
    precio = models.IntegerField()
    stock = models.IntegerField()
    proveedor = models.ForeignKey('Proveedor', on_delete = models.CASCADE, null = True)
    venta = models.ForeignKey('Venta', on_delete = models.CASCADE, null = True)
    categoria = models.ForeignKey('Categoria', on_delete = models.CASCADE, null = True)

    def __str__(self):
        return ("{}:{}".format(self.RUT, self.nombre, self.precio, self.stock, self.proveedor))

class Categoria(models.Model):
    RUT = models.PositiveIntegerField(primary_key=True)
    nombre =  models.CharField(max_length = 50)
    descripcion =  models.CharField(max_length = 80)

    def __str__(self):
        return ("{}:{}".format(self.RUT, self.nombre, self.descripcion))




