from django.test import TestCase
from cliqo.models import NewMatter, NewContact


class TestModels(TestCase):
    @classmethod
    def setUpTestData(cls):
        matter = NewMatter.objects.create(
            reference_number="REF0000",
            client_name="Client Name",
            client_type="Person",
            nature_of_matter="Nature of Matter",
            price_estimate=100,
            hour_estimate=1,
            hourly_rate=100,
        )

        contact = NewContact.objects.create(
            ref=matter,
            client_phone="+27123456789",
            client_email="client@domain.com",
            client_address="Client Address",
            contact_name="Contact Name",
            contact_phone="+27123456789",
            contact_email="contact@domain.com",
            contact_address="Contact Address",
        )

    def test_newmatter_model_return_value(self):
        matter = NewMatter.objects.first()
        client = getattr(matter, 'client_name')
        reference = getattr(matter, 'reference_number')
        self.assertEqual(str(matter),
                         "{}, {}".format(client, reference))

    def test_newcontact_model_return_value(self):
        contact = NewContact.objects.first()
        name = getattr(contact, 'contact_name')
        reference = getattr(contact, 'ref')
        self.assertEqual(str(contact),
                         "{} (Contact for) {}".format(name, reference))
