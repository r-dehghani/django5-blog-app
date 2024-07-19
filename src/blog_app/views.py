from django.shortcuts import render
from rest_framework import generics
from rest_framework import permissions


from .serializers import PostsSerializers
from .models import Posts
from .permissions import IsAuthorOrReadOnly 

class PostListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Posts.objects.all()
    serializer_class = PostsSerializers


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (permissions.IsAdminUser,)
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Posts.objects.all()
    serializer_class = PostsSerializers