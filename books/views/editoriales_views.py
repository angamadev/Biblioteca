from django.shortcuts import render,redirect
from books.forms.editorial_form import EditorialCreate,EditorialCreateModelforms
from books.models.editorial_model import Editorial
from django.urls import reverse


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

def editorial_create(request):
    if request.POST:
        form = EditorialCreateModelforms(request.POST)
        if form.is_valid():
            
            nueva_editorial = Editorial.objects.create(
                nombre = form.cleaned_data["nombre"],
                direccion = form.cleaned_data["direccion"],
                ciudad = form.cleaned_data["ciudad"],
                estado = form.cleaned_data["estado"],
                pais = form.cleaned_data["pais"],
                codigo_postal = form.cleaned_data["codigo_postal"],
                telefono = form.cleaned_data["telefono"],
                email = form.cleaned_data["email"],
                sitio_web = form.cleaned_data["sitio_web"],
                fecha_fundacion = form.cleaned_data["fecha_fundacion"]
            )
            context = {
                "form" : form,
                "new_editorial" : "Editorial Creada exitosamente"
            }
            # return render(request, 'editoriales/editorial_create.html',context)
            return redirect(reverse("books:editorial_detail", kwargs={ "id": nueva_editorial.pk }))

        else:
            context = {
                "form" : form,
            }
            print(request.GET)
            return render(request, 'editoriales/editorial_create.html',context)

    else:
        form = EditorialCreateModelforms()
        context = {
            "form" : form
        }
        return render(request, 'editoriales/editorial_create.html',context)
