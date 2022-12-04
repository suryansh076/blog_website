from django.urls import path
from .views import *
from django.conf import settings
urlpatterns = [
   path('',homes,name="homes"),
   path('loginse/',login,name="login"),
   path('register/',signup,name="signup"),
   path('add-blog/',add_blog,name="add_blog"),
   path('blog_detail/<slug:slug>/',blog_detail,name="blog_detail"),
   path('logout/', LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name='logout'),
   path('your-blogs/',your_blogs,name='your_blogs'),
   path('user-profile/',user_profile,name='user_profile'),
   path('verify-account/<slug:token>/',account_verfication,name='account_verfication')
   
]