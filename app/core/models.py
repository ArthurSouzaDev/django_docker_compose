from django.db import models

# Create your models here.
class Documento(models.Model):
    titulo = models.CharField(max_length=100)
    arquivo = models.FileField(upload_to='arquivos_salvos/') 

    def __str__(self):
        return self.titulo

        