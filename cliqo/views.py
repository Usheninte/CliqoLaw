from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from django.views import generic
# from .forms import NewMatterForm
from .models import NewMatter, CollaboratorInfo, Outcome


def home(request):
    return render(request, 'cliqo/home.html')


def dashboard(request):
    return render(request, 'cliqo/dashboard.html')


class CreateMatterMain(generic.CreateView):
    model = NewMatter
    fields = ['reference_number', 'client_name',
              'nature_of_matter', 'price_estimate',
              'hour_estimate', 'hourly_rate']
    template_name_suffix = '_create'
    success_url = reverse_lazy('cliqo:matters')

# def new_matter(request):
#     if request.method == 'POST':
#         new_matter_form = NewMatterForm(request.POST)
#         if new_matter_form.is_valid():
#             reference_number = new_matter_form.cleaned_data['reference_number']
#             nature_of_matter = new_matter_form.cleaned_data['nature_of_matter']
#             price_estimate = new_matter_form.cleaned_data['price_estimate']
#             hourly_rate = new_matter_form.cleaned_data['hourly_rate']
#             client_name = new_matter_form.cleaned_data['client_name']
#             contact_name = new_matter_form.cleaned_data['contact_name']
#             contact_phone = new_matter_form.cleaned_data['contact_phone']
#             contact_email = new_matter_form.cleaned_data['contact_email']
#             contact_address = new_matter_form.cleaned_data['contact_address']
#             new_matter_form.save()
#             return redirect(reverse('cliqo:new-client'))
#     else:
#         new_matter_form = NewMatterForm()
#
#     return render(request, 'cliqo/newmatter_create.html',
#                   {'new_matter_form': new_matter_form})


class MattersListView(generic.ListView):
    model = NewMatter

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class MattersDeleteView(generic.DeleteView):
    model = NewMatter
    template_name_suffix = '_delete'
    success_url = reverse_lazy('cliqo:matters')


class MattersMainView(generic.DetailView):
    model = NewMatter
    template_name_suffix = '_main'

    def get_context_data(self, **kwargs):
        context = super(MattersMainView, self).get_context_data(**kwargs)
        context['matters'] = NewMatter.objects.filter(pk=self.get_object().pk)
        return context


class MattersUpdateView(generic.UpdateView):
    model = NewMatter
    fields = ['reference_number', 'client_name',
              'nature_of_matter', 'price_estimate',
              'hour_estimate', 'hourly_rate']
    template_name_suffix = '_update'

    def get_success_url(self):
        user_id = self.kwargs['pk']
        return reverse_lazy('cliqo:matter-focus', kwargs={'pk': user_id})

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

