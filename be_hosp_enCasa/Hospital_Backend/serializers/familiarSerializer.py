from rest_framework import serializers
from  Hospital_Backend.models.familiar import Familiar


class FamiliarSerializer(serializers.ModelSerializer):
    class Meta:
        model=Familiar
        fields=('username','id_paciente','parentesco','correo')