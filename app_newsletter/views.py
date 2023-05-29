from django.shortcuts import render, redirect
from .models import *

def telaDeLogin(request):
    if request.method == "POST":
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        cadastro = Cadastro.objects.filter(email=email,senha=senha)

        if cadastro:
            return redirect('home',cadastro[0].id)
        
    return render(request,'telaDeLogin.html')

def cadastro(request):
    if request.method == "POST":
        #Pegar as informações do form, do html
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
     
        #Parte de criação no banco de dados
        cadastro = Cadastro()
        cadastro.nome = nome
        cadastro.email = email
        cadastro.senha = senha
        cadastro.save()
        return redirect('home',cadastro.id)

    return render(request,'cadastro.html')

def home(request,id):
    cadastro = Cadastro.objects.filter(id=id)
    cadastros = {
        'cadastros':cadastro
    }

    return render(request,'home.html',cadastros)

def add_email(request,id):

    servico = Servico.objects.all()

    servicos = {
        'servicos':servico
    }
    return render(request,'email/add_email.html',servicos)