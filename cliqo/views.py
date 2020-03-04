from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from django.views import generic
# from .forms import NewMatterForm
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


class MattersDeleteView(generic.DeleteView):
    model = NewMatter
    template_name_suffix = '_delete'
    success_url = reverse_lazy('cliqo:matters')


# class MattersUpdateView(generic.UpdateView):
#     model = NewMatter
#     fields = ['client_name', 'nature_of_matter', 'price_estimate', 'contact_person']
#     template_name_suffix = '_update'
#     success_url = reverse_lazy('cliqo:matter-focus')


class MattersMainView(generic.DetailView):
    model = NewMatter
    template_name_suffix = '_main'

    def get_context_data(self, **kwargs):
        context = super(MattersMainView, self).get_context_data(**kwargs)
        return context


# def new_matter(request):
#     if request.method == 'POST':
#         new_matter_form = NewMatterForm(request.POST)
#         if new_matter_form.is_valid():
#             reference_number = new_matter_form.cleaned_data['reference_number']
#             nature_of_matter = new_matter_form.cleaned_data['nature_of_matter']
#             price_estimate = new_matter_form.cleaned_data['price_estimate']
#             hourly_rate = new_matter_form.cleaned_data['hourly_rate']
#             new_matter_form.save()
#             return redirect(reverse('cliqo:new-client'))
#     else:
#         new_matter_form = NewMatterForm()
#
#     return render(request, 'cliqo/new_matter.html',
#                   {'new_matter_form': new_matter_form})


# def new_client(request):
#     if request.method == 'POST':
#         new_client_form = ClientInfoForm(request.POST)
#         if new_client_form.is_valid():
#             client_name = new_client_form.cleaned_data['client_name']
#             contact_phone = new_client_form.cleaned_data['contact_phone']
#             contact_email = new_client_form.cleaned_data['contact_email']
#             contact_address = new_client_form.cleaned_data['contact_address']
#             new_client_form.save()
#             return redirect(reverse('cliqo:new-collaborator'))
#     else:
#         new_client_form = ClientInfoForm()
#
#     return render(request, 'cliqo/new_client.html',
#                   {'new_client_form': new_client_form})


# def new_collaborator(request):
#     if request.method == 'POST':
#         new_collaborator_form = CollaboratorInfoForm(request.POST)
#         if new_collaborator_form.is_valid():
#             full_name = new_collaborator_form.cleaned_data['full_name']
#             phone_number = new_collaborator_form.cleaned_data['phone_number']
#             role = new_collaborator_form.cleaned_data['role']
#             email = new_collaborator_form.cleaned_data['email']
#             new_collaborator_form.save()
#             return redirect(reverse('cliqo:matters'))
#     else:
#         new_collaborator_form = CollaboratorInfoForm()
#
#     return render(request, 'cliqo/new_collaborator.html',
#                   {'new_collaborator_form': new_collaborator_form})

