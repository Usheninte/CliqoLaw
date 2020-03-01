from django.contrib import admin

from .models import NewMatter


class NewMatterAdmin(admin.ModelAdmin):
    fields = ['client_name', 'nature_of_matter', 'price_estimate', 'contact_person']


admin.site.register(NewMatter, NewMatterAdmin)