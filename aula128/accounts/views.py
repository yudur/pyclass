from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.validators import validate_email
from django.contrib.auth.models import User


def login(request):
    return render(request, 'accounts/login.html')


def logout(request):
    return render(request, 'accounts/logout.html')


def cadastro(request):
    if request.method != 'POST':
        return render(request, 'accounts/cadastro.html')

    nome = request.POST.get('nome')
    sobrenome = request.POST.get('sobrenome')
    email = request.POST.get('email')
    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')
    rep_senha = request.POST.get('rep_senha')

    if not nome or not sobrenome or not email or not usuario or not senha or not rep_senha:
        messages.error(request, 'preencha todos os campos vazios.')
        return render(request, 'accounts/cadastro.html')

    try:
        validate_email(email)
    except:
        messages.error(request, 'email inválido.')
        return render(request, 'accounts/cadastro.html')

    if len(usuario) <= 4:
        messages.error(request, 'usuário precisa ter mais de 4 caracteres.')
        return render(request, 'accounts/cadastro.html')

    if len(senha) <= 6:
        messages.error(request, 'senha precisa ter mais de 6 caracteres.')
        return render(request, 'accounts/cadastro.html')

    if senha.isalpha() or senha.isnumeric() or senha.isspace():
        messages.error(request, 'senha precisa conter letras e números.')
        return render(request, 'accounts/cadastro.html')

    if senha != rep_senha:
        messages.error(request, 'senha incorreta.')
        return render(request, 'accounts/cadastro.html')

    if User.objects.filter(username=usuario).exists():
        messages.error(request, 'usuário já existente.')
        return render(request, 'accounts/cadastro.html')

    if User.objects.filter(email=email).exists():
        messages.error(request, 'E-mail já existente.')
        return render(request, 'accounts/cadastro.html')

    messages.success(request, 'Registrado com sucesso! Agora faça login.')

    user = User.objects.create_user(username=usuario, email=email,
                                    password=senha, first_name=nome,
                                    last_name=sobrenome)
    user.save()
    return redirect('login')


def dashboard(request):
    return render(request, 'accounts/dashboard.html')
