from django.urls import path, include
from .views import user_login,  ProfileView, PollsView ,register



app_name = "login"

urlpatterns = [
    path('',user_login,name='loginpage'),
    path('', include('social_django.urls', namespace='social')),
    path('register/',register,name='register'),

]