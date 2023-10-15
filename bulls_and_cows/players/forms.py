from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model

from bulls_and_cows.players.models import PlayerAccount


class RegisterPlayerForm(auth_forms.UserCreationForm):
    class Meta:
        model = PlayerAccount
        fields = ('username', 'email', 'profile_picture', 'password1', 'password2')


class LogInForm(auth_forms.AuthenticationForm):
    username = auth_forms.UsernameField(
        widget=forms.TextInput(
            attrs={
                'autofocus': True,
                'placeholder': 'Username',
            }))

    password = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'autocomplete': 'current-password',
                'placeholder': 'Password'
            }
        )
    )
