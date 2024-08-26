from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


INPUT_CLASSES = 'w-full px-6 py-4 rounded-xl'

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    username = forms.CharField(widget=forms.TextInput(attrs=
                                                      {'placeholder': 'Your usrename',
                                                       'class': INPUT_CLASSES}))
    email = forms.CharField(widget=forms.EmailInput(attrs=
                                                    {'placeholder': 'Your email address',
                                                     'class' : INPUT_CLASSES}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs=
                                                           {'placeholder': 'Your password',
                                                            'class': INPUT_CLASSES}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs=
                                                           {'placeholder': 'Repeat password',
                                                            'class': INPUT_CLASSES}))

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs=
                                                      {'placeholder': 'Your usrename',
                                                       'class': INPUT_CLASSES}))
    password = forms.CharField(widget=forms.PasswordInput(attrs=
                                                          {'placeholder': 'Your password',
                                                           'class': INPUT_CLASSES}))
