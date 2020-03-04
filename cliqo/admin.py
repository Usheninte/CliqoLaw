from django.contrib import admin

from .models import NewMatter, NewClient, NewContact, CollaboratorInfo, Outcome


class NewMatterAdmin(admin.ModelAdmin):
    fields = ['reference_number', 'client_name',
              'nature_of_matter', 'price_estimate',
              'hour_estimate', 'hourly_rate']


class NewClientAdmin(admin.ModelAdmin):
    fields = ['contact_name', 'contact_phone', 'contact_email', 'contact_address']


class NewContactAdmin(admin.ModelAdmin):
    fields = ['contact_name', 'contact_phone', 'contact_email', 'contact_address']


class CollaboratorInfoAdmin(admin.ModelAdmin):
    fields = ['ref', 'full_name', 'phone_number', 'role', 'email']


class OutcomeAdmin(admin.ModelAdmin):
    fields = ['ref', 'goal']


admin.site.register(NewMatter, NewMatterAdmin)
admin.site.register(NewClient, NewClientAdmin)
admin.site.register(NewContact, NewContactAdmin)
admin.site.register(CollaboratorInfo, CollaboratorInfoAdmin)
admin.site.register(Outcome, OutcomeAdmin)
