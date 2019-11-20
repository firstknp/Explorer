from django.urls import path
from .views import user_login ,HomePageView


app_name = "login"

urlpatterns = [
    path('home', HomePageView.as_view(), name='home'),
    path('login',user_login,name='loginpage'),


]