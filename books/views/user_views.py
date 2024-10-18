from django.shortcuts import render,redirect
from biblioteca.forms.user_forms import LoginForm,UserRegisterForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.urls import reverse,reverse_lazy
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# Create your views here.
def registro_view(request):
    if request.POST:
        formulario = UserRegisterForm(request.POST)
        if formulario.is_valid():
            username = formulario.cleaned_data["username"]
            first_name = formulario.cleaned_data["first_name"]
            last_name = formulario.cleaned_data["Last_name"]
            email = formulario.cleaned_data["email"]
            password1 = formulario.cleaned_data["password1"]
            password2 = formulario.cleaned_data["password2"]
            user =User.objects.create_user(username,email,password2)
            if user: 
                user.first_name = first_name
                user.last_name = last_name
                user.password1 = password1
                user.save()
                
            context = {
                "msg" : "Ususario creado correctamente",
                
            }
            return render(request,'general/registro.html', context)
        
        else:
            context = {
                "form" : formulario,
            }
            return render(request,'general/registro.html', context)
    else:
        formulario = UserRegisterForm()
        context = {
            "form" : formulario
            }
        return render(request,'general/registro.html', context)


def login_view(request):
    if request.POST:
        formulario = LoginForm(request.POST)
        users = User.objects.filter(username="a")
        print(users)
        if formulario.is_valid():
            username = formulario.cleaned_data["username"]
            password = formulario.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request,user)
                return redirect(reverse_lazy("home"))
            else:
                context = {
                    "form" : formulario,
                    "success" : False,
                    "error_message" : "Usuario no valido"
                }
                return render(request,'general/login.html', context)
            
            
                message_content = f'El usuario {username} con contraseña {password} se ha registrado correctamente'
                print(username)
                User.objects.create_user(
                    username = username,
                    password = password,
                )
                
                success = send_mail(
                    "Creacion de contacto nuevo",
                    message_content,
                    "info@angamadev.com",
                    ["angamadev@gmail.com"],
                    fail_silently=False,
                )
                context = {
                    "form" : formulario,
                    "success" : success
                }
                
                print(f'Se ha registrado el usuario { username } con contraseña {password} se ha registrado correctamente')
                return render(request,'general/login.html', context)
            
        else:
            context = {
                "form" : formulario,
            }
            return render(request,'general/login.html', context)
    else:
        formulario = LoginForm()
        context = {
            "form" : formulario
            }
        return render(request,'general/login.html', context)
@login_required
def logout_view(request):
    logout(request)
    return redirect(reverse_lazy("home"))

