from datetime import datetime
from books.models import Libro,Editorial,Autor

def get_current_year(request):
    current_year = datetime.now().year
    return {
        "current_year" : current_year
    }
    
def get_stadistics(request):
    if request.user.is_authenticated:
        usuario_logueado = request.user      
    else: 
        usuario_logueado = False     
    return {
            "n_libros" : Libro.objects.all().count(),
            "n_autores" : Autor.objects.all().count(),
            "n_editoriales" : Editorial.objects.all().count(),
            "usuario_logueado": usuario_logueado       
        }
