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
            return Response({"message": "Aluno encontrado!", "status": status.HTTP_200_OK}, status=status.HTTP_200_OK)
        except Aluno.DoesNotExist:
            return Response({"message": "Aluno não encontrado!"}, status=status.HTTP_400_BAD_REQUEST)
