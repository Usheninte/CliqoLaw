from django.contrib import admin

from .models import NewMatter, CollaboratorInfo, Outcome


class NewMatterAdmin(admin.ModelAdmin):
    fields = ['reference_number', 'nature_of_matter', 'price_estimate', 'hourly_rate',
              'client_name', 'contact_name', 'contact_phone', 'contact_email', 'contact_address']


class CollaboratorInfoAdmin(admin.ModelAdmin):
    fields = ['ref', 'full_name', 'phone_number', 'role', 'email']


class OutcomeAdmin(admin.ModelAdmin):
    fields = ['ref', 'goal']


admin.site.register(NewMatter, NewMatterAdmin)
admin.site.register(CollaboratorInfo, CollaboratorInfoAdmin)
admin.site.register(Outcome, OutcomeAdmin)