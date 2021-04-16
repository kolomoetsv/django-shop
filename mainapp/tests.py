from django.test import TestCase, Client


class ViewTestCase(TestCase):
    # Check the index page response
    def test_get_index_page(self):
        c = Client()
        response = c.get('/')
        self.assertEqual(response.status, 200)
