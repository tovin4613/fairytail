from rest_framework import serializers
from product.models import Post, comment, Media, User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields =['id','User','created_at']


class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = ['id', 'Post', 'media_path', 'created_at']
        
class commentSerializer(serializers.ModelSerializer):
    class Meta:
        model = comment
        fields = ['id', 'Post', 'User_id', 'content', 'created_at']

class PostSerializer(serializers.ModelSerializer):
    Medias=MediaSerializer(many=True, read_only=True)
    User = UserSerializer(many=True, read_only=True)
    comment=commentSerializer(many=True, read_only=True)
    class Meta:
        model = Post    
        fields = ['id', 'User', 'title', 'content','Medias', 'created_at','comment']
        

        
# class PostDetailSerializer(serializers.ModelSerializer):
#     comment=commentSerializer(many=True,read_only=True)
#     User=UserSerializer(many=True, read_only=True)
#     Medias=MediaSerializer(many=True, read_only=True)
#     class Meta:
#         model=Post
#         fields=['id','User','title','content','Medias','created_at','comment']