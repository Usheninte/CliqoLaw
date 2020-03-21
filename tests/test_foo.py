from django.test import TestCase

foo = "bar"


class TestFoo(TestCase):

    def setup(self):
        pass

    def test_foo(self):
        self.assertEqual(foo, "bar")
        self.assertNotEqual(foo, "apple")
