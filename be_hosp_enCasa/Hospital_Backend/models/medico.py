from django.db import models
from .usuario import Usuario

class Medico(models.Model):
    id=models.AutoField(primary_key=True)
    usuario=models.ForeignKey(Usuario, on_delete=models.CASCADE)
    especialidad=models.CharField(max_length=45)
    rol=models.CharField('Rol',max_length=35)
    licencia = models.CharField(max_length=20)