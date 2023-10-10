from django.db import models

# Create your models here.

class Topico(models.Model):
    
    topico = models.CharField(max_length=264,unique=True)
    
    def __str__(self):
        return self.topico

class Pagina(models.Model):
    
    topico = models.ForeignKey(Topico, on_delete=models.CASCADE)
    
    name = models.CharField(max_length=264,unique=True)
    url = models.URLField(unique=True)
    
    def __str__(self):
        return self.name
    
class Acessos(models.Model):
    
    pagina = models.ForeignKey(Pagina, on_delete=models.CASCADE)
    date = models.DateField()
    
    def __str__(self):
        return str(self.date)
    

class Personagem(models.Model):
    
    Classe = (
    ("GUERREIRO", "Guerreiro"),
    ("ARQUEIRO", "Arqueiro"),
    ("LANCEIRO", "Lanceiro"),
    ("CLERIGO", "Clérigo"),
    ("MAGO", "Mago"),
)
    
    nome = models.CharField(max_length=128)
    classe = models.CharField(max_length=128,
                                choices=Classe,
                                default="Guerreiro")
    atributos = models.IntegerField()
    
    def __str__(self):
        return self.nome
    

class Peneira(models.Model):
    
    temperature = models.IntegerField()
    name = models.CharField(max_length=128)
    
    def __str__(self):
        return str(self.name)

    
class Evento(models.Model):
    
    idPeneira = models.ForeignKey(Peneira, on_delete=models.CASCADE)
    create = models.DateField()
    temperature = models.IntegerField()
    nome = models.CharField(max_length=128, default='evento')
    
    
    def __str__(self):
        return str(self.nome)

