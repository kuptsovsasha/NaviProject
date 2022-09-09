import typing

from django.urls import URLPattern, URLResolver, path

from NaviProject.post.views import (
    DislikeCreateAPIView,
    LikeCreateAPIView,
    LikesAnalyticsListView,
    PostCreateAPIView,
)

URL = typing.Union[URLPattern, URLResolver]
URLList = typing.List[URL]

urlpatterns: URLList = [
    path("", PostCreateAPIView.as_view()),
    path("like/", LikeCreateAPIView.as_view()),
    path("dislike/", DislikeCreateAPIView.as_view()),
    path("likes-analytics/", LikesAnalyticsListView.as_view()),
]
