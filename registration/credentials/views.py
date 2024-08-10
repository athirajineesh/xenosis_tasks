import email

from django.contrib import messages, auth
from django.shortcuts import render, redirect
from django.contrib.auth.models import User


def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is  not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid credentials")
            return  redirect('login')
    return render(request,"login.html")
def register(request):
    if request.method=='POST':
        username=request.POST['username']
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        mail = request.POST['email']
        password= request.POST['password']
        cpass = request.POST['confirm password']
        if password==cpass:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username exists")
                return redirect('register')
            elif User.objects.filter(email=mail).exists():
                messages.info(request, "email exists")
                return redirect('register')
            else:
              user=User.objects.create_user(username=username,password=password,first_name=firstname,last_name=lastname,email=mail)
              user.save()
              return redirect('login')
        else:
            messages.info(request,"password not matching")
            return redirect('register')
        return redirect('/')
    return render(request,"register.html")
def logout(request):
    auth.logout(request)
    return redirect('/')
# Create your views here.
