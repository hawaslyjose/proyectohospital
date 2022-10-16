from rest_framework import serializers
from dataclasses import field
from Hospital_Backend.models.usuario import Usuario


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model= Usuario
        fields =('username','password','perfil','nombre','apellidos','telefono','genero')