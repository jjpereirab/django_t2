from django.contrib import admin
from .models import Producto


# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    modelo = Producto
    list_display = ['nombre', 'precio', "disponible", "creacion"]  # <--- SE TIENE QUE LLAMAR list_display
    search_fields = ['nombre', 'precio']  # <--- SE TIENE QUE LLAMAR search_fields
    readonly_fields = ('creacion',) # <--- SE TIENE QUE LLAMAR readonly_fields


admin.site.register(Producto, ProductoAdmin)