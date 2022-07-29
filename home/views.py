import re
from django.http import HttpResponse
from django.shortcuts import render , redirect
from requests import request
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login
# Create your views here.
def index(request):
	if request.user.is_anonymous:
		return render(request,'login.html')
	return render(request,'index.html')
def loginuser(request):
	if request.method=='POST':
		usern=request.POST.get('username')
		passw=request.POST.get('password')
		user = authenticate(username=usern,password=passw)
		if user is not None:
			login(request,user)
			return redirect('/')
		else:
			return render(request,'login.html')
	return render(request,'login.html')
def logoutuser(request):
	return redirect("/login")
def createaccount(request):
	return render(request,'newuser.html')
def newuser(request):
	if request.method=='POST':
		userName = request.POST.get('usern', None)
		userPass = request.POST.get('passw', None)
		userMail = request.POST.get('email', None)
		user = User(username=userName,
                                 email=userMail,
                                 password=userPass)
		user.save()
		return redirect(request,'/')
	return redirect(request,'/')