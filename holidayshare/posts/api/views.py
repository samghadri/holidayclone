from posts.models import Post
from .serializers import PostListSerializer, PostDetailSerializer, PostCreateSerializer
from rest_framework import generics



class PostListApi(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer


class PostDetailApi(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field = 'slug'


class PostCreateApi(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer
