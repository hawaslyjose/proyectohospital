from ast import Delete
from Hospital_Backend.models.usuario import Usuario
from Hospital_Backend.serializers.usuarioSerializer import UsuarioSerializer
from rest_framework  import views, status
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CrearUsuarioView(views.APIView):
    def post(self, request, **kwargs):
        serializer=UsuarioSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        tokenData={
            "username":request.data["username"],
            "password":request.data["password"],
        }

        tokenSerializer= TokenObtainPairSerializer(data=tokenData)
        tokenSerializer.is_valid(raise_exception=True)
        
        return Response(tokenSerializer.validate_data, status=status.HTTP_201_CREATED)

from Hospital_Backend.models.usuario import Usuario

class UsuarioView(views.APIView):

    def delete(self, request, pk, format=None):
        modelo=Usuario.objects.get(pk=pk)
        modelo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get(self, request, pk, format=None):
        model=Usuario.objects.get(pk=pk)
        serializer=UsuarioSerializer(model)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        model=Usuario.objects.get(pk=pk)
        serializer=UsuarioSerializer(model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)