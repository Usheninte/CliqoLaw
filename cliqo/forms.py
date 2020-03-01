from django.forms import ModelForm
from .models import NewMatter


class NewMatterForm(ModelForm):
    class Meta:
        model = NewMatter
        fields = ['client_name', 'nature_of_matter', 'price_estimate', 'contact_person']

