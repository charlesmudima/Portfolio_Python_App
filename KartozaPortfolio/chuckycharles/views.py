from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from chuckycharles.models import Profile, CustomAccountManager
from django import forms
from chuckycharles.forms import ProfileForm

# Create your views here.
from django.http import HttpResponse


def home(request):
    form = ProfileForm()

    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            # return redirect('home')
    context = {'form': form}
    return render(request, 'home.html', context)

def login(request):
    return render(request, "login.html")


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")