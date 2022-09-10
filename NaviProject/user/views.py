from django.contrib.auth import get_user_model
from drf_yasg import openapi, utils
from rest_framework import permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView

from NaviProject.user.serializers import UserSerializer

User = get_user_model()


class CreateUserView(APIView):
    permission_classes = (permissions.AllowAny,)

    email = openapi.Parameter(
        "email", openapi.IN_QUERY, description="user email", type=openapi.TYPE_STRING
    )
    password = openapi.Parameter(
        "password",
        openapi.IN_QUERY,
        description="user password",
        type=openapi.TYPE_STRING,
    )
    first_name = openapi.Parameter(
        "first_name",
        openapi.IN_QUERY,
        description="user name",
        type=openapi.TYPE_STRING,
    )
    last_name = openapi.Parameter(
        "last_name",
        openapi.IN_QUERY,
        description="user last_name",
        type=openapi.TYPE_STRING,
    )

    @utils.swagger_auto_schema(
        manual_parameters=[email, password, first_name, last_name]
    )
    def post(self, request):
        serializer = UserSerializer(data=request.GET)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


user_id = openapi.Parameter(
    "user_id", openapi.IN_QUERY, description="user id", type=openapi.TYPE_STRING
)


@utils.swagger_auto_schema(method="get", manual_parameters=[user_id])
@api_view(("GET",))
@permission_classes((permissions.IsAuthenticated,))
def get_user_activity(request, *args, **kwargs):
    """return last user activity by user id"""
    user_id = request.GET.get("user_id", None)
    user = User.objects.filter(id=user_id).last()
    if user:
        user_activity = {
            "last_log_in": user.last_login,
            "last_request": user.last_activity,
        }
        return Response({"detail": user_activity}, status=status.HTTP_200_OK)
    return Response({"detail": "User not found"}, status=status.HTTP_404_NOT_FOUND)
