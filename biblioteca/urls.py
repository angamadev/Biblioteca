"""
URL configuration for ConquerManager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from django.urls import include, path
from debug_toolbar.toolbar import debug_toolbar_urls # type: ignore
from .views import home_view,search_view,ContactUsFormView,SearchFormView

urlpatterns = [
    path("", home_view, name='home'),
    path('libros/', include('books.url.libro_url', namespace='libro')),
    path('autores/', include('books.url.autor_url', namespace='autor')),
    path('editoriales/', include('books.url.editorial_url', namespace='editorial')),
    path("contact", ContactUsFormView.as_view(), name='contacto'),
    path('user/', include('books.url.user_url', namespace='user')), 
    path('admin/', admin.site.urls),
    path("buscar/", search_view, name='search'),
] + debug_toolbar_urls()
