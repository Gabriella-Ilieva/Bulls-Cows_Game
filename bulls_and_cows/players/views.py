from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_views, get_user_model, login

from bulls_and_cows.players.forms import RegisterPlayerForm, LogInForm


class RegisterPlayerView(views.CreateView):
    template_name = 'index.html'
    form_class = RegisterPlayerForm
    success_url = reverse_lazy('registered_main')


class LoginPlayerView(auth_views.LoginView):
    form_class = LogInForm
    template_name = 'index.html'
