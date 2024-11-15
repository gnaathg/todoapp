from django.shortcuts import render, redirect
from django.views.generic import View
from task.forms import SignUpForm, SignInForm, TodoForm
from django.contrib.auth import authenticate, login, logout
from task.models import ToDo
from django.utils.decorators import method_decorator
from task.decorators import signin_required
from django.views.decorators.cache import never_cache

decs = [signin_required,never_cache]


class SignUpView(View):

    template_name = "signup.html"

    form_class = SignUpForm


    def get(self, request, *args, **kwargs):

        form_instance = self.form_class()

        return render(request, self.template_name, {"form": form_instance})


    def post(self, request, *args, **kwargs):

        form_instance = self.form_class(request.POST)

        if form_instance.is_valid():

            form_instance.save()

            print("Account Created!!")

            return redirect("signin")  # Redirect to "signin" after successful sign-up

        print("Failed to create Account.")

        return render(request, self.template_name, {"form": form_instance})

class SigninView(View):

    template_name = "signin.html"

    form_class = SignInForm

    def get(self, request, *args, **kwargs):

        form_instance = self.form_class()

        return render(request, self.template_name, {"form": form_instance})
    
    def post(self, request, *args, **kwargs):

        form_instance = self.form_class(request.POST)

        if form_instance.is_valid():

            data = form_instance.cleaned_data

            uname = data.get("username")

            pwd = data.get("password")

            user_object = authenticate(request, username=uname, password=pwd)

            if user_object:

                login(request, user_object)

                print('Session started')

                return redirect("index")  # Redirect to "index" after successful sign-in

        print("Invalid credentials")

        return render(request, self.template_name, {"form": form_instance})

@method_decorator(decs,name="dispatch")
class IndexView(View):

    template_name = 'index.html'

    form_class = TodoForm

    def get(self, request, *args, **kwargs):

        qs = ToDo.objects.filter(owner=request.user)

        form = self.form_class()

        return render(request, self.template_name, {'form': form,'data':qs})


    def post(self, request, *args, **kwargs):

        form_instance = self.form_class(request.POST)

        if form_instance.is_valid():

            form_instance.instance.owner=request.user

            form_instance.save()

            return redirect("index")  # Redirect to "index" after creating a new ToDo

        return render(request, self.template_name, {'form': form_instance})

@method_decorator(decs,name="dispatch")
class ToDoDeleteView(View):

    def get(self,request,*args,**kwargs):

        id = kwargs.get("id")

        ToDo.objects.get(id=id).delete()

        return redirect("index")

@method_decorator(decs,name="dispatch")
class ToUpdateView(View):

    def get(self,request,*args,**kwargs):

        id = kwargs.get("id")

        ToDo.objects.filter(id=id).update(status=True)

        return redirect("index")
