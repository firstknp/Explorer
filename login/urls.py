from django.urls import path, include
from .views import user_login, HomePageView, ProfileView, PollsView, user_logout


app_name = "login"

urlpatterns = [
    path('home', HomePageView.as_view(), name='home'),
    path('', user_login,name='loginpage'),
    path('', include('social_django.urls', namespace='social')),
    path('profile', ProfileView.as_view(), name='profile'),
    path('polls', PollsView.as_view(), name='polls'),
    path('logout', user_logout, name='logout'),

]