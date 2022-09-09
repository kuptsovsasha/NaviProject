import typing

from django.urls import URLPattern, URLResolver, path
from rest_framework_simplejwt.views import TokenRefreshView

from .jwt_views import CustomTokenObtainPairView

URL = typing.Union[URLPattern, URLResolver]
URLList = typing.List[URL]

urlpatterns: URLList = [
    path("token/", CustomTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
