from django.db import models
from django.utils import timezone

# Criar um modelo do Professor, com nome, email, telefone, registro, disciplina
class Professor(models.Model):
    # Atributos = características = variáveis
    nome = models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=30)
    email = models.EmailField()
    # ERRO ENCONTRADO: import timezone não realizado
    # Correção: adicionado na linha 2 o comando <from django.utils import timezone>
    criacao_data = models.DateTimeField(default=timezone.now) 
    telefone = models.CharField(max_length=15)
    registro = models.CharField(max_length=10)
    disciplina = models.CharField(max_length=30)
    ativo = models.BooleanField(default=True)
    observacao = models.TextField(blank=True)
    imagem = models.ImageField(upload_to='img/%Y/%m', blank=True)

    # Métodos = ações = funções
    def __str__(self):
        return f'{self.nome} {self.sobrenome}'

# Criar um modelo do Aluno, com nome, email, telefone, matricula
class Aluno(models.Model):
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    email = models.EmailField()
    telefone = models.CharField(max_length=15)
    # ERRO ENCONTRADO: models.IntegerField() é um tipo errado para a situação
    # Correção: tipo alterado para models.CharField, para armazenar zeros à esquerda
    matricula = models.CharField()
    # ERRO ENCONTRADO: import timezone não realizado
    # Correção: adicionado na linha 2 o comando <from django.utils import timezone>
    criacao_data = models.DateTimeField(default=timezone.now)  
    observacao = models.TextField(blank=True)
    ativo = models.BooleanField(default=True)
    imagem = models.ImageField(upload_to='img/%Y/%m', blank=True)

    def __str__(self):
        return f'{self.nome} {self.sobrenome}'

class Aula(models.Model):
    aluno_id = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    professor_id = models.ForeignKey(Professor, on_delete=models.CASCADE)
    # ERRO ENCONTRADO: import timezone não realizado
    # Correção: adicionado na linha 2 o comando <from django.utils import timezone>
    horario = models.DateTimeField(default=timezone.now)  
    observacao = models.TextField(blank=True)
    status = models.CharField(
        default='A',
        max_length=1,
        choices=(
            ('A', 'Agendada'),
            ('X', 'Cancelada'),
            ('C', 'Confirmada'),
            ('R', 'Realizada')
        )
    )

    def __str__(self):
        return f'Aula {self.status} com sucesso.'
