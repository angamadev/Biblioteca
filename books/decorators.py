from books.models import Editorial,Libro,Autor
from django.http import Http404
from django.core.exceptions import PermissionDenied

def is_user_created_editorial(function):
    def wrap(request, *args, **kwargs):
        try:
            editorial = Editorial.objects.get(pk=kwargs["pk"])
            
        except Editorial.DoesNotExist:
            raise Http404
        
        if request.user == editorial.created_by:
            return function(request, *args, **kwargs)
        
        raise PermissionDenied
    return wrap
    
def is_user_created_libro(function):
    def wrap(request, *args, **kwargs):
        try:
            libro = Libro.objects.get(pk=kwargs["pk"])
            
        except Libro.DoesNotExist:
            raise Http404
        
        if request.user == libro.created_by:
            return function(request, *args, **kwargs)
        
        raise PermissionDenied
    return wrap

    
def is_user_created_autor(function):
    def wrap(request, *args, **kwargs):
        try:
            autor = Autor.objects.get(pk=kwargs["pk"])
            
        except Autor.DoesNotExist:
            raise Http404
        
        if request.user == autor.created_by:
            return function(request, *args, **kwargs)
        
        raise PermissionDenied
    return wrap

    