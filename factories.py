import factory
from django.contrib.auth import get_user_model
from factory.django import DjangoModelFactory

from NaviProject.post.models import Like, Post

User = get_user_model()


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    first_name = factory.Sequence(lambda n: "First%03d" % n)
    last_name = factory.Sequence(lambda n: "Last%03d" % n)
    email = factory.Faker("email")
    password = factory.Faker("password")


class PostFactory(DjangoModelFactory):
    class Meta:
        model = Post

    user = factory.SubFactory(UserFactory)
    title = factory.Faker("text")
    text = factory.Faker("text")


class LikeFactory(DjangoModelFactory):
    class Meta:
        model = Like

    user = factory.SubFactory(UserFactory)
    post = factory.SubFactory(PostFactory)
