from django.contrib import admin
from django.urls import path

from user.views import UserListCreateView

urlpatterns = [
    path('list/', UserListCreateView.as_view()),
]