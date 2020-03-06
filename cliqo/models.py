from django.db import models


class NewMatter(models.Model):
    reference_number = models.CharField(max_length=100, unique=True, default="#REF0000")
    client_name = models.CharField(max_length=250, unique=True, default="Client Name")
    nature_of_matter = models.TextField(default="Nature of Matter")
    price_estimate = models.IntegerField(default=100)
    hour_estimate = models.IntegerField(default=1)
    hourly_rate = models.IntegerField(default=100)

    def __str__(self):
        return "{}'s Matter".format(self.client_name)


class NewClient(models.Model):
    ref = models.ForeignKey(NewMatter, to_field='reference_number',
                            on_delete=models.CASCADE, verbose_name='Reference Number')
    client_name = models.ForeignKey(NewMatter, to_field='client_name',
                                    on_delete=models.CASCADE, verbose_name='Client Name')
    client_phone = models.CharField(max_length=20, default="+27123456789")
    client_email = models.EmailField(default="client@domain.com")
    client_address = models.TextField(default="Client Address")
    contact_name = models.CharField(max_length=250, default="Contact Name")
    contact_phone = models.CharField(max_length=20, default="+27123456789")
    contact_email = models.EmailField(default="contact@domain.com")
    contact_address = models.TextField(default="Contact Address")

    def __str__(self):
        return "{} - Client".format(self.contact_name)


class Tasks(models.Model):
    BILL = 'Billable'
    NON_BILL = 'Non-billable'
    BILLING_CHOICES = [
        (BILL, 'Billable'),
        (NON_BILL, 'Non-billable')
    ]

    ref = models.ForeignKey(NewMatter, to_field='reference_number',
                            on_delete=models.CASCADE, verbose_name='Reference Number')
    task = models.CharField(max_length=250, default="Task")
    billing = models.CharField(max_length=12, choices=BILLING_CHOICES, default=BILL)

    def __str__(self):
        return "{} - {}".format(self.ref, self.task)
