from django import forms

from django.contrib.auth.forms import UserCreationForm

from task.models import User

class SignUpForm(UserCreationForm):

    class Meta:

        model = User

        fields = ["username","password1","password2","phone","email"]

class SignInForm(forms.Form):

    username = forms.CharField()

    password = forms.CharField()

    