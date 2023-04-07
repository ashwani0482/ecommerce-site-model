from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def login_page(request):
    
    if request.method =='POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user_obj = User.objects.filter(username = email)

        if not user_obj.exists():
            messages.warning(request, "Provided email does't exists, you can continue with SignUp!!")
            return HttpResponseRedirect(request.path_info)
        
        if not user_obj[0].profile.is_email_verified:
            messages.warning(request, "Verify your email")
            return HttpResponseRedirect(request.path_info)
            
        
        user_obj= authenticate(username=email , password=password)
        if user_obj:
            login(request, user_obj)
            return redirect('/')

        messages.warning(request, 'Invalid Cerendentials')

    return render(request, 'accounts/login.html')

def register_page(request):
    
    
    if request.method =='POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user_obj = User.objects.filter(username = email)

        if user_obj.exists():
            messages.warning(request, 'Provided email already exists !!')
            return HttpResponseRedirect(request.path_info)
        
        user_obj = User.objects.create(first_name=first_name, last_name=last_name, email=email, username=email )

        user_obj.set_password(password)
        user_obj.save()

        messages.success(request, 'An email has been sent to your mail')
        return HttpResponseRedirect(request.path_info) 
            
    return render(request, 'accounts/register.html')