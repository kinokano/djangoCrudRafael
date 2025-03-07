import uuid

from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import Aluno
from ..serializers import AlunoModelSerializer


class AlunoModelViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoModelSerializer


class VerificaLogin(APIView):
    def post(self, request):
        # Captura os dados enviados no corpo da requisição
        nome = request.data.get('nome')
        email = request.data.get('email')

        # Verifica se o aluno existe no banco de dados
        try:
            aluno = Aluno.objects.get(nome=nome, email=email)
            
            # Aqui você pode gerar um token ou qualquer outra informação para o cookie
            token = str(uuid.uuid4())  # Exemplo de um token gerado aleatoriamente

            # Criando a resposta e configurando o cookie HttpOnly
            response = Response(
                {"message": "Aluno encontrado!", "status": status.HTTP_200_OK},
                status=status.HTTP_200_OK
            )

            # Adiciona o cookie HttpOnly na resposta
            response.set_cookie(
                key='auth_token',  # Nome do cookie
                value=token,  # Valor do cookie (pode ser o token JWT ou qualquer outro dado)
                httponly=True,  # Impede o acesso via JavaScript
                secure=True,  # Só envia o cookie em requisições HTTPS
                samesite='Strict',  # Protege contra CSRF
                max_age=3600  # Tempo de expiração (1 hora, por exemplo)
            )

            return response

        except Aluno.DoesNotExist:
            return Response({"message": "Aluno não encontrado!"}, status=status.HTTP_400_BAD_REQUEST)
