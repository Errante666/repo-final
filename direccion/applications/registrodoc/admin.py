from django.contrib import admin
from .models import *    # este  enlace es para importar  de la carpeta moedls

# Register your models here.


admin.site.register(Administracion)
admin.site.register(Materia)


class DocenteAdmin(admin.ModelAdmin):
    list_display = (
        'last_name',
        'first_name',    
        'age',
        'id',       
        'materia',
    )

    search_fields = ('last_name', 'first_name')       #para el campo de busqueda
    
admin.site.register(Docente, DocenteAdmin)

class NoDocenteAdmin(admin.ModelAdmin):
    list_display = (
        'last_name',
        'first_name',    
        'age',
        'id',
        'administracion',
       
    )

    search_fields = ('last_name', 'first_name')   #para el campo de busqueda
    

admin.site.register(NoDocente, NoDocenteAdmin)

