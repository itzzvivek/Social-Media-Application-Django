from django.contrib import admin

from .models import Profile,Post,FollowerCount,LikePost

admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(FollowerCount)
admin.site.register(LikePost)
