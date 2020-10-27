from django.contrib import admin
from . models import profileOwner,profilePosts,friendComments

# Register your models here.

admin.site.register(profileOwner)
admin.site.register(profilePosts)
admin.site.register(friendComments)


