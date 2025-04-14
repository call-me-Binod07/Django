# from django.shortcuts import render,HttpResponse
# from django.contrib.auth.models import User

# from django.db import IntegrityError

# # Create your views here.

# def HomePage(request):
#      return render(request,'home.html')

# def SignupPage(request):
#     if request.method=='POST':
#         uname=request.POST.get('username')
#         if User.objects.filter(username=uname).exists():
#             # Return error message to user
#          return render(request, 'signup.html', {'error': 'Username already exists'})


#         email=request.POST.get('email')
#         pass1=request.POST.get('password1')
#         pass2=request.POST.get('password2')

#         my_user=User.objects.create_user(uname,email,pass1)
#         my_user.save()

#         return HttpResponse("user has beem created sucessfully")


        
        

#     return render(request,'signup.html')

# def LoginPage(request):
#     return render(request,'login.html')

# def logout(request):
#     pass








from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.db import IntegrityError
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='login')
def HomePage(request):
     return render(request,'home.html')

def SignupPage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        # Validate passwords match
        if pass1 != pass2:
            messages.error(request, "Passwords do not match!")
            return render(request, 'signup.html')

        # Check if username exists
        if User.objects.filter(username=uname).exists():
            messages.error(request, "Username already exists!")
            return render(request, 'signup.html')

        # Check if email exists
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered!")
            return render(request, 'signup.html')
        
        try:
            # Create user
            my_user = User.objects.create_user(username=uname, email=email, password=pass1)
            my_user.save()
            messages.success(request, "Account created successfully! Please login.")
            return redirect('login')  # Assuming you have a URL named 'login'
        except IntegrityError:
            messages.error(request, "An error occurred during registration. Please try again.")
            return render(request, 'signup.html')

    return render(request,'signup.html')

def LoginPage(request):
      if request.method == 'POST':
        username1 = request.POST.get('username')
        pass1 = request.POST.get('pass')

        user=authenticate(request,username=username1,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse("incorrect username and password")

      
      return render(request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')






