from rest_framework import serializers
from product.models import Post, comment, Media

class boardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post    
        fields = ['id', 'User_id', 'title', 'content', 'created_at']
class commentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = comment
        fields = ['id', 'Post_id', 'User_id', 'content', 'created_at']
class MediaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Media
        fields = ['id', 'Post_id', 'media_path', 'created_at']