from django.db import models
 
# Create your models here.
class Professor(models.Model):
    def _str_(self):
        return "Nome: " + self.nome + " - Email: " + self.email
 
    nome = models.TextField(max_length=255)
    email = models.TextField(max_length=255)
    celular = models.TextField(max_length=20)
    login = models.TextField(max_length=20)
    senha = models.TextField(max_length=20)
 
    def save(self):
        print('estou salvando!')
        if(self.login == ''):
            raise Exception('login nao enviado')
        if(self.email == ''):
            self.email = "email nao fornecido"
        super(Professor,self).save()
 
 
class Disciplina(models.Model):
 
	nome_1 = models.TextField(max_length=50)
	ementa = models.TextField(max_length=5000)
 
 
class DisciplinaOfertada(models.Model):
 
	curso = models.TextField(max_length=255)
	turma = models.TextField(max_length=5)
	ano = models.IntegerField() #um inteiro, representa um ano
	semestre = models.IntegerField() #um inteiro, 1 para primeiro sem e 2 para segundo
	professor = models.IntegerField() #id de um professor valido
	disciplina = models.IntegerField() #id de uma disciplina valida