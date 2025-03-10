from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    is_aluno = models.BooleanField(default=False)


# Create your models here.
# class Aluno(models.Model):
#     nome = models.CharField(max_length=255)
#     email = models.EmailField()

#     def __str__(self):
#         return self.nome