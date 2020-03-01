from django.shortcuts import render, redirect, reverse
from django.views import generic
from .forms import NewMatterForm
from .models import NewMatter


def home(request):
    return render(request, 'cliqo/home.html')


def dashboard(request):
    return render(request, 'cliqo/dashboard.html')


class MattersListView(generic.ListView):
    model = NewMatter

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def new_matter(request):
    if request.method == 'POST':
        new_matter_form = NewMatterForm(request.POST)
        if new_matter_form.is_valid():
            client_name = new_matter_form.cleaned_data['client_name']
            nature_of_matter = new_matter_form.cleaned_data['nature_of_matter']
            price_estimate = new_matter_form.cleaned_data['price_estimate']
            contact_person = new_matter_form.cleaned_data['contact_person']
            new_matter_form.save()
            return redirect(reverse('cliqo:matters'))
    else:
        new_matter_form = NewMatterForm()

    return render(request, 'cliqo/new_matter.html',
                  {'new_matter_form': new_matter_form})
