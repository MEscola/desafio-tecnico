import re
from django.core.exceptions import ValidationError

def validate_cpf(value):
    # Remove pontos e traço
    cpf = re.sub(r'\D', '', value)

    # Verifica tamanho
    if len(cpf) != 11:
        raise ValidationError("CPF deve conter 11 dígitos.")

    # Evita CPFs com todos os números iguais
    if cpf == cpf[0] * 11:
        raise ValidationError("CPF inválido.")

    # Validação dos dígitos verificadores
    for i in range(9, 11):
        soma = sum(int(cpf[num]) * ((i + 1) - num) for num in range(i))
        digito = ((soma * 10) % 11) % 10

        if digito != int(cpf[i]):
            raise ValidationError("CPF inválido.")

def validade_telefone(value):
    pattern =r'^(\(?\d{2}\)?\s?)?(9?\d{4}-?\d{4})$'
    
    if not re.match(pattern, value):
        raise ValidationError("Número de telefone inválido.")

def validade_nascimento(value):
    from datetime import date
    if value > date.today():
        raise ValidationError("A data de nascimento não pode ser no futuro.")