from django.shortcuts import render
from django.contrib.auth import get_user_model

from rest_framework.generics import RetrieveUpdateAPIView, ListCreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import AuthUserSerializers

User = get_user_model()

class AuthUserListApiView(ListCreateAPIView):
	"""docstring for AuthUserListApiView"""

	queryset = User.objects.all()
	serializer_class = AuthUserSerializers


class AuthUserApiView(RetrieveUpdateAPIView):
	"""docstring for AuthUserApiView"""
	
	serializer_class = AuthUserSerializers
	queryset = User.objects.all()
