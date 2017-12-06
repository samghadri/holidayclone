from posts.models import Post
from .serializers import PostListSerializer
from rest_framework import generics



class PostListApi(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer
