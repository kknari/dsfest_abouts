from rest_framework import viewsets

from django.shortcuts import render
from .models import Post
from .serializers import PostCreateSerializer
from .permissions import CustomReadOnly

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer
    