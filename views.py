
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.http.response import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from rest_framework import status 
from .models import profileOwner,profilePosts,friendComments
from django.shortcuts import render
from django.http import HttpResponse
import json



class SingUp(APIView):

    def post(self,request):
         datalist = {}
         datalist = request.data
         Username = datalist['Username']
         Email  = datalist['Email']
         Password = datalist['Password']
         Password1 = datalist['Password1']
         if Password == Password1:
             user = User.objects.create_user(Username,Email,Password)
         else:
            return JsonResponse({"password":"not matched"})
       
         return JsonResponse({"User Created Sucessfully":"ok"})

class Login(APIView):

    def post(self,request):
         username = request.POST.get('username')
         password = request.POST.get('password')

         user = authenticate(request, username=username, password=password)
         if user is not None:
             return JsonResponse({"login":"Sucessfully"})
         else:
            
             return JsonResponse({"Wrong1":"credential"})

class UserDetails(APIView):
    def get(self,request):
        users = User.objects.filter(pk=3)
        userList =User.objects.filter(pk=2).values()
        print("---------------------------",users)
        print("--------------------------------",userList)
        return JsonResponse({"Wrong1":"credential"})

class profileOwnerr(APIView):

    def post(self,request):
        datalist = {}
        datalist = request.data
        location = datalist['location']
        about_me = datalist['about_me']
        print("-------------------------",datalist)
        r = profileOwner(location=location,about_me=about_me)
        r.save()

        return JsonResponse({"User Created Sucessfully":"ok"})


class getallposts(APIView):

    def get(self,request):
        courses = profileOwner.objects.filter(friend=profileOwner.objects.get(id=1))
        linked_content = []
        name =[]
        for content in courses:
            # name.append(content)
            # content ={ 'posts':content.id}
            name.append(content.id)
            linked_content.append(content)
        print('---------------------------------------',linked_content)
        print('pppppppppppppppppppppppppppppppppppppppppp',name)
        post1=[]
        post = profilePosts.objects.filter(pk__in=name)
        print('post--------------------------',post)
        for i in post:
            i ={'post':i.posts}
            print('-----------------------',i)
            post1.append(i)
        print('iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii',post1)

        return JsonResponse(post1 , safe=False)



     
       
        # tutorial_list = []

        # for tutorial in tutorials:
        #     #   print(tutorial.title)
        #       tutorial ={ 'id':tutorial.id,'title':tutorial.title,'description':tutorial.description,'published':tutorial.published}
        #       tutorial_list.append(tutorial)
        # #print(tutorial_list)
    
        
        # return JsonResponse(tutorial_list, safe=False)
    
        # ---------------------------------------------------------------------
    #     class getallposts(APIView):

    # def get(self,request):
    #     # a=profileOwner.objects.get(name=1).friend.all()
    #     a = profileOwner.objects.filter(friend=profileOwner.objects.get(id=2))
    #     print('-----------------------------------------',a)

    #     # profileOwner.objects.filter(profileOwner.friend).distinct()

    #     # profilepost = profilePosts.objects.all()
    #     # a=profileOwner.objects.filter(friend=profileOwner.objects.get(id=2))
        
    #     # a=profilePosts.objects.filter(profileowner=111)

    #     post_list = []
    #     # # for post in profilepost:
    #     # #     #   print(tutorial.title)
    #     # #       post ={ post.id:post.posts}
    #     # #       post_list.append(post)
    #     # # # print(post_list)
    #     for i in a:
    #         #   print(tutorial.title)
    #           post ={ i.id:i.name}
    #           post_list.append(i)
    #     print(post_list)
    #     # return JsonResponse(post, content_type="application/json")

        
    #     return JsonResponse(post, safe=False)
        # ---------------------------------------------------------------------


class post(APIView):

    def post(self,request):
        datalist = {}
        datalist = request.data
        post1 = datalist['posts']
        profileowner = datalist['profileowner']
        p = profilePosts(posts=post1, profileowner_id= profileowner)
        p.save()

        return JsonResponse(datalist, safe=False)
        
        # return JsonResponse({"dev":"ok"})


class comment(APIView):

    def post(self,request):
        datalist = {}
        datalist = request.data
        comments = datalist['comments']
        profileposts_id= datalist['profileposts_id']
        friend_id = datalist['friend_id']
        try:
            one_entry = profilePosts.objects.get(pk=profileposts_id)
            
        except:
             return JsonResponse({"kindly enter correct ":"profileposts_id"})

        try:
            one_entry2 =profileOwner.objects.get(pk=friend_id) 

        except:
             return JsonResponse({"kindly enter correct ":"friend_id"})

        courses = profileOwner.objects.filter(friend=profileOwner.objects.get(id=profileposts_id))
        linked_content = []
        for content in courses:
            content =content.id
            linked_content.append(content)

        print('................................................',linked_content)
        print('--------------------------------------------',friend_id)   

        if int(friend_id) in linked_content:
            c = friendComments(comments=comments, profileposts_id=profileposts_id,friend_id=friend_id)
            c.save()
            return JsonResponse({"Successfully ":"Commented"})
        else:
            return JsonResponse({"Not Posted Comment":"As he is not his friend"})
    

        # for x in linked_content:
        #     print('.............................................. ..',linked_content)
        #     print('---------------xxxxxxxx------------',x)
        #     print('**********************************fffffffffff**',friend_id)
        #     if x == friend_id:
        #         print('tttttttttttttttttttttttttttttttttttttttttttttttttttttttttt')
        #         c = friendComments(comments=comments, profileposts_id=profileposts_id,friend_id=friend_id)
        #         c.save()
        #     return JsonResponse(datalist, safe=False)
                
        
    


        # if friend_id not in linked_content:
        #     c = friendComments(comments=comments, profileposts_id=profileposts_id,friend_id=friend_id)
        #     c.save()
        #     return JsonResponse(datalist, safe=False)
            
            
        
        # return JsonResponse({"dev":"ok"})

# In Progress 
class createprofileOwner(APIView):

    def post(self,request):
        print('-----------------------',request)
        datalist = {}
        datalist = request.data
        location = datalist['location']
        about_me= datalist['about_me']
        name = datalist['name']
        friend=datalist['friend']
        name1 =User.objects.all()
        linked_content_name = []
        for content in name1:
            content =content
            linked_content_name.append(content)

        b =  User.objects.create_superuser(name,'v@myproject.com', '12345')
        b.save()

        courses = profileOwner.objects.all()
    
        linked_content = []
        for content in courses:
            content =content.name
            linked_content.append(content)

            
        if name in str(linked_content_name):
            if friend in str(linked_content_name):
                c = profileOwner(name=name,location=location,about_me=about_me,friend=friend)
                c.save()
                return JsonResponse({"Successfully ":"okkkkkkkkkkkkkk"})
            else:
                return JsonResponse({"Not Posted Comment":"99999999999999"})

        else:

            return JsonResponse({"dev":"ok"})


        
        





  

        
       

