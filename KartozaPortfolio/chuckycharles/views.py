from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from chuckycharles.models import Profile, CustomAccountManager
from django import forms
from chuckycharles.forms import ProfileForm

# Create your views here.
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

def home(request):
    form = ProfileForm()
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = authenticate(request, email=email, password=password)
            user = form.cleaned_data.get('user_name')
            messages.success(request, "Account was created for " + user + " successfully!")
            return redirect('login')
    context = {'form': form}
    return render(request, 'home.html', context)

def loginPage(request):
    
    # checking if user details are correct
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)

        # if user details are correct, then login (if user is actually there)
        if user is not None:
            login(request, user)
            messages.info(request, "Login successful!")
            return redirect('dashboard') # redirect to home or index page
        else:
            messages.info(request, "Username or Password is incorrect!")
            return render(request, "login.html")
    context = {}
    return render(request, "login.html", context)

def logoutUser(request):
    logout(request)
    return redirect('login')

def dashboard(request):
    profile = request.POST.get('user_name')
    
    context = {}
    
    return render(request, "dashboard.html", context)

def profileuser(request):
    context = {}
    return render(request, "profile.html", context)

def allusers(request):
    context = {}
    location = request.POST.get('location')
    return render(request, "all_users.html", context)

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")