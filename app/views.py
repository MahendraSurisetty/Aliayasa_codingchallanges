from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import PostModel
from .serializers import PostSerializer
from django.http import HttpResponse
from django.db import models

class ListPostsAPIView(generics.ListAPIView):
    queryset = PostModel.objects.all()
    serializer_class = PostSerializer
    
class FilteredPostsAPIView(generics.ListAPIView):
    queryset = PostModel.objects.filter(title=None)
    serializer_class = PostSerializer

class RecentCommentsPostsAPIView(generics.ListAPIView):
    queryset = PostModel.objects.order_by('-comments__publication_date').distinct()
    serializer_class = PostSerializer

class CreatedAtPostsAPIView(generics.ListAPIView):
    queryset = PostModel.objects.order_by('-created_at')
    serializer_class = PostSerializer

class DeleteEmptyPostsAPIView(generics.DestroyAPIView):
    queryset = PostModel.objects.annotate(num_comments=models.Count('comments')).filter(num_comments=0)
    serializer_class = PostSerializer

