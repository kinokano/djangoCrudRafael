from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import *
from ..serializers import UserSerializer


class User(APIView):
    def get(self, request, id=None):
        if id:
            usuario = get_object_or_404(CustomUser, pk=id)
            serializer = UserSerializer(usuario)
            return Response(serializer.data, status=status.HTTP_200_OK)

        usuario = CustomUser.objects.all()
        serializer = UserSerializer(usuario, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        nome = request.data.get('username')
        senha = request.data.get('password')

        if not nome or not senha:
            return Response({"error": "Todos os campos são obrigatórios."}, status=status.HTTP_400_BAD_REQUEST)

        usuario = CustomUser.objects.create(
            username=nome,
            password=make_password(senha),
            is_active=True,
            is_aluno=True
        )

        return Response({"message": "Usuário criado com sucesso!", "id": usuario.id}, status=status.HTTP_201_CREATED)

    def put(self, request, id):
        usuario = get_object_or_404(CustomUser, pk=id)
        serializer = UserSerializer(usuario, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
    
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,id):
        usuario = get_object_or_404(CustomUser, pk=id)
        if usuario:
            usuario.delete()
            return Response({"status": status.HTTP_200_OK})
        else:
            return Response({"status": status.HTTP_404_NOT_FOUND})
                

class Login (APIView):
    def post(self, request):
        nome = request.data.get('nome')
        senha = request.data.get('senha')
        user = authenticate(username=nome, password=senha)
        if user:
            login(request, user)
            return Response({"status": status.HTTP_200_OK})
        else:
            return Response({"message": "Nao encontrei", "status": status.HTTP_404_NOT_FOUND})


class GetDadosUsuarioLogado(APIView):
    def get(self, request): 

        user_id = request.session.get('_auth_user_id')

        if user_id:
            user = CustomUser.objects.filter(id=user_id).first()
            serializer = UserSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response({"error": "Usuário não encontrado ou não autenticado"}, status=status.HTTP_404_NOT_FOUND)