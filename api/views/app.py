from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination

from user_activity_app.models import *
from api.serializers import *
from rest_framework import generics
from rest_framework import viewsets
from rest_framework import serializers




class UserInfoApi(viewsets.ModelViewSet):
	serializer_class = UserSerializer

	def get_queryset(self):
		queryset = activity_period.objects.all()
		return queryset












