from django.urls import path, include
from .views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='homepage'),
    path('', include('social_django.urls', namespace='social')),
]