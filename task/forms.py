from django import forms

from django.contrib.auth.forms import UserCreationForm

from task.models import User ,ToDo

class SignUpForm(UserCreationForm):

    password1=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"})),
    password2=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))


    class Meta:

        model = User

        fields = ["username","password1","password2","phone","email"]

        widgets = {
            "username" : forms.TextInput(attrs={"class":"form-control"}), 
            "email" : forms.EmailInput(attrs={"class":"form-control"}),
            "phone" : forms.PasswordInput(attrs={"class":"form-control"})
        }

class SignInForm(forms.Form):

    username = forms.CharField()

    password = forms.CharField()

class TodoForm(forms.ModelForm):

    class Meta:

        model = ToDo

        fields = ['title']
