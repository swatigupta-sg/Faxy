from django.shortcuts import render
from django.contrib.auth.views import LoginView,LogoutView
from django.views import View
from auth import forms
from django.contrib.auth import login
from django.http import HttpResponseRedirect

class Login(LoginView):
    template_name = 'auth/login.html'

class Logout(LogoutView):
    pass

class Signup(View):
    def get(self, request):
        context = {
            "form" : forms.SignUpForm()
        }
        return render(request, 'auth/signup.html', context)

    def post(self, request):
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return HttpResponseRedirect('/')

        context = {
            "form" : form
        }
        return render(request, 'auth/signup.html', context)
        