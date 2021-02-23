from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
	"""Test API View"""
	def get(self, request, format = None):
		""""Renvoie une liste de APIView features"""
		an_apiview = [
		'Uses HTTP methods as funcion (get, post, patch, put, delete',
		'si similar to a trditionelle vue Django',
		'Gives you the most control over your application logic',
		'is mapped manually to URLSs',
		]
		return Response({'message':'Coucou', 'an_apiview':an_apiview})