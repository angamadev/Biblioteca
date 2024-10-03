from django import forms

# from books import forms

class SearchForm(forms.Form):
    q = forms.CharField(
        label="Introduce cualquier cadena de texto"
        , max_length=100
        )