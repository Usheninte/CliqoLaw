from django.forms import ModelForm
from .models import NewMatter, ClientInfo, CollaboratorInfo


class NewMatterForm(ModelForm):
    class Meta:
        model = NewMatter
        fields = ['reference_number', 'nature_of_matter', 'price_estimate']


class ClientInfoForm(ModelForm):
    class Meta:
        model = ClientInfo
        fields = ['ref', 'client_name', 'contact_phone', 'contact_email', 'contact_address']


class CollaboratorInfoForm(ModelForm):
    class Meta:
        model = CollaboratorInfo
        fields = ['ref', 'full_name', 'phone_number', 'role', 'email']
