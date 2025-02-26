from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views.api_views import AlunoModelViewSet, VerificaLogin
from .views.web_views import criar_aluno, home, login

#CADASTRO DAS ROTAS DA API
router = DefaultRouter()
router.register('alunos',AlunoModelViewSet)



urlpatterns = [
    path('api/',include(router.urls)),
    path('api/verificaLogin',VerificaLogin.as_view(),name="VerificaLogin"),
    path('',login, name="login"),
    path('home/',home, name="home"),
    path('criarAluno/',criar_aluno, name="criar_aluno"),
]


