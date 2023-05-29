from django.db import models

# Create your models here.
class Cadastro(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    email= models.TextField(max_length=255)
    senha = models.TextField(max_length=255)

class Servico(models.Model):
    id = models.AutoField(primary_key=True)
    descricao = models.TextField(max_length=255)

class CadastroServico(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.TextField(max_length=255)
    servico = models.ForeignKey(Servico,on_delete=models.CASCADE)
    cadastro_id = models.ForeignKey(Cadastro,on_delete=models.CASCADE)