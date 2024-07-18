from django.shortcuts import render
from rest_framework import generics

from .serializers import PostsSerializers
from .models import Posts

class PostListView(generics.ListCreateAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializers


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializers