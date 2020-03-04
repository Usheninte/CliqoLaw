from django.forms import ModelForm
from .models import NewMatter


class NewMatterForm(ModelForm):
    class Meta:
        model = NewMatter
        fields = ['reference_number', 'nature_of_matter', 'price_estimate', 'hour_estimate', 'hourly_rate']
