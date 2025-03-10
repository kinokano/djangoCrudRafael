
from django.contrib.auth import authenticate, get_user_model, login
from django.contrib.sessions.models import Session
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import *
from ..serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

class Login (APIView):
    def post(self,request):
        nome = request.data.get('nome')
        senha = request.data.get('senha')
        user = authenticate(username=nome, password=senha)
        if user:
            login(request,user)
            return Response({"status": status.HTTP_200_OK})
        else:
            return Response({"message": "Nao encontrei","status": status.HTTP_404_NOT_FOUND})

class GetDadosUsuarioLogado(APIView):
    def get(self, request):  # Agora usamos GET, pois não precisamos enviar dados no corpo
        # Django já captura a sessão automaticamente
        user_id = request.session.get('_auth_user_id')

        if user_id:
            user = CustomUser.objects.filter(id=user_id).first()
            if user:
                user_data = {
                    "id": user.id,
                    "username": user.username,
                    "email": user.email,
                    "first_name": user.first_name,
                    "last_name": user.last_name
                }
                return Response(user_data, status=status.HTTP_200_OK)

        return Response({"error": "Usuário não encontrado ou não autenticado"}, status=status.HTTP_404_NOT_FOUND)


# class VerificaLogin(APIView):
#     def post(self, request):
#         # Captura os dados enviados no corpo da requisição
#         nome = request.data.get('nome')
#         email = request.data.get('email')

#         # Verifica se o aluno existe no banco de dados
#         try:
#             # aluno = Aluno.objects.get(nome=nome, email=email)
    
#             # Aqui você pode gerar um token ou qualquer outra informação para o cookie
#             token = str(uuid.uuid4())  # Exemplo de um token gerado aleatoriamente

#             # Criando a resposta e configurando o cookie HttpOnly
#             response = Response(
#                 {"message": "Aluno encontrado!", "status": status.HTTP_200_OK},
#                 status=status.HTTP_200_OK
#             )

#             # Adiciona o cookie HttpOnly na resposta
#             response.set_cookie(
#                 key='auth_token',  # Nome do cookie
#                 value=token,  # Valor do cookie (pode ser o token JWT ou qualquer outro dado)
#                 httponly=True,  # Impede o acesso via JavaScript
#                 secure=True,  # Só envia o cookie em requisições HTTPS
#                 samesite='Strict',  # Protege contra CSRF
#                 max_age=3600  # Tempo de expiração (1 hora, por exemplo)
#             )

#             return response

#         except Aluno.DoesNotExist:  
#             return Response({"message": "Aluno não encontrado!"}, status=status.HTTP_404_NOT_FOUND)
