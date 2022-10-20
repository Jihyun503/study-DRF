from django.contrib import admin
from django.urls import path

from board.views import PostListCreateView

urlpatterns = [
    path('list/', PostListCreateView.as_view()),
]