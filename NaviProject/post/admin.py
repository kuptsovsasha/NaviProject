from django.contrib import admin

from .models import Dislike, Like, Post

# Register your models here.


class LikeInline(admin.TabularInline):
    model = Like
    extra = 0


class DislikeInline(admin.TabularInline):
    model = Dislike
    extra = 0


class PostAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "text",
        "title",
    )
    inlines = (LikeInline, DislikeInline)


admin.site.register(Post, PostAdmin)
