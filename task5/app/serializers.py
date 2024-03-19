# serializers.py

from rest_framework import serializers
from .models import PostModel, CommentModel

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentModel
        fields = ('id', 'comment', 'publication_date')

class PostWithCommentsSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = PostModel
        fields = ('id', 'title', 'author', 'created_at', 'comments')

class PostSerializer(serializers.ModelSerializer):
    total_comments = serializers.SerializerMethodField()

    class Meta:
        model = PostModel
        fields = ('id', 'title', 'author', 'created_at', 'total_comments')

    def get_total_comments(self, obj):
        return obj.comments.count()
