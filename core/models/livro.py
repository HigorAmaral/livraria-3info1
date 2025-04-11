from django.db import models

class Livro(models.Model):
    titulo = models.CharField(max_length=50)
    isbn = models.CharField(max_length=13, unique=True)
    quantidade = models.IntegerField(default=0)
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.titulo