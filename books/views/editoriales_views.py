from django.shortcuts import render
from books.models.editorial_model import Editorial


# Create your views here.
def editoriales_view(request):
    editoriales = Editorial.objects.all()
    context = {
        "editoriales" : editoriales,
    }
    
    return render(request, 'editoriales/editorial.html', context)

def editorial_detail(request, id):
    editorial = Editorial.objects.get(pk=id)

    context = {
            "editorial": editorial,
        }
    return render(request, 'editoriales/editorial_detail.html', context)