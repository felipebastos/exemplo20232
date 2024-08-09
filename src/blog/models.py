from django.db import models
from django.contrib.auth.models import User

# Create your models here.
CATEGORIAS = (
    ('tic', 'Tecnologia da Informação e Comunicação'),
    ('fof', 'Fofocas'),
)

class Postagem(models.Model):
    titulo = models.CharField(max_length=100, unique=True)
    texto = models.TextField()

    curtidas = models.IntegerField()

    categoria = models.CharField(max_length=3, choices=CATEGORIAS, default='fof')

    autor = models.ForeignKey(User, on_delete=models.CASCADE)

    pronto = models.BooleanField(default=False)

    tags = models.ManyToManyField('Tag', through='PostTag')

    def __str__(self):
        return f'Autor: {self.autor.username} - {self.titulo}'



class Tag(models.Model):
    texto = models.CharField(max_length=10, null=False, unique=True)

    def __str__(self):
        return str(self.texto)



class PostTag(models.Model):
    postagem = models.ForeignKey(Postagem, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    desde = models.DateTimeField(auto_now_add=True)
