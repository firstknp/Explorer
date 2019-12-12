import json
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User, Group, Permission
from django.db import transaction

from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views import View

from guardian.conf import settings as guardian_settings
from guardian.mixins import PermissionRequiredMixin
from guardian.shortcuts import assign_perm


from .models import Survey, Question, Choice, SurveyAssignment



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

        perm = Permission.objects.get(codename='view_surveyassignment')
        for assignee in assignees:
            assigned_to = User.objects.get(pk=int(assignee))
            assigned_survey = SurveyAssignment.objects.create(
                survey=survey,
                assigned_by=request.user,
                assigned_to=assigned_to
            )
            assign_perm(perm, assigned_to, assigned_survey)
            
        return redirect(reverse('login:home'))

class SurveyAssignmentView(PermissionRequiredMixin, View):
    permission_required = 'survey.view_surveyassignment'

    def get_object(self):
        self.obj = get_object_or_404(
            SurveyAssignment, pk=self.kwargs['assignment_id'])
        return self.obj

    def get(self, request, assignment_id):
        return render(request, 'survey/survey_assignment.html', {'survey_assignment': self.obj})

    def post(self, request, assignment_id):
        context = {'validation_error': ''}
        save_id = transaction.savepoint()
        try:
            for question in self.obj.survey.questions.all():
                question_field = f"question_{question.id}"
                if question_field not in request.POST:
                    context['validation_error'] = 'All questions require an answer'
                    break

                choice_id = int(request.POST[question_field])
                choice = get_object_or_404(Choice, pk=choice_id)
                SurveyResponse.objects.create(
                    survey_assigned=self.obj,
                    question=question,
                    choice=choice
                )

            if context['validation_error']:
                transaction.savepoint_rollback(save_id)
                return render(request, 'survey/survey_assignment.html', context)

            transaction.savepoint_commit(save_id)
        except:
            transaction.savepoint_rollback(save_id)

        return redirect(reverse('profile'))

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