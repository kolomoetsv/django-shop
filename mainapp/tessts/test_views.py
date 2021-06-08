from django.test import TestCase, Client


class ViewTestCase(TestCase):
    def test_post_creation(self):
        c = Client()
        response = c.get('/')
        self.assertEqual(response.status, 200)