from django.db import models

# Create your models here.

class PostModel(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

class CommentModel(models.Model):
    post = models.ForeignKey(PostModel, related_name='comments', on_delete=models.CASCADE)
    comment = models.TextField()
    publication_date = models.DateTimeField(auto_now_add=True)

