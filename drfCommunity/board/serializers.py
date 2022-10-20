from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.Serializer):
    id = serializers.IntegerField(help_text="게시글id", read_only=True)
    user = serializers.CharField(help_text="유저")
    category = serializers.CharField(help_text='카테고리')
    title = serializers.CharField(help_text='제목', allow_null=True)
    content = serializers.CharField(help_text='내용', allow_null=True)

    def create(self, validated_data):
        return Post.objects.create(**validated_data)