from django.test import TestCase, Client, RequestFactory
from django.urls import reverse
from cliqo.views import MattersMainView
from cliqo.models import NewMatter, NewContact
from django.views.generic import DetailView


class TestViewsGeneral(TestCase):
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

    def setup(self):
        self.client = Client()

    def test_home_view_GET(self):
        response = self.client.get(reverse('index'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/home.html')

    def test_dashboard_view_GET(self):
        response = self.client.get(reverse('cliqo:dashboard'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'cliqo/dashboard.html')

    def test_newmatter_list_view_GET(self):
        response = self.client.get(reverse('cliqo:matters'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'cliqo/newmatter_list.html')

    # def test_matters_main_detail_view_GET(self):
        # response = self.client.get(reverse('cliqo:matter-focus'))
        # request = RequestFactory().get('main/mtr-1')
        # view = MattersMainView()
        # view.setup(request)
        #
        # context = view.get_context_data()
        # context['matters'] = NewMatter.objects.filter(pk=NewMatter.objects.first().pk)
        #
        # self.assertTrue(context)


class TestMattersMainView(TestCase):
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

    # class MattersMainView(DetailView):
    #     model = NewMatter
    #     template_name = 'cliqo/newmatter_main.html'

    def setUp(self):
        super(TestMattersMainView, self).setUp()
        self.request = RequestFactory().get('main/mtr-1')
        self.view = MattersMainView()

    def test_context_data(self):
        kwargs = {'pk': 1}
        context = self.view.get_context_data(**kwargs)
        context['matters'] = NewMatter.objects.filter(pk=self.get_object().pk)
        self.assertEqual(context['matters'], 'foo')
