from django.shortcuts import render

# Create your views here.
# views.py

from rest_framework import generics
from .models import PostModel
from .serializers import PostWithCommentsSerializer, PostSerializer

class PostListWithComments(generics.ListAPIView):
    queryset = PostModel.objects.all()
    serializer_class = PostWithCommentsSerializer

class FilteredPostList(generics.ListAPIView):
    queryset = PostModel.objects.filter(title__isnull=True)
    serializer_class = PostSerializer

class PostsByRecentComments(generics.ListAPIView):
    queryset = PostModel.objects.order_by('-comments__publication_date')
    serializer_class = PostSerializer

class PostsByCreatedAt(generics.ListAPIView):
    queryset = PostModel.objects.order_by('-created_at')
    serializer_class = PostSerializer

class DeletePostWithNoComments(generics.DestroyAPIView):
    queryset = PostModel.objects.all()

    def perform_destroy(self, instance):
        if instance.comments.count() == 0:
            instance.delete()

