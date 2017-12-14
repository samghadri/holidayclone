from rest_framework.serializers import ModelSerializer
from posts.models import Post


class PostListSerializer(ModelSerializer):
    class Meta:

        model = Post
        fields =['user','message','created_date', 'slug', 'group']

class PostDetailSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ['slug', 'message','created_date','group']


class PostCreateSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ['message', 'group']
