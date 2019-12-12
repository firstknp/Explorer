from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required




class HomePageView(TemplateView):
    template_name = 'home.html'

class ProfileView(TemplateView):
    template_name = 'profile.html'

class PollsView(TemplateView):
    template_name = 'polls.html'

def index(request):
    return render(request, 'login/index.html')


@login_required
def special(request):
    return HttpResponse("You are logged in!")


@login_required
def user_logout(request):
    logout(request)
<<<<<<< HEAD
    # return HttpResponseRedirect(reverse('index'))
    # return redirect('loginpage')
    return render(request, "loginpage.html", {})
=======
    return redirect(reverse('login:user_login'))
>>>>>>> master


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                if request.user.is_superuser:
                    return redirect("admin:index")
                else:
                    return render(request, "home.html", {})
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Failed to login.")
            return HttpResponse("Invalid login details given")
    else:
        return render(request, "loginpage.html", {})



def register(request):
    template = 'loginpage.html'
    
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                form.cleaned_data['username'], 
                form.cleaned_data['email'], 
                form.cleaned_data['password1']
            )
            user.save()

    else:
        form = RegisterForm()

    return render(request, template, {'form': form})