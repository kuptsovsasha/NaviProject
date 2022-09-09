from rest_framework import serializers

from NaviProject.post.models import Dislike, Like, Post


class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["user", "text", "title"]
        read_only_fields = ["user"]


class LikeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ["user", "post"]
        read_only_fields = ["user"]


class DislikeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dislike
        fields = ["user", "post"]
        read_only_fields = ["user"]


class LikesAnalyticsSerializer(serializers.Serializer):
    date = serializers.CharField()
    total_count = serializers.CharField()
