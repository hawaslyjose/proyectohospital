from Hospital_Backend.models.signos import Signos_vitales
from rest_framework import serializers

class SignosVitalesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Signos_vitales
        fields=('id_paciente','oximetria','frec_cardiaca','frec_respiratoria','temperatura','glicemias','presion','fecha_registro')