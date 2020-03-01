from django.db import models
from django.urls import reverse


class NewMatter(models.Model):
    client_name = models.CharField(max_length=250)
    nature_of_matter = models.TextField()
    price_estimate = models.IntegerField()
    contact_person = models.CharField(max_length=250)

    def __str__(self):
        return "%s's matter" % self.client_name

