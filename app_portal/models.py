from django.db import models
from django.contrib.auth.models import User

class Operacao(models.Model):
    # Tipos de operação possível
    Operacoes = (
        ('+', 'soma'),
        ('-', 'subtração'),
        ('*', 'multiplicação'),
        ('/', 'divisão')
    )

    # Relaciona a operação com o usuário que fez
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    # expressao = models.CharField(max_length=100, null=True, blank=True)
    operando1 = models.FloatField()
    operando2 = models.FloatField()
    operador = models.CharField(max_length=1, choices=Operacoes)
    # Guarda o resultado
    resultado = models.FloatField()
    # Data e hora em que a operação foi realizada
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.operando1} {self.operador} {self.operando2}  = {self.resultado}"
