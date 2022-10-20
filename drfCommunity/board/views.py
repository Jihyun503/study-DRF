from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView

from board.models import Post
from board.serializers import PostSerializer

class PostListCreateView(ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()