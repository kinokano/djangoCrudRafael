from django.contrib.auth import get_user_model
from django.shortcuts import render

from ..models import *


def login(request):
    return render(request, 'login.html')


def home(request):
    if not request.user.is_authenticated:

        return render(request, 'login.html')
    else:
        users = CustomUser.objects.all()
        return render(request, 'home.html', {'usuarios': users})

    # alunos = Aluno.objects.all()
    # return render(request,'home.html', {'alunos': alunos})


def criar_aluno(request):
    return render(request, 'criar_alunos.html')
