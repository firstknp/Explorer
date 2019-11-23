from django.urls import path, include
from .views import user_login ,HomePageView


app_name = "login"

urlpatterns = [
    path('home', HomePageView.as_view(), name='home'),
    path('login',user_login,name='loginpage'),
    path('', include('social_django.urls', namespace='social')),


]