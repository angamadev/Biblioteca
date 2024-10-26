import re
from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.utils.translation import gettext as _
from books.models.editorial_model import Editorial

# from books import forms

class EditorialCreate(forms.Form):
    nombre = forms.CharField(max_length=200)
    direccion = forms.CharField(max_length=300)
    ciudad = forms.CharField(max_length=100, required=False)
    estado = forms.CharField(max_length=100, required=False)
    pais = forms.CharField(max_length=100, required=False)
    codigo_postal = forms.CharField(max_length=20, required=False)
    telefono = forms.CharField(max_length=20, required=False)
    email = forms.EmailField()
    sitio_web = forms.URLField(required=False)
    fecha_fundacion = forms.DateField(widget=forms.SelectDateWidget)

    def clean_nombre(self):
        nombre = self.cleaned_data["nombre"]
        if len(nombre) < 5:
            raise forms.ValidationError(_("El nombre debe tener al menos 5 caracteres"))
        return nombre
    
class EditorialCreateModelforms(ModelForm):
    class Meta:
        model = Editorial
        fields = [
            'nombre',
            'direccion',
            'ciudad',
            'codigo_postal',
            'estado',
            'pais',
            'telefono',
            'email',
            'fecha_fundacion',
            'sitio_web',
            ]

