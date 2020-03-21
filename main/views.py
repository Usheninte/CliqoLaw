from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from .models import *
from .forms import CreateUserForm


def home(request):
    return render(request, 'main/home.html')


def signup_page(request):
    signup_form = CreateUserForm()
    if request.method == 'POST':
        signup_form = CreateUserForm(request.POST)
        if signup_form.is_valid():
            signup_form.save()
            user = signup_form.cleaned_data['username']
            messages.success(request, 'Account was created for ' + user)

            return redirect('main:login')

    context = {'signup_form': signup_form}
    return render(request, 'main/signup.html', context)


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('todo:lists')
        else:
            messages.info(request, 'Username OR Password, is incorrect')

    return render(request, 'main/login.html')


def logout_user(request):
    logout(request)
    return redirect('main:login')
