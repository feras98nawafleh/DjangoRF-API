from django.shortcuts import render
from rest_framework import generics
from .serializers import PostSerialzer
from .models import Post

# CR views
class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerialzer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerialzer