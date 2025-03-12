from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views.api_views import *
from .views.web_views import criar_aluno, home, login

#CADASTRO DAS ROTAS DA API
# router = DefaultRouter()
# router.register('user',UserViewSet)

urlpatterns = [
    # path('api/',include(router.urls)),
    path('api/user', User.as_view(),name="usuarios"),
    path('api/user/<int:id>', User.as_view(),name="usuarios_detail"),
    path('api/login',Login.as_view(),name="VerificaLogin"),
    path('api/GetDadosUsuarioLogado',GetDadosUsuarioLogado.as_view(),name="getDadosUsuarioLogado"),
    path('',login, name="login"),
    path('home/',home, name="home"),
    path('criarAluno/',criar_aluno, name="CriarAluno"),
    path('criarAluno/<int:id>',criar_aluno, name="CriarAlunoDetail"),
]


