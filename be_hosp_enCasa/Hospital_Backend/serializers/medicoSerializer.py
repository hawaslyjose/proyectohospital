from string import printable
from rest_framework import serializers
from Hospital_Backend.models.medico import Medico

class MedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medico
        fields = ['id', 'especialidad','rol', 'licencia', 'usuario']