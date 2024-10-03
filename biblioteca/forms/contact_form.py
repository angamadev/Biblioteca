from django import forms

class ContactForm(forms.Form):
    nombre = forms.CharField(
        label="nombre",
        max_length=100
    )
    email = forms.EmailField(
        label="email",
    )
    comentario = forms.CharField(
        label="comentario",
        max_length= 300,
        widget=forms.Textarea,
    )
    def clean_comentario(self):
        comentario = self.cleaned_data["comentario"]
        if len(comentario) < 5:
            raise forms.ValidationError("El comentario debe tener al menos 5 caracteres")
        return comentario
    
    def clean_nombre(self):
        nombre = self.cleaned_data["nombre"]
        if len(nombre) < 2:
            raise forms.ValidationError("El nombre debe tener al menos 2 caracteres")
        return nombre
    
    