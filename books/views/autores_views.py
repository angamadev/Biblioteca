from django.shortcuts import render
from datetime import date
from books.models.autor_model import Autor



# Create your views here.
def autores_view(request):
    autores = Autor.objects.all()
    context = {
        "autores":autores,
    }
    return render(request, 'autores/autor.html', context)

def autor_detail(request, id):
    autor = Autor.objects.get(pk=id)

    context = {
            "autor": autor,
        }
    return render(request, 'autores/autor_detail.html', context)