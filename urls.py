from django.conf.urls import url 
from manytomany import views 

urlpatterns = [ 
      url('api/singUp',views.SingUp.as_view()),
      url('api/Login',views.Login.as_view()),
      url('api/getUser',views.UserDetails.as_view()),
      url('api/profileOwnerr',views.profileOwnerr.as_view()),
      url('api/getpost',views.getallposts.as_view()),
      url('api/post',views.post.as_view()),
      url('api/commentonpost',views.comment.as_view()),
      url('api/createProfileOwner',views.createprofileOwner.as_view())
 ]

