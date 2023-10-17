from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Create your views here.
def login(request):
    template = 'users/login.html'
    return render(request, template)
    #! validando se veio de um formulario
    # if request.method != 'POST':
    #     return render(request, 'users/login.html')
    #
    # usuario = request.POST.get('usuario')
    # senha = request.POST.get('senha')
    #
    # user = auth.authenticate(request, username=usuario, password=senha)
    # if not user:
    #     messages.add_message(request, messages.ERROR, 'Usuário ou senha inválido')
    #     return render(request, 'users/login.html')
    # else:
    #     auth.login(request, user)
    #     return redirect('home')

def logout(request):
    # auth.logout(request)
    return redirect('home')
