from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    #user 
    class Meta:
        model = Post
        fields = '__all__'