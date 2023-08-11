from django.contrib import admin
from .models import Laboratorio, DirectorGeneral, Producto

class LaboratorioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    search_fields = ('id', 'nombre__icontains')

class DirectorGeneralAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'laboratorio')
    search_fields = ('id','nombre__icontains', 'laboratorio')
    
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id','nombre', 'laboratorio', 'get_fabricacion_year', 'p_costo', 'p_venta')
    search_fields = ('id','nombre__startswith', 'laboratorio')
    list_filter = ('nombre', 'laboratorio__nombre')

    def get_fabricacion_year(self, obj):
        return obj.f_fabricacion.year

    get_fabricacion_year.short_description = 'Año de Fabricación'

admin.site.register(Laboratorio, LaboratorioAdmin)
admin.site.register(DirectorGeneral, DirectorGeneralAdmin)
admin.site.register(Producto, ProductoAdmin)