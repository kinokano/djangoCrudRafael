from rest_framework import serializers

from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = "__all__"

    def create(self, validated_data):
        # Criação de usuário com senha hash
        password = validated_data.pop('password', None)
        user = CustomUser.objects.create(**validated_data)  # Ou CustomUser.objects.create se for o caso

        if password:
            user.set_password(password)  # Criptografa a senha
            user.save()

        return user
    
    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)

        # Atualiza os outros campos
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        # Atualiza a senha (com hash) se fornecida
        if password:
            instance.set_password(password)
        
        instance.save()
        return instance