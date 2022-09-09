from django.db.models import CharField, Count, F, Value
from django.db.models.functions import Concat, Extract
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions

# Create your views here.
from rest_framework.filters import OrderingFilter
from rest_framework.response import Response

from .filters import LikesAnalyticsFilters
from .models import Like
from .serializers import (
    DislikeCreateSerializer,
    LikeCreateSerializer,
    LikesAnalyticsSerializer,
    PostCreateSerializer,
)


class PostCreateAPIView(generics.CreateAPIView):
    serializer_class = PostCreateSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class LikeCreateAPIView(generics.CreateAPIView):
    serializer_class = LikeCreateSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class DislikeCreateAPIView(generics.CreateAPIView):
    serializer_class = DislikeCreateSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class LikesAnalyticsListView(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = LikesAnalyticsSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = LikesAnalyticsFilters

    def get_queryset(self):
        pre_queryset = Like.objects.filter()
        queryset = (
            pre_queryset.annotate(
                year=(Extract(expression="created_at", lookup_name="year")),
                month=(Extract(expression="created_at", lookup_name="month")),
                day=(Extract(expression="created_at", lookup_name="day")),
                date=Concat(
                    "year",
                    Value("-"),
                    "month",
                    Value("-"),
                    "day",
                    output_field=CharField(),
                ),
            )
            .values("date")
            .order_by("date")
            .annotate(total_count=Count("id"))
        )
        return queryset
