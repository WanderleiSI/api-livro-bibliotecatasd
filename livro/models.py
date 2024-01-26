from django.db import models

# Create your models here.
class Livro(models.Model):
    nome = models.CharField(max_length=30,null=False,blank=False)
    editora = models.CharField(max_length=15,null=False,blank=False)
    ano = models.DateField(null=True)

    
    def __str__(self):
        return F"{self.nome} | {self.editora} | {self.ano}"
