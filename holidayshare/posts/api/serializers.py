from rest_framework.serializers import ModelSerializer
from posts.models import Post

class PostListSerializer(ModelSerializer):
    class Meta:
        
        model = Post
        fields =['user','message','created_date']
