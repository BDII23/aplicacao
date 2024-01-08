from django.db import models


class Componente(models.Model):
    descricao = models.TextField()
    quantidade = models.IntegerField(default=0)

    # Relacionamentos
    tipo = models.ForeignKey('TipoComponente', on_delete=models.CASCADE)
    armazem = models.ForeignKey('Armazem', on_delete=models.CASCADE)

    def __str__(self):
        return self.descricao

class TipoComponente(models.Model):
    tipo = models.CharField(max_length=100)

    def __str__(self):
        return self.tipo

class Armazem(models.Model):
    endereco = models.CharField(max_length=100)

    def __str__(self):
        return self.endereco


# Create your models here.
