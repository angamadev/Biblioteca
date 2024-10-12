from django.shortcuts import render
from books.models import Autor,Libro,Editorial
from books.forms import SearchForm
from .forms import ContactForm
from django.views.generic.edit import FormView
from django.core.mail import send_mail
from django import forms


# Vistas generales de la aplicacion
def home_view(request):
    return render(request,'general/home.html')

# def contact_view(request):
#     if request.POST:
#         formulario = ContactForm(request.POST)
        
#         if formulario.is_valid():
#             nombre = formulario.cleaned_data["nombre"]
#             email = formulario.cleaned_data["email"]
#             comentario = formulario.cleaned_data["comentario"]

#             context = {
#                 "formulario" : formulario,
#                 "success" : True
#             }
#             print(f'se ha enviado un correo a { nombre } procedente de {email} con el texto {comentario}')

#             return render(request,'general/contact.html', context)
#         else: 
#             context = {
#                 "formulario" : formulario,
#             }
#             return render(request,'general/contact.html', context)
        
#     formulario = ContactForm()
#     context = {
#         "formulario" : formulario,
#         "success" : True
#     }
#     return render(request,'general/contact.html', context)

class ContactUsFormView(FormView):
    template_name = 'general/contact.html'
    form_class = ContactForm
    success_url = "/"

    def form_valid(self, form):
        
        nombre = form.cleaned_data["nombre"]
        email = form.cleaned_data["email"]
        comentario = form.cleaned_data["comentario"]
        message_content = f'{nombre} con email {email} ha escrito lo siguiente: {comentario}'
        
        success = send_mail(
            "formulario de contacto de mi web de Biblioteca",
            message_content,
            "info@angamadev.com",
            ["angamadev@gmail.com"],
            fail_silently=False,
        )
            
        return super().form_valid(form)

class SearchFormView(FormView):
    template_name = 'general/search.html'
    form_class = SearchForm
    success_url = 'general/search.html'

    # def get(self, request, *args, **kwargs):
    #     """Handle GET requests: instantiate a blank version of the form."""
    #     formulario = SearchForm(request.GET)
    #     return self.render_to_response(self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["autores"] = Autor.objects.filter(nombre__icontains=['q'])
        context["editoriales"] = Editorial.objects.filter(nombre__icontains=['q'])
        context["libros"] = Libro.objects.filter(nombre__icontains=['q'])
    
        return context

def search_view(request):
    if request.GET:
        
        formulario = SearchForm(request.GET)
        busqueda = formulario.data['q']
        print(busqueda)
        autores = Autor.objects.filter(nombre__icontains=busqueda)
        editoriales = Editorial.objects.filter(nombre__icontains=busqueda)
        libros = Libro.objects.filter(titulo__icontains=busqueda)
        context = {
            'autores' : autores,
            'editoriales' : editoriales,
            'libros' : libros,
            "formulario" : formulario
        }
        return render(request, 'general/search.html', context) 
    else:
        formulario = SearchForm()
        
    context = { 
        "formulario" : formulario
    }
    return render(request, 'general/search.html', context)
    
## Funcion de search view simple
# ----------------------------------    
# def search_view(request):
    # if request.GET:
    #     busqueda = request.GET['q']
    #     autores = Autor.objects.filter(nombre__icontains=busqueda)
    #     editoriales = Editorial.objects.filter(nombre__icontains=busqueda)
    #     libros = Libro.objects.filter(titulo__icontains=busqueda)
    #     context = {
    #         'autores' : autores,
    #         'editoriales' : editoriales,
    #         'libros' : libros,
    #     }
    #     print(context)
    #     return render(request, 'general/search.html', context)  
    # return render(request, 'general/search.html', context)


## funcion de contacto view simple
# ---------------------------------------
# def contact_view(request):
#     if request.POST:
#         nombre = request.POST["nombre"]
#         email = request.POST["email"]
#         comentario = request.POST["comentario"]
#         print(f'se ha enviado un correo a { nombre } procedente de {email} con el texto {comentario}')
#     return render(request,'general/contact.html')

    