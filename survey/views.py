import json
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User, Group, Permission

from django.shortcuts import render, redirect, reverse

from guardian.conf import settings as guardian_settings
from django.views import View
from django.db import transaction

from .models import Survey, Question, Choice



class SurveyCreateView(LoginRequiredMixin, View):
    def get(self, request):
        users = User.objects.all()
        return render(request, 'create_survey.html', {'users': users})

    def post(self, request):
        data = request.POST

        title = data.get('title')
        questions_json = data.getlist('questions')
        assignees = data.getlist('assignees')
        valid = True
        context = {}
        if not title:
            valid = False
            context['title_error'] = 'title is required'

        if not questions_json:
            valid = False
            context['questions_error'] = 'questions are required'

        if not assignees:
            valid = False
            context['assignees_error'] = 'assignees are required'

        if not valid:
            context['users'] = User.objects.all()
            return render(request, 'create_survey.html', context)

        survey = Survey.objects.create(title=title, created_by=request.user)
        for question_json in questions_json:
            question_data = json.loads(question_json)
            question = Question.objects.create(
                text=question_data['text'], survey=survey)
            for choice_data in question_data['choices']:
                Choice.objects.create(
                    text=choice_data['text'], question=question)


        return redirect(reverse('login:home'))



class QuestionViewModel:
    def __init__(self, text):
        self.text = text
        self.choices = []
    def add_survey_response(self, survey_response):
        for choice in self.choices:
            if choice.id == survey_response.choice.id:
                choice.responses += 1
                break


class ChoiceResultViewModel:
    def __init__(self, id, text, responses=0):
        self.id = id
        self.text = text
        self.responses = responses