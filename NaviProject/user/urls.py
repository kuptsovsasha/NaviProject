import typing

from django.urls import URLPattern, URLResolver, path

from NaviProject.user.views import CreateUserView, get_user_activity

URL = typing.Union[URLPattern, URLResolver]
URLList = typing.List[URL]

urlpatterns: URLList = [
    path("", CreateUserView.as_view()),
    path("user-activity/", get_user_activity),
]
