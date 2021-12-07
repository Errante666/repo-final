from django import forms
from .models import Docente
from .models import NoDocente


class DocenteForm(forms.ModelForm):
    

    class Meta:
        """Meta definition for Docenteform."""        

        model = Docente
        fields = (
            'first_name',
            'first_name',
            'age',            
            'materia',
            'avatar',             

        )
        
class NoDocenteForm(forms.ModelForm):
    

    class Meta:
        """Meta definition for NoDocenteform."""        

        model = NoDocente
        fields = (
            'first_name',
            'first_name',
            'age',
            'administracion',
            'avatar',             

        )
        