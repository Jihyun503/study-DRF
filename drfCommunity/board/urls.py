from django.contrib import admin
from django.urls import path, include

from board.views import PostListCreateView, PostDetailView, PostViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
# 첫 번째 인자는 url의 prefix
# 두 번째 인자는 ViewSet
router.register('post', PostViewSet)

urlpatterns = [
    path('list/', PostListCreateView.as_view()),
    path('<int:pk>/', PostDetailView.as_view()),
    path('', include(router.urls))
]