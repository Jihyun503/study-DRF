from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from .serializers import UserSerializer
from .models import User

class UserCreateView(CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
