from django.db import models

from users.validators import validate_cpf

class User(models.Model):
    nome_completo = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14, unique=True, validators=[validate_cpf])
    telefone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    aceite_cadastro = models.BooleanField()

    def __str__(self):
        return f'{self.nome_completo} - {self.cpf}'