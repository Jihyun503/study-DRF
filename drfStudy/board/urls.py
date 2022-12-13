from django.contrib import admin
from django.urls import path, include

from board.views import BoardViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
# 첫 번째 인자는 url의 prefix
# 두 번째 인자는 ViewSet
router.register('', BoardViewSet)

urlpatterns = [
    #path('list/', BoardListCreateView.as_view()),
    #path('<int:pk>/', PostDetailView.as_view()),
    path('', include(router.urls)),
]