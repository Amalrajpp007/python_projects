from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


def register(request):
    if request.method=='POST':
     username1=request.POST['user_name']
     first_name=request.POST['fname']
     last_name = request.POST['lname']
     email = request.POST['email']
     password = request.POST['pass']
     password2 = request.POST['pass2']
     if password==password2:
        if User.objects.filter(username=username1).exists():
            messages.info(request,'username taken')
            return redirect('register')
        if User.objects.filter(password=password2).exists():
            messages.info(request,'password taken')
            return redirect('register')
        if User.objects.filter(email=email).exists():
            messages.info(request,'email taken')
            return redirect('register')

        user=User.objects.create_user(username=username1,email=email,first_name=first_name,last_name=last_name,password=password)
        user.save()
        return redirect('/')
     else:
        messages.info(request,'password not matching')
    return render(request,'register.html')

def login(request):

    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['pass']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect ('/')
        else:
             messages.info(request,'invalid credentials')
    return render(request,'login.html')
def logout(request):
    auth.logout(request)
    return redirect('/')