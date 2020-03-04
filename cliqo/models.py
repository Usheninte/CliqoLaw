from django.db import models


class NewMatter(models.Model):
    reference_number = models.CharField(max_length=100, unique=True, default="#REF0000")
    nature_of_matter = models.TextField(default="Nature of Matter")
    price_estimate = models.IntegerField(default=100)
    hourly_rate = models.IntegerField(default=100)
    client_name = models.CharField(max_length=250, default="Client Name")
    contact_name = models.CharField(max_length=250, default="Contact Name")
    contact_phone = models.CharField(max_length=20, default="+27123456789")
    contact_email = models.EmailField(default="contact@domain.com")
    contact_address = models.TextField(default="Contact Address")

    def __str__(self):
        return "%s's Matter" % self.client_name


class CollaboratorInfo(models.Model):
    ref = models.ForeignKey(NewMatter, to_field='reference_number',
                            on_delete=models.CASCADE, verbose_name='matter reference')
    full_name = models.CharField(max_length=250, default="Collaborator Name")
    phone_number = models.CharField(max_length=20, default="+27123456789")
    role = models.CharField(max_length=150, default="Collaborator Role")
    email = models.EmailField(default="collab@domain.com")

    def __str__(self):
        return "%s - Collaborator" % self.full_name


class Outcome(models.Model):
    ref = models.ForeignKey(NewMatter, to_field='reference_number',
                            on_delete=models.CASCADE, verbose_name='matter reference')
    goal = models.CharField(max_length=250, default="Ensure that ...")

    def __str__(self):
        return self.goal
