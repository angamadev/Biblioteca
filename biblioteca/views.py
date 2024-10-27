import re
from django.shortcuts import render
from books.models import Autor,Libro,Editorial
from books.forms import SearchForm
from .forms import ContactForm
from django.views.generic.edit import FormView
# from django.views.generic import View
from django.core.mail import send_mail
from django import forms
from django.utils.translation import gettext as _
# from django.utils import translation
# from django.http import HttpResponseRedirect




# Vistas generales de la aplicacion
def home_view(request):
    return render(request,'general/home.html')


class ContactUsFormView(FormView):
    template_name = 'general/contact.html'
    form_class = ContactForm
    success_url = "/"

    def form_valid(self, form):
        
        nombre = form.cleaned_data["nombre"]
        email = form.cleaned_data["email"]
        comentario = form.cleaned_data["comentario"]
        message_content = _(f'{nombre} con email {email} ha escrito lo siguiente: {comentario}')
        
        success = send_mail(
            _("formulario de contacto de mi web de Biblioteca"),
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


# class SetLanguageView(View):
#     def post(self, request, *args, **kwargs):
#         # Obtenemos el idioma seleccionado del formulario
#         language = request.POST.get('language',None)
        
#         # Si se selecciono un idioma, lo activamos
#         if language:
#             translation.activate(language)
#             request.session[translation.LANGUAGE_SESSION_KEY] = language
            
#         #Redirigimos a la pagina desde donde se hizo la peticion
#         next_url = request.POST.get('next', '/')
#         return HttpResponseRedirect(next_url)
            
