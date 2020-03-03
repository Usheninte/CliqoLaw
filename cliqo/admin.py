from django.contrib import admin

from .models import NewMatter, ClientInfo, CollaboratorInfo, Outcomes


class NewMatterAdmin(admin.ModelAdmin):
    fields = ['client_name', 'nature_of_matter', 'price_estimate', 'contact_person']


class ClientInfoAdmin(admin.ModelAdmin):
    fields = ['ref', 'client_name', 'contact_phone', 'contact_email', 'contact_address']


class CollaboratorInfoAdmin(admin.ModelAdmin):
    fields = ['ref', 'full_name', 'phone_number', 'role', 'email']


class OutcomesAdmin(admin.ModelAdmin):
    fields = ['goal']


admin.site.register(NewMatter, NewMatterAdmin)
admin.site.register(ClientInfo, ClientInfoAdmin)
admin.site.register(CollaboratorInfo, CollaboratorInfoAdmin)
admin.site.register(Outcomes, OutcomesAdmin)
