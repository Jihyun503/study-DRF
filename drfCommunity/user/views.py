from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from user.models import User
from user.serializers import UserSerializer

class UserListCreateView(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
