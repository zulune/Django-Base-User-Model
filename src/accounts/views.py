from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import CreateView, FormView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth import get_user_model, login, authenticate

from .forms import LoginForm, RegisterForm
# Create your views here.


class RegisterView(SuccessMessageMixin, CreateView):
    form_class = RegisterForm
    template_name = 'accounts/register.html'
    success_url = '/'
    success_message = 'Thank you for register!'


class LoginView(SuccessMessageMixin, FormView):
    form_class = LoginForm
    template_name = 'accounts/login.html'
    success_url = '/'
    success_message = 'Hello to the site!'

    def form_valid(self, form):
        request = self.request
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None and user.is_active:
            login(request, user)
            return super(LoginView, self).form_valid(form)
        else:
            return super(LoginView, self).form_invalid(form)