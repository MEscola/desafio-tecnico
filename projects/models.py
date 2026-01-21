from django.db import models

class Projects(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    data_inicio = models.DateField()
    data_fim = models.DateField()
    dono_projeto = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
        related_name='projetos'
    )

class SubItem(models.Model):
        STATUS = [
            ('PENDENTE', 'Pendente'),
            ('EM_ANDAMENTO', 'Em Andamento'),
            ('CONCLUIDO', 'Concluído'),
        ]

        project = models.ForeignKey(
            'Projects',
            on_delete=models.CASCADE,
            related_name='subitens'
        )

        titulo = models.CharField(max_length=100)
        descricao = models.TextField()
        responsavel = models.ForeignKey(
            'users.User',
            on_delete=models.CASCADE,
        )

        status = models.CharField( max_length=20, choices=STATUS, default='' )
        prazo = models.DateField()