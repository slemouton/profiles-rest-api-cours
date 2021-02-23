from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers

class HelloApiView(APIView):
	"""Test API View"""
	serializer_class = serializers.HelloSerializer
	def get(self, request, format = None):
		""""Renvoie une liste de APIView features"""
		an_apiview = [
		'Uses HTTP methods as funcion (get, post, patch, put, delete',
		'si similar to a trditionelle vue Django',
		'Gives you the most control over your application logic',
		'is mapped manually to URLSs',
		]
		return Response({'message':'Coucou', 'an_apiview':an_apiview})

	def post(self, request):
		"""Create a hello message with our name"""
		serializer = self.serializer_class(data=request.data)
		if serializer.is_valid():
			name = serializer.validated_data.get('name')
			message = f'Hello {name}'
			return Response ({'message': message})
		else:
			return Response(
				serializer.errors,
				status=status.HTTP_400_BAD_REQUEST
				)
	def put(self, request,pk=None):
		"""handle updating an object"""
		return Response({'method': 'PUT'})
	def patch(self, request,pk=None):
		"""handle a partial update of an object"""
		return Response({'method': 'PATCH'})	
	def delete(self,request,):
		"""effacer un objet"""
		return Response({'method': 'DELETE'})