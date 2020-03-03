from django.db import models


class NewMatter(models.Model):
    reference_number = models.CharField(max_length=100, unique=True, default="#REF0000")
    nature_of_matter = models.TextField()
    price_estimate = models.IntegerField()
    hourly_rate = models.IntegerField(default=100)

    def __str__(self):
        return "Matter %s" % self.reference_number


class ClientInfo(models.Model):
    ref = models.ForeignKey(NewMatter, to_field='reference_number',
                            on_delete=models.CASCADE, verbose_name='matter reference')
    client_name = models.CharField(max_length=200)
    contact_phone = models.CharField(max_length=20)
    contact_email = models.CharField(max_length=200)
    contact_address = models.TextField()

    def __str__(self):
        return "%s's Information" % self.client_name


class CollaboratorInfo(models.Model):
    ref = models.ForeignKey(NewMatter, to_field='reference_number',
                            on_delete=models.CASCADE, verbose_name='matter reference')
    full_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)
    role = models.CharField(max_length=100)
    email = models.CharField(max_length=200)

    def __str__(self):
        return "%s - Collaborator" % self.full_name


# class Outcomes(models.Model):
#     ref = models.ForeignKey(NewMatter, to_field='reference_number',
#                             on_delete=models.CASCADE, verbose_name='matter reference')
#     goal = models.CharField(max_length=300)
#
#     def __str__(self):
#         return self.goal
