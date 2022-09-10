from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from NaviProject.views import healthy

swagger_view = get_schema_view(
    openapi.Info(
        title="STAR NAVI API",
        default_version="v1",
        description="Overview of STAR NAVI API",
        terms_of_service="",
        contact=openapi.Contact(email="kuptsovsasha@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path(
        "", swagger_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"
    ),
    path("healthy/", healthy),
    path("admin/", admin.site.urls),
    path("auth/", include("NaviProject.custom_jwt.urls")),
    path("user/", include("NaviProject.user.urls")),
    path("post/", include("NaviProject.post.urls")),
]
