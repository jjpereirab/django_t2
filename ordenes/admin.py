from django.contrib import admin
from .models import Orden, ProductoEnOrden

# Register your models here.
class ProductoEnOrdenInLine(admin.TabularInline):
    model = ProductoEnOrden
    extra = 0

class OrdenAdmin(admin.ModelAdmin):
    modelo = Orden
    list_display = ['id', 'usuario', "activa", "creacion"]  # <--- SE TIENE QUE LLAMAR list_display
    search_fields = ['usuario', 'id']  # <--- SE TIENE QUE LLAMAR search_fields
    readonly_fields = ('creacion',) # <--- SE TIENE QUE LLAMAR readonly_fields
    inlines = [ProductoEnOrdenInLine] # <--- SE TIENE QUE LLAMAR readonly_fields


admin.site.register(Orden, OrdenAdmin)
