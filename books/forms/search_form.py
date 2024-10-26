from django import forms
from django.utils.translation import gettext as _

# from books import forms

class SearchForm(forms.Form):
    q = forms.CharField(
        label=_("Introduce cualquier cadena de texto")
        , max_length=100
        )