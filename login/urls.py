from django.urls import path, include
<<<<<<< HEAD
from .views import user_login, HomePageView, ProfileView, PollsView, user_logout
=======
from .views import user_login ,HomePageView ,register
>>>>>>> master


app_name = "login"

urlpatterns = [
    path('home', HomePageView.as_view(), name='home'),
    path('', user_login,name='loginpage'),
    path('', include('social_django.urls', namespace='social')),
<<<<<<< HEAD
    path('profile', ProfileView.as_view(), name='profile'),
    path('polls', PollsView.as_view(), name='polls'),
    path('logout', user_logout, name='logout'),
=======
    path('register',register,name='register'),

>>>>>>> master

]