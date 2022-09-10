from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Post(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, related_name="posts"
    )
    text = models.TextField(max_length=255, blank=True)
    title = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Like(models.Model):
    class Meta:
        unique_together = ["post", "user"]

    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, blank=True, related_name="likes"
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, related_name="likes"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.post.title

    def save(self, *args, **kwargs):
        self.check_existed_dislike()
        return super().save(*args, **kwargs)

    def check_existed_dislike(self):
        """Checks if current user already set dislike for current post and delete if exist"""
        dislike = Dislike.objects.filter(post=self.post, user=self.user).last()
        if dislike:
            dislike.delete()


class Dislike(models.Model):
    class Meta:
        unique_together = ["post", "user"]

    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, blank=True, related_name="dislikes"
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, related_name="dislikes"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.post.title

    def save(self, *args, **kwargs):
        self.check_existed_like()
        return super().save(*args, **kwargs)

    def check_existed_like(self):
        """"Checks if current user already set like for current post and delete if exist"""
        like = Like.objects.filter(post=self.post, user=self.user).last()
        if like:
            like.delete()
