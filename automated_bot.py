import random

import environ

from factories import LikeFactory, PostFactory, UserFactory

env = environ.Env()

USERS_NUM = env("USERS_NUM")
POSTS_BY_USER = env("POSTS_BY_USER")
LIKES_BY_USER = env("LIKES_BY_USER")


def create_mock_data():

    users = []
    for _ in range(int(USERS_NUM)):
        user = UserFactory()
        users.append(user)
    posts = []
    for _ in range(int(POSTS_BY_USER)):
        user = random.choice(users)
        post = PostFactory(user=user)
        posts.append(post)

    for _ in range(int(LIKES_BY_USER)):
        user = random.choice(users)
        post = random.choice(posts)
        LikeFactory(user=user, post=post)


if __name__ == "__main__":
    create_mock_data()