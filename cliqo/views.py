from django.shortcuts import render


def home(request):
    return render(request, 'cliqo/home.html')


def dashboard(request):
    return render(request, 'cliqo/dashboard.html')
