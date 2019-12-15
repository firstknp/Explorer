from django.contrib.auth.models import User
from django.test import TestCase, Client

class Test(TestCase):
    def setUp(self):
        self.client = Client()
        self.username = "unittest"
        self.userpass = "12345678"
        self.user = User.objects.create_user(self.username,password=self.userpass)


    def test_status_home(self):
        c = self.client
        response = c.get(path='/home/')
        status = response.status_code
        self.assertEqual(status, 200)
        
    def test_home(self):
        c = self.client
        response = c.get(path='/home/')
        self.assertTemplateUsed(response, 'survey/home.html')


    def test_status_survey(self):
        self.client.force_login(self.user)
        response = self.client.get(path='/survey/')
        status = response.status_code
        self.assertEqual(status, 200)

    def test_survey(self):
        self.client.force_login(self.user)
        response = self.client.get(path='/survey/')
        self.assertTemplateUsed(response, 'survey/survey.html')


    def test_status_survey_vote(self):
        self.client.force_login(self.user)
        response = self.client.get(path='/survey/vote/')
        status = response.status_code
        self.assertEqual(status, 200)

    def test_survey_vote(self):
        self.client.force_login(self.user)
        response = self.client.get(path='/survey/vote/')
        self.assertTemplateUsed(response, 'survey/survey_vote.html')


    def test_status_surveys_create(self):
        self.client.force_login(self.user)
        response = self.client.get(path='/surveys/create/')
        status = response.status_code
        self.assertEqual(status, 200)

    def test_survey_surveys_create(self):
        self.client.force_login(self.user)
        response = self.client.get(path='/surveys/create/')
        self.assertTemplateUsed(response, 'survey/create_survey.html')
        