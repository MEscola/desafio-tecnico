from django.db import models

from users.validators import validade_nascimento, validade_telefone, validate_cpf
from django.db import models


class User(models.Model):
    nome_completo = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14, unique=True, validators=[validate_cpf])
    telefone = models.CharField(max_length=15, validators=[validade_telefone])
    email = models.EmailField(unique=True)
    data_nascimento = models.DateField(null=True, blank=True, validators=[validade_nascimento])
    aceite_cadastro = models.BooleanField()

    def __str__(self):
        return f'{self.nome_completo} - {self.cpf}'