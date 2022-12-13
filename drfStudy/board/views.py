from django.shortcuts import render
from .models import Board
from .serializers import BoardSerializer
from rest_framework.generics import ListCreateAPIView
from rest_framework import viewsets

class BoardViewSet(viewsets.ModelViewSet):
    serializer_class = BoardSerializer
    queryset = Board.objects.all()

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)

