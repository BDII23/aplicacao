'''class utilizador_perfil(models.Model):
    data_criacao = models.DateTimeField(auto_now_add=True)
    perfil = models.CharField(max_length=100)

    def __str__(self):
        return self.perfil

class utilizador(models.Model):
    data_criacao = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(max_length=500)
    senha = models.CharField(max_length=400)
    nome = models.CharField(max_length=300)
    sobrenome = models.CharField(max_length=300)
    perfil = models.ForeignKey(utilizador_perfil, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nome} {self.sobrenome}"
'''