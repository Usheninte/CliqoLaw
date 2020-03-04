from django.db import models


class NewMatter(models.Model):
    reference_number = models.CharField(max_length=100, unique=True, default="#REF0000")
    nature_of_matter = models.TextField()
    price_estimate = models.IntegerField()
    hourly_rate = models.IntegerField(default=100)
    client_name = models.CharField(max_length=250, default="Client Name")
    contact_name = models.CharField(max_length=250, default="Contact Name")
    contact_phone = models.CharField(max_length=20, default="+27123456789")
    contact_email = models.EmailField(default="contact@domain.com")
    contact_address = models.TextField(default="Contact Address")
    collaborator_full_name = models.CharField(max_length=250, default="Collaborator Name")
    collaborator_phone_number = models.CharField(max_length=20, default="+27123456789")
    collaborator_role = models.CharField(max_length=150, default="Collaborator Role")
    collaborator_email = models.EmailField(default="collab@domain.com")
    matter_goal = models.CharField(max_length=250, default="Ensure that ...")

    def __str__(self):
        return "%s's Matter" % self.client_name
