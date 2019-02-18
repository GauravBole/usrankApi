from django.shortcuts import render
from django.contrib.auth import get_user_model

from rest_framework.generics import RetrieveUpdateAPIView, ListCreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import StageSerializer, StageUserSerializer

from .models import Stage, UserStage
User = get_user_model()

class StageApiView(RetrieveUpdateAPIView):
	"""docstring for StageApiView"""
	queryset = Stage.objects.all()
	serializer_class = StageSerializer
	


class StageListApiView(ListCreateAPIView):
	"""docstring for StageListApiView"""
	serializer_class = StageSerializer
	queryset = Stage.objects.all()

		
class UserStageApiView(RetrieveUpdateAPIView):
	"""docstring for StageApiView"""
	queryset = UserStage.objects.all()
	serializer_class = StageUserSerializer


class UserStageListApiView(ListCreateAPIView):
	"""docstring for StageListApiView"""
	serializer_class = StageUserSerializer
	queryset = UserStage.objects.all()	