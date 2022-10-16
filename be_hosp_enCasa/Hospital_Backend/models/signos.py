from django.db import models
from .paciente import Paciente

class Signos_vitales(models.Model):
    id_sigvitales=models.AutoField(primary_key=True)
    id_paciente=models.ForeignKey(Paciente, related_name='sig_vitales', on_delete=models.CASCADE)
    oximetria=models.IntegerField(default=0)
    frec_cardiaca=models.IntegerField(default=0)
    frec_respiratoria=models.IntegerField(default=0)
    temperatura=models.IntegerField(default=0)
    glicemias=models.IntegerField(default=0)
    presion=models.CharField(max_length=7)
    fecha_registro=models.DateTimeField()