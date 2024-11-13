from django.shortcuts import render,redirect

# Create your views here.

from django.views.generic import View

from task.forms import SignUpForm,SignInForm

from django.contrib.auth import authenticate,login,logout

class SignUpView(View):

    template_name = "signup.html"

    form_class =SignUpForm

    def get(self,request,*args,**kwargs):

        form_instance = self.form_class()

        return render(request,self.template_name,{"form":form_instance})
    
    def post(self,request,*args,**kwargs):


        form_data = request.POST

        form_instance = self.form_class(form_data)

        if form_instance.is_valid():

            form_instance.save()

            print("Account Created!!")

            return redirect("signup")
        
        print("Failed to create Account.")
    
        return render(request,self.template_name,{"form":form_instance})

class SigninView(View):

    template_name = "signin.html"

    form_class = SignInForm

    def get(self,request,*args,**kwargs):

        form_instance = self.form_class

        return render(request,self.template_name,{"form":form_instance})
    
    def post(self,request,*args,**kwargs):

        form_data = request.POST

        form_insatnce = self.form_class(form_data)

        if form_insatnce.is_valid():

            data = form_insatnce.cleaned_data

            uname = data.get("username")

            pwd = data.get("password")

            user_object = authenticate(request,username = uname,password = pwd)

            if user_object:

                login(user_object)

                print('session started')

                return redirect("signin")

        print("invalid credential")

        return render(request,self.template_name,{"form":form_insatnce})
