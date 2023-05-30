from django.db import models

class Livro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    ano_lancamento = models.IntegerField()
    estado = models.CharField(max_length=100)
    paginas = models.IntegerField()
    editora = models.CharField(max_length=100)

    def __str__(self):
        return self.titulo
