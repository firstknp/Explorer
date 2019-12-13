from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

urlpatterns = [
  path('profile/', views.ProfileView.as_view(), name='profile'),
  path('surveys/create/', views.SurveyCreateView.as_view(), name='survey_create'),
  path('survey-assginment/<int:assignment_id>/', views.SurveyAssignmentView.as_view(), name='survey_assignment'),
  path('survey-results/<int:survey_id>/', views.SurveyResultsView.as_view(), name='survey_results')
    ]