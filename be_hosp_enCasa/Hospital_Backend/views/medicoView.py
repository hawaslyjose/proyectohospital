from Hospital_Backend.models.medico import Medico
from Hospital_Backend.serializers.medicoSerializer import MedicoSerializer
from rest_framework  import views, status
from rest_framework.response import Response

class crearpersonalsaludview(views.APIView):
    def post(self, request, format=None):
        serializador=MedicoSerializer(data=request.data)
        if serializador.is_valid():
            serializador.save()
            return Response (serializador.data, status=status.HTTP_201_CREATED)
        return Response(serializador.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, format=None):
        modelo=Medico.objects.all()
        serializar=MedicoSerializer(modelo, many=True)
        return Response(serializar.data)

class consultarpersonalsaludview(views.APIView):
    def put(self, request, pk, format=None):
        modelo=Medico.objects.get(pk=pk)
        serializacion=MedicoSerializer(modelo, data=request.data)
        if serializacion.is_valid():
            serializacion.save()
            return Response (serializacion.data)
        return Response(serializacion.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        modelo=Medico.objects.get(pk=pk)
        modelo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def get(self, request, pk, format=None):
        modelo=Medico.objects.get(pk=pk)
        serializar=MedicoSerializer(modelo)
        return Response (serializar.data)
