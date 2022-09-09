from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

User = get_user_model()


class CustomTokenObtainPairView(TokenObtainPairView):
    """
    Custom methods based on rest_framework_simplejwt TokenObtainPairView.
    post:
    Takes a refresh type JSON web token and return token pairs if user is activated already.
    """

    serializer_class = TokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        email = self.request.data.get("email", None)
        user = User.objects.filter(email=email).last()
        if not user:
            return Response(
                {"not_user_error": "User not found!"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        if not user.is_active:
            return Response(
                {"not_active_error": "User is not active now!"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        return super().post(request, *args, **kwargs)
