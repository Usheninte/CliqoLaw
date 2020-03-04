from django.forms import ModelForm
from .models import NewMatter


class NewMatterForm(ModelForm):
    class Meta:
        model = NewMatter
        fields = ['reference_number', 'nature_of_matter', 'price_estimate', 'hourly_rate',
                  'client_name', 'contact_name', 'contact_phone', 'contact_email', 'contact_address',
                  'full_name', 'phone_number', 'role', 'email', 'goal']
