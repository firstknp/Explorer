from django.contrib.auth.models import User
from django.test import TestCase, Client

class Test(TestCase):
    def register(self):
        self.client = Client()
        self.username = "unittest"
        self.userpass = "12345678"
        self.user = User.objects.create_user(self.username,password=self.userpass)
    

    def test_status_template(self):
        c = self.client
        response = c.get(path='')
        status = response.status_code
        self.assertEqual(status, 200)
        
    def test_template(self):
        c = self.client
        response = c.get(path='')
        self.assertTemplateUsed(response, 'loginpage.html')


    def test_status_register(self):
        c = self.client
        response = c.get(path='/register')
        status = response.status_code
        self.assertEqual(status, 200)

    def test_register(self):
        c = self.client
        response = c.get(path='/register')
        self.assertTemplateUsed(response, 'loginpage.html')


    def test_status_homepage(self):
        c = self.client
        response = c.get(path='/home')
        status = response.status_code
        self.assertEqual(status, 200)

    def test_homepage(self):
        c = self.client
        response = c.get(path='/home')
        self.assertTemplateUsed(response, 'home.html')
        