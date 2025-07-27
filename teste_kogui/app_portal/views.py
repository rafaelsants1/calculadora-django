from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .models import Operacao
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from datetime import datetime

def login_view(request):
    if request.method == 'POST':
        # Identifica o formulário que foi enviado
        form_type = request.POST.get('form_type')

        if form_type == 'login':
            # Captura dados do formulário
            username = request.POST.get('username')
            password = request.POST.get('password')
            # Autentica o usuário com as credenciais

            user = authenticate(request, username=username, password=password)
            if user is not None:
                # Se o usuário for válido, o login é feito e direciona para a calculadora
                login(request, user)
                return redirect('calculadora')
            else:
                return render(request, 'login.html', {'erro': 'Usuário ou senha inválidos.'})
            
        # Registra novo usuário
        elif form_type == 'register':
            username = request.POST.get('new_username')
            email = request.POST.get('new_email')
            password1 = request.POST.get('new_password1')
            password2 = request.POST.get('new_password2')

            if password1 != password2:
                return render(request, 'login.html', {'erro': 'As senhas não coincidem'})
            
            if User.objects.filter(username=username).exists():
                return render(request, 'login.html', {'erro': 'Usuário já existe'})
            
            user = User.objects.create_user(username=username, password=password1, email=email)
            login(request, user) # Realiza login automaticamente após cadastro
            return redirect('calculadora')
        
    return render(request, 'login.html')

@login_required # Garante que somente os usuários logados podem acessar
def calculadora_view(request):
    # Busca os últimos 5 cálculos realizados do usuário
    historico = Operacao.objects.filter(usuario=request.user).order_by('-data')[:5]
    resultado = ""
    expressao = ""

    if request.method == 'POST':
        expressao = request.POST.get('expressao', '')
        try:
            resultado = eval(expressao)

            for operador in ['+', '-', '*', '/']:
                if operador in expressao:
                    op1, op2 = expressao.split(operador)
                    op1 = float(op1)
                    op2 = float(op2)
                    break

            Operacao.objects.create(
                usuario=request.user,
                operando1=op1,
                operando2=op2,
                operador=operador,
                resultado=resultado,
                data=datetime.now()
            )
        except:
            resultado = 'Erro'

    # Para criar o teclado virtual
    teclado = [
        [('7', '7'), ('8', '8'), ('9', '9'), ('÷', '/')],
        [('4', '4'), ('5', '5'), ('6', '6'), ('x', '*')],
        [('1', '1'), ('2', '2'), ('3', '3'), ('-', '-')],
        [('0', '0'), ('.', '.'), ('+', '+'),],
    ]

    return render(request, 'app_portal.html', {
        'historico': historico,
        'resultado': resultado,
        'teclado': teclado,
        'expressao': resultado
    })

def logout_view(request):
    logout(request)
    return redirect('login')