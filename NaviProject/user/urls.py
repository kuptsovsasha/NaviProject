from django.urls import path

from NaviProject.user.views import CreateUserView, get_user_activity

urlpatterns = [
    path("", CreateUserView.as_view()),
    path("user-activity/", get_user_activity),
]
