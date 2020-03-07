from django.db import models


class NewMatter(models.Model):
    PERSON = 'Person'
    BIZ = 'Business'
    CLIENT_TYPES = [
        (PERSON, 'Person'),
        (BIZ, 'Business')
    ]

    reference_number = models.CharField(max_length=100, unique=True, default="#REF0000")
    client_name = models.CharField(max_length=250, default="Client Name")
    client_type = models.CharField(max_length=8, choices=CLIENT_TYPES, default=PERSON)
    nature_of_matter = models.TextField(default="Nature of Matter")
    price_estimate = models.IntegerField(default=100)
    hour_estimate = models.IntegerField(default=1)
    hourly_rate = models.IntegerField(default=100)

    def __str__(self):
        return "{}, {}".format(self.client_name, self.reference_number)


class NewContact(models.Model):
    ref = models.ForeignKey(NewMatter, to_field='reference_number',
                            on_delete=models.CASCADE, verbose_name='Reference Number')
    client_phone = models.CharField(max_length=20, default="+27123456789")
    client_email = models.EmailField(default="client@domain.com")
    client_address = models.TextField(default="Client Address")
    contact_name = models.CharField(max_length=250, default="Contact Name")
    contact_phone = models.CharField(max_length=20, default="+27123456789")
    contact_email = models.EmailField(default="contact@domain.com")
    contact_address = models.TextField(default="Contact Address")

    def __str__(self):
        return "{} (Contact for) {}".format(self.contact_name, self.ref)


class Tasks(models.Model):
    BILL = 'Billable'
    NON_BILL = 'Non-billable'
    BILLING_CHOICES = [
        (BILL, 'Billable'),
        (NON_BILL, 'Non-billable')
    ]

    ref = models.ForeignKey(NewMatter, to_field='reference_number',
                            on_delete=models.CASCADE, verbose_name='Reference Number')
    billing = models.CharField(max_length=12, choices=BILLING_CHOICES, default=BILL)

    def __str__(self):
        return "{} - {}".format(self.ref, self.task)
