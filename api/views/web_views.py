from django.shortcuts import redirect, render

from ..models import *


def login(request):
    return render(request, 'login.html')

def home(request):
    if not request.user.is_authenticated:
        return render(request, 'login.html')
    else:
        users = CustomUser.objects.all()
        return render(request, 'home.html', {'usuarios': users})

def criar_aluno(request,id=None):
    if not request.user.is_authenticated:
        return render(request, 'login.html')
    else:
        if id:
            user = CustomUser.objects.filter(id=id).first()
            if user:
                return render(request, 'criar_alunos.html', {'usuarioDetalhe': user})   
            else:
                return redirect('CriarAluno') #o nome no redirect é dado pelo name colocado na rota no arquivo urls.py

        return render(request, 'criar_alunos.html')
        
