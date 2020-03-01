from django.shortcuts import render, redirect
from .forms import NewMatterForm


def home(request):
    return render(request, 'cliqo/home.html')


def dashboard(request):
    return render(request, 'cliqo/dashboard.html')


def matters(request):
    return render(request, 'cliqo/matters.html')

def new_matter(request):
    if request.method == 'POST':
        new_matter_form = NewMatterForm(request.POST)
        if new_matter_form.is_valid():
            client_name = new_matter_form.cleaned_data['client_name']
            nature_of_matter = new_matter_form.cleaned_data['nature_of_matter']
            price_estimate = new_matter_form.cleaned_data['price_estimate']
            contact_person = new_matter_form.cleaned_data['contact_person']
            new_matter_form.save()
            return redirect(reversed('cliqo:matters'))
    else:
        new_matter_form = NewMatterForm()

    return render(request, 'cliqo/new_matter.html',
                  {'new_matter_form': new_matter_form})
