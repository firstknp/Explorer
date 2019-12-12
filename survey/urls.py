from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

urlpatterns = [
  path('surveys/create/', views.SurveyCreateView.as_view(), name='survey_create'),
    ]