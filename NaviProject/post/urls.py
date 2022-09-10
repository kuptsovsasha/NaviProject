from django.urls import path

from NaviProject.post.views import (
    DislikeCreateAPIView,
    LikeCreateAPIView,
    LikesAnalyticsListView,
    PostCreateAPIView,
)

urlpatterns = [
    path("", PostCreateAPIView.as_view()),
    path("like/", LikeCreateAPIView.as_view()),
    path("dislike/", DislikeCreateAPIView.as_view()),
    path("likes-analytics/", LikesAnalyticsListView.as_view()),
]
