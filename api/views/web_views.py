from django.shortcuts import render

from ..models import Aluno


def login(request):
    return render(request,'login.html')

def home(request):
    if not request.COOKIES.get('auth_token'):
            return render(request, 'login.html') 
    
    alunos = Aluno.objects.all()
    return render(request,'home.html', {'alunos': alunos})

def criar_aluno(request):
    return render(request,'criar_alunos.html')