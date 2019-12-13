from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

urlpatterns = [
  path('home/', views.HomePageView.as_view(), name='home'),
  path('survey/', views.SurveyView.as_view(), name='survey'),
  path('survey/vote/', views.SurveyVote.as_view(), name='survey_vote'),
  path('surveys/create/', views.SurveyCreateView.as_view(), name='survey_create'),
  path('survey-assginment/<int:assignment_id>/', views.SurveyAssignmentView.as_view(), name='survey_assignment'),
  path('survey-results/<int:survey_id>/', views.SurveyResultsView.as_view(), name='survey_results'),
  path('survey-remove/<int:survey_id>/', views.remove_survey, name='survey-remove'),
    ]