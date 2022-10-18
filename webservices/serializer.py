from django.shortcuts import render
from rest_framework import serializers
from principal.models import *

class universal_serializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model  = Universal
		fields = ('id','nombre','apellido','documento','genero','tipo_de_rh','empresa_universidad','rol_de_usuario','imagen_universi')