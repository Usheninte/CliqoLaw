from django.db import models


class NewMatter(models.Model):
    reference_number = models.CharField(max_length=100, unique=True, default="#REF0000")
    client_name = models.CharField(max_length=250, unique=True, default="Client Name")
    nature_of_matter = models.TextField(default="Nature of Matter")
    price_estimate = models.IntegerField(default=100)
    hour_estimate = models.IntegerField(default=1)
    hourly_rate = models.IntegerField(default=100)

    def __str__(self):
        return "%s's Matter" % self.client_name


class NewClient(models.Model):
    ref = models.ForeignKey(NewMatter, to_field='reference_number',
                            on_delete=models.CASCADE, verbose_name='Reference Number')
    client_phone = models.CharField(max_length=20, default="+27123456789")
    client_email = models.EmailField(default="client@domain.com")
    client_address = models.TextField(default="Client Address")

    def __str__(self):
        return "%s - Client" % self.client_name


class NewContact(models.Model):
    ref = models.ForeignKey(NewMatter, to_field='reference_number',
                            on_delete=models.CASCADE, verbose_name='Reference Number')
    contact_name = models.CharField(max_length=250, default="Contact Name")
    contact_phone = models.CharField(max_length=20, default="+27123456789")
    contact_email = models.EmailField(default="contact@domain.com")
    contact_address = models.TextField(default="Contact Address")

    def __str__(self):
        return "%s - Client" % self.contact_name


class CollaboratorInfo(models.Model):
    ref = models.ForeignKey(NewMatter, to_field='reference_number',
                            on_delete=models.CASCADE, verbose_name='Reference Number')
    full_name = models.CharField(max_length=250, default="Collaborator Name")
    phone_number = models.CharField(max_length=20, default="+27123456789")
    role = models.CharField(max_length=150, default="Collaborator Role")
    email = models.EmailField(default="collab@domain.com")

    def __str__(self):
        return "%s - Collaborator" % self.full_name


class Outcome(models.Model):
    ref = models.ForeignKey(NewMatter, to_field='reference_number',
                            on_delete=models.CASCADE, verbose_name='Reference Number')
    goal = models.CharField(max_length=250, default="Ensure that ...")

    def __str__(self):
        return self.goal
