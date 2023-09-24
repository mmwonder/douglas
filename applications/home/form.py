from django import forms
from .models import prueba

class PruebaForm(forms.ModelForm):
    """Form definition for MODELNAME."""

    class Meta:
        """Meta definition for MODELNAMEform."""

        model = prueba
        fields = ('titulo',
                  'subtitulo',
                  'cantidad',)
        widgets={
            'titulo':forms.TextInput(
                attrs = {
                    'placeholder':'Ingrese texto aqui'
                }
            )
        }
        
    def clean_cantidad(self):
        cantidad=self.cleaned_data['cantidad'] #recupera el valor que se encuentra dentro de cantidad
        if cantidad < 10:
            raise forms.ValidationError('ingrese un numero mayor a 10')
        return cantidad
