from django.db import models
from django.contrib.auth.models import User


class profileOwner(models.Model):
    name = models.OneToOneField(User,on_delete=models.CASCADE)
    location = models.CharField(max_length=100,default='')
    about_me = models.TextField(max_length=100)
    friend = models.ManyToManyField("self", blank=True)

    def __str__(self):
        return self.name.username

    # profilefriends = models.ManyToManyField('profileFriends') 
class profilePosts(models.Model):
    profileowner = models.ForeignKey(profileOwner,on_delete=models.CASCADE)
    posts = models.CharField(max_length=100,default='')

    def __str__(self):
        return self.posts

class friendComments(models.Model):
    comments = models.CharField(max_length=500,)
    profileposts = models.ForeignKey(profilePosts,on_delete=models.CASCADE)
    friend = models.ForeignKey(profileOwner,on_delete=models.CASCADE)
    

    def __str__(self):
        return self.comments

    

# class profileFriends(models.Model):
#     # friend = models.ManyToManyField(profileOwner)
#     # friends = models.OneToOneField(User,on_delete=models.CASCADE,default='')
#     blood_groups = models.CharField(max_length=10,default='B+')
#     comments = models.TextField(max_length=500,)
#     profileowner = models.ForeignKey(profileOwner,on_delete=models.CASCADE)


#     def __str__(self):
#         return self.friends.username




