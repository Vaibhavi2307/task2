from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from .serializers import UserSerializer

class UserRegister(ListCreateAPIView):
    serializer_class=UserSerializer