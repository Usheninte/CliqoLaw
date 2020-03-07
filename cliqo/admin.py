from django.contrib import admin

from .models import NewMatter, NewContact


class NewMatterAdmin(admin.ModelAdmin):
    fields = ['reference_number', 'client_name',
              'nature_of_matter', 'price_estimate',
              'hour_estimate', 'hourly_rate']


class NewContactAdmin(admin.ModelAdmin):
    fields = ['ref', 'client_phone', 'client_email', 'client_address',
              'contact_name', 'contact_phone', 'contact_email', 'contact_address']


admin.site.register(NewMatter, NewMatterAdmin)
admin.site.register(NewContact, NewContactAdmin)
