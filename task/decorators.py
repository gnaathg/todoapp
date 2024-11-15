from django.shortcuts import redirect,render
def signin_required(fn):

    def wrapper(request,*args,**kwargs):

        if not request.user.is_auntheticated:

            return redirect("signin")
        
        return render(request,*args,**kwargs)
    
    return wrapper