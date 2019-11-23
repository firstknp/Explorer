from django.views.generic import TemplateView
from django.contrib.auth import authenticate

class HomePageView(TemplateView):
    template_name = 'homepage.html'