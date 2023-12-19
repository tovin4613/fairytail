from rest_framework import serializers
from product.models import Post

class boardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post    
        fields = ['id', 'User_id', 'title', 'content', 'created_at']